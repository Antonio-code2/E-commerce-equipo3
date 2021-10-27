from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required
from werkzeug.urls import url_parse
from app import login_manager
from . import auth_bp
from .forms import SignupForm, LoginForm
from .models import User



# ruta para el formulario de registro
# registro ==> index.html   cuando el usuario se registro sera redireccionado a lapagina de inicio o index
@auth_bp.route('/register/', methods=['GET', 'POST'])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = SignupForm()  # instancia de la clase signupform
    error = None
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        password = form.password.data
        #comprobamos que no hay un usuario con es email
        user = User.get_by_email(email)
        if user is not None:
            error = f'el email {email} ya esta siendo utilizado por otro usuario'
        else:

        # creamos el usuario y lo guardamos
            user = User(nombre=nombre, email=email, apellido=apellido)
            user.set_password(password)
            user.save()
        # dejamos el usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            return redirect(next_page)
    title = "crea una cuenta"
    return render_template('auth/registro.html', title=title, form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


# ruta para el login de acceso
# si el usuario esta logeado se redireccionara a la pagina del home donde estan los productos pero con la vista de usuario donde podra hacer las demas funcionalidades
# si no esta mostrara la pagina del home sin las funcionalidades y se mostrara una alerta de que no esta logeado y si no tiene cuenta sera redireccionando con un boton al formulario de registro
# si es administrador sera redirrecionado a el dashboard administrativ
# login ==> index.html


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            return redirect(next_page)
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))



@auth_bp.route('/view_user/')
@login_required
def view_user():
    return render_template('auth/view_User.html')



