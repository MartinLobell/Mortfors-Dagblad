from wtforms import Form, StringField, SubmitField, TextAreaField, DateTimeField, validators, PasswordField, DateField, IntegerField
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
    brodtext = TextAreaField("Brödtext", [validators.DataRequired()])
    datum = DateField("Datum XXXX-XX-XX", [validators.DataRequired()])
    p_nr = IntegerField("Anställningsnummer", [validators.DataRequired()])