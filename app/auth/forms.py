from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length



# clase para el formulario de registro, aun en desarrollo, utilizando wtf-formularios.
class SignupForm(FlaskForm):
    name = StringField('nombre', validators=[DataRequired()], render_kw={
                       'placeholder': 'Nombre', })
    apellido = StringField('apellido', validators=[DataRequired()], render_kw={
        'placeholder': 'apellido', })
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={
        'placeholder': 'email', })
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
        'placeholder': 'password', })
    submit = SubmitField('Registrar')



class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()], render_kw={
                        'placeholder': ' correo elentronico'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={
                             'placeholder': ' contraseña'})
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('login')
