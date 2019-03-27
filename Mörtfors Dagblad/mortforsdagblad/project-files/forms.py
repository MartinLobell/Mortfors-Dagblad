from wtforms import Form, validators, StringField, SubmitField, TextAreaField, DateTimeField, PasswordField, DateField, IntegerField, SelectField
import datetime

class CommentaryForm(Form):
    namn = StringField("Namn", [validators.DataRequired()])
    kommentar = TextAreaField("Kommentar", [validators.DataRequired()])
    submit = SubmitField("Skicka")

class LoginForm(Form):
    username = StringField("Användare", [validators.DataRequired()])
    password = PasswordField("Lösenord", [validators.DataRequired()])

class ArticleForm(Form):
    rubrik = StringField("Rubrik", [validators.DataRequired()])
    ingress = StringField("Ingress", [validators.DataRequired()])
    text = TextAreaField("Text", [validators.DataRequired()])
    datum = DateField("Datum ÅÅÅÅ-MM-DD", [validators.DataRequired()])
    undkat_id = SelectField("Underkategori", choices=[('1', 'Staden'), ('2', 'Landsbygden'), ('3', 'Europa'), ('4', 'Nordamerika'), ('5', 'Sydamerika'), ('6', 'Afrika'), ('7', 'Asien'), ('8', 'Oceanien'), ('9', 'Fotboll'), ('10', 'Hockey'), ('11', 'Tennis'), ('12', 'Basket'), ('13', 'Ridsport'), ('14', 'Simning'), ('15', 'Musik'), ('16', 'Film'), ('18', 'Litteratur'), ('19', 'Teater'), ('20', 'Varmt'), ('21', 'Kallt')])
    p_nr = SelectField("Journalist", choices=[('1', 'Eyvind Svensson'), ('2', 'Karl-Alfred S. Ohs'), ('3', 'Ann-Christine Hollandaise'), ('4', 'Guido Bolognese'), ('5', 'Boonsri Sriracha'), ('6', 'Kent von Schnabel'), ('7', 'Tza Tziki'), ('8', 'Bea R. Näs')])