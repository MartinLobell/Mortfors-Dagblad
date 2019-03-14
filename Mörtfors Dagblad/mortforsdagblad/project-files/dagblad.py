from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import CommentaryForm, LoginForm, ArticleForm
from functools import wraps
import psycopg2

app = Flask(__name__)
mddb = psycopg2.connect(host = "pgserver.mah.se",
                        user="m11p3220",
                        password = "a4e094h8",
                        database = "m11p3220")
cursor = mddb.cursor()

def is_logged_in(f):

# Den funktion som tillgängliggör innehåll enbart för inloggade användare.
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bara för behöriga, sorry!", "success")
            return redirect(url_for("login"))
    return wrap

@app.route("/")
def index():

# Listar alla databasens artiklar med den nyaste överst.
    cursor.execute("SELECT * FROM artikel ORDER BY datum DESC")
    texts = cursor.fetchall()

    return render_template("index.html", texts=texts)

@app.route("/login", methods=["GET", "POST"])
def login():

# Inloggningsformulär för administratören.
    form = LoginForm(request.form)
    if request.method == "POST":
        username = request.form["username"]
        password_candidate = request.form["password"]

        cursor = mddb.cursor()
        signature = cursor.execute("SELECT * FROM admin WHERE username = %s", (username,))
        data = cursor.fetchone()

# Om användarnamn och lösenord finns registrerade skapas en logged in-session.
        if len(data) != 0:
            password = data[0]
            username = data[0]
            session["logged_in"] = True
            session["username"] = username
            flash("Välkommen!", "success")
            return redirect(url_for("index"))
            cursor.close()
        else:
            flash("Ingen användare med denna epost hittades", "danger")
            return render_template("login.html", form=form)
    else:
        return render_template("login.html", form=form, title="Logga in")
        
@app.route("/logout/")
@is_logged_in

# Stänger av logged in-sessionen och användaren återgår till det "vanliga" innehållet.
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/artikel/<art_id>", methods=["GET", "POST"])
def article(art_id): 

# Hämtar den artikel som klickats på.
    cursor = mddb.cursor()
    cursor.execute("""SELECT * FROM artikel 
                      WHERE art_id = %s""",
                      (art_id,))
    article_full = cursor.fetchone()   

# Hämtar tillhörande journalist(er) till vald artikel via en sambandstabell.
    cursor = mddb.cursor()
    cursor.execute("""SELECT j.namn, j.p_nr FROM artikel as a 
                    JOIN skriven_av as s
                    JOIN journalist as j
                    ON a.art_id = s.art_id
                    AND s.journalist = j.p_nr
                    AND a.art_id = %s""", 
                    (art_id,))
    authors = cursor.fetchall()

# Hämtar tillhörande bild(er) till vald artikel via en sambandstabell.
    cursor.execute("""SELECT b.bildfil, b.alt_text, s.bildtext FROM artikel as a 
                    JOIN artikel_bild as s
                    JOIN bild as b
                    ON a.art_id = s.art_id
                    AND s.bild_id = b.bild_id
                    AND a.art_id = %s""", 
                    (art_id,))
    photos = cursor.fetchall()

# Kommentarformulär för vald artikel.
    form = CommentaryForm(request.form)
    if form.validate():
      namn = form.namn.data.strip()
      kommentar = form.kommentar.data.strip()

# Lägger in kommentarer tillhörande vald artikel till databasen.
      cursor = mddb.cursor()
      cursor.execute("""INSERT INTO kommentar (art_id, namn, kommentar) 
                    VALUES (%s, %s, %s)""", 
                    (art_id, namn, kommentar))
      mddb.commit()
      cursor.close()
      return redirect(url_for("index"))

# Listar kommentarer tillhörande vald artikel.
    cursor = mddb.cursor()
    cursor.execute("""SELECT namn, kommentar, tid_datum, kom_id
    FROM kommentar
    where art_id = %s""", 
    (art_id,))
    comments = cursor.fetchall()

    return render_template("artikel.html", title="Artikel", form=form, article_full=article_full, comments=comments, authors=authors, photos=photos)

@app.route("/add_article", methods=["GET", "POST"])
@is_logged_in
def add_article():

# Formulär för att skriva in en ny artikel.
    form = ArticleForm(request.form)
    if form.validate():
        rubrik = form.rubrik.data.strip()
        ingress = form.ingress.data.strip()
        brodtext = form.brodtext.data.strip()
        datum = form.datum.data
        p_nr = form.p_nr.data

# Lägger in ny artikel till databasen.
        cursor.execute("""INSERT INTO artikel (rubrik, ingress, brodtext, datum) 
                        VALUES (%s, %s, %s, %s)""",
                        (rubrik, ingress, brodtext, datum))

    # Hämtar artikel-ID från den senast inlagda artikeln.
        cursor.execute("SELECT art_id FROM artikel ORDER BY art_id DESC LIMIT 1;")
        latest_article = cursor.fetchone()
        art_id = latest_article[0]

    # Lägger till artikel-ID från den senast inlagda artikeln i sambandstabellen.
        cursor.execute("""INSERT INTO skriven_av (art_id, journalist)
                            VALUES (%s, %s)""", 
                            (int(art_id), p_nr))

        mddb.commit()
        cursor.close()
        return redirect(url_for("index"))

    return render_template("add_article.html", title="Skriv artikel", form=form)

@app.route("/journalist/<p_nr>")
def journalist(p_nr):

# Hämtar vald journalist.
    cursor.execute("""SELECT * FROM journalist 
                    WHERE p_nr = %s""",
                    (p_nr,))
    journalist_info = cursor.fetchone()

    return render_template("journalist.html", title="Journalist", journalist_info=journalist_info)
    
@app.route("/delete_comment/<kom_id>", methods=["GET", "POST"])
@is_logged_in
def delete_comment(kom_id):

# Tar bort vald kommentar från databasen.
    cursor.execute("DELETE FROM kommentar WHERE kom_id = %s", (kom_id,))
    mddb.commit()
    cursor.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(port=8080, debug=True)