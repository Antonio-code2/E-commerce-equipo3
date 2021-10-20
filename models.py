#librerias necesarias
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash #liberias para la encriptacion de la contraseña


#clase para las sesiones de usuarios
class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_paswword(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


# lista para almacenar los usuarios, recuerden que solo es temporal para pruebas, en un futuro se utilizara la base de datos
users = []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None
