#librerias necesarias
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.core import BooleanField, IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileRequired


# clase para el formulario de registro, aun en desarrollo, utilizando wtf-formularios.
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()], render_kw={
                       'placeholder': 'Nombre', })
    apellido = StringField('Apellidos', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrar')


#clase para el fomulario para publicar los post
class PostForm(FlaskForm):
    # photo = FileField('selecciona una imagen ', validators=[FileRequired()])
    title = StringField('Titulo', validators=[DataRequired()])
    title_slug = StringField('Titulo slug', validators=[Length(max=128)])
    precio = StringField('precio')
    descripcion = TextAreaField('Descripcion del producto')
    submit = SubmitField('enviar')


#clase para el formulario de login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={
                        'placeholder': ' correo elentronico'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
                             'placeholder': ' contraseña'})
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Login')
