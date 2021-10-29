from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    # photo = FileField('selecciona una imagen ', validators=[FileRequired()])
    title = StringField('Titulo', validators=[DataRequired()])
    title_slug = StringField('Titulo slug', validators=[Length(max=128)])
    precio = StringField('precio')
    post_image = FileField('imagen de cabecera', validators=[FileAllowed(['jpg', 'png'], 'solo se permiten imagenes')])
    descripcion = TextAreaField('Descripcion del producto')
    image_name = StringField('image_name')
    submit = SubmitField('enviar')


class UserAdminForm(FlaskForm):
    id_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')