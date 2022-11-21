from flask_wtf import FlaskForm
from wtforms import fields
from wtforms import validators

from app.models import Book


class LoginForm(FlaskForm):
    email = fields.EmailField(
        'E-mail', validators=[validators.Email('E-Mail invalido')])
    password = fields.PasswordField('Password', validators=[validators.Length(
        3, 30, "O campo deve conter de 3 a 30 caracteres")])
    remember = fields.BooleanField('Permanecer Conectado')
    submit = fields.SubmitField('Login')


class RegisterForm(FlaskForm):
    name = fields.StringField(
        'Nome Completo', validators=[validators.DataRequired()])
    email = fields.EmailField(
        'E-mail', validators=[validators.Email('E-Mail invalido'), validators.DataRequired()])
    password = fields.PasswordField('Password', validators=[validators.Length(
        3, 30, "O campo deve conter de 3 a 30 caracteres"), validators.DataRequired()])

    submit = fields.SubmitField('Cadastrar')


class BookForm(FlaskForm):
    name = fields.StringField(
        'Nome do Livro', validators=[validators.DataRequired('Campo Obrigatório')])

    submit = fields.SubmitField('Salvar')


class UserBookForm(FlaskForm):
    book = fields.SelectField("Livro", coerce=int)
    submit = fields.SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [
            (book.id, book.name) for book in Book.query.all()
        ]
