from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length



class PostForm(FlaskForm):
    # photo = FileField('selecciona una imagen ', validators=[FileRequired()])
    title = StringField('Titulo', validators=[DataRequired()])
    title_slug = StringField('Titulo slug', validators=[Length(max=128)])
    precio = StringField('precio')
    content = TextAreaField('Descripcion del producto')
    submit = SubmitField('enviar')