from flask import Flask, render_template, request, redirect, url_for, current_app
from flask_login.utils import login_user
from flask_wtf import form
from forms import LoginForm, PostForm, SignupForm
from flask_login import LoginManager, login_manager, current_user, login_user, logout_user
from models import User, get_user, users
from werkzeug.urls import url_parse




app = Flask(__name__)
#llave secreta, se puede cambiar por la que quieran
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
# ruta para la pagina de inicio o principal
# listado de productos
# listado de productos ==> producto   cuando el usuario seleccione un producto sera redirigido a la interfaz del producto


login_manager = LoginManager(app)

#esta es una lista donde se almacenan los post o produtos, pero solo es temporalmente, cuando se reincia el servidor los post se eliminan
posts = []


@app.route('/', methods=['GET'])
def index():  # acciones => reg
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    return render_template('index.html', posts=posts)


# ruta para el login de acceso

# si el usuario esta logeado se redireccionara a la pagina del home donde estan los productos pero con la vista de usuario donde podra hacer las demas funcionalidades
# si no esta mostrara la pagina del home sin las funcionalidades y se mostrara una alerta de que no esta logeado y si no tiene cuenta sera redireccionando con un boton al formulario de registro
# si es administrador sera redirrecionado a el dashboard administrativo
# login ==> index.html
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    title = 'Iniciar sesion'
    return render_template('login.html', title=title, form=form)


#esta ruta es para cerrar la sesion
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# ruta para el formulario de registro
# registro ==> index.html   cuando el usuario se registro sera redireccionado a lapagina de inicio o index
@app.route('/register/', methods=['GET', 'POST'])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()  # instancia de la clase signupform
    if form.validate_on_submit():
        name = form.name.data
        apellido = form.apellido.data
        email = form.email.data
        password = form.password.data
        # creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, apellido, email, password)
        users.append(user)
        # dejamos el usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    title = "crea una cuenta"
    return render_template('registro.html', title=title, form=form)


@app.route('/p/<string:slug>/')
def post_view(slug):
    return render_template('DetalleProducto.html', slug_title=slug)
# ruta para la vista de un producto seleccionado


# ruta para la busqueda de productos por categoria, aun no se ha implementado
@app.route('/buscar', methods=['GET'])
def buscar_producto():
    return render_template('busqueda.html')

# ruta para entrar al perfil de el administrado, cuando este se loguee sera enviado a esta interfaz, y es el caso de que el super administrado agrege a otros administradores, esta sera la interfaz que se les mostrara cuando el registro este verificado
@app.route('/user_admin')
def user_admin():
    return render_template('admin/dashadmin.html')



# interfaz de administracion en pruebas
@app.route('/admin/')
def admin():
    # si tiene un rol diferente pero de administracion mostrara el mensaje con dicho rol
    usuario = 'administrador'
    mensaje = 'Hola ' + usuario + \
        ' Bienvenidos a la interfaz de administracion, aqui podras administrar los productos, usuarios y roles'
    return render_template('admin/admbase.html', mensaje=mensaje, usuario=usuario)



# ruta para la vista de la tabla de productos
@app.route('/table-product')
def product_admin():
    mensaje = 'administracion de la tabla de productos'
    return render_template('admin/table_product.html', mensaje=mensaje)


# rutas para publicar post/productos y editar post/productos
@app.route('/admin/post/', methods=['GET', 'POST'], defaults={'post_id': None})
@app.route('/admin/post/<int:post_id>/', methods=['GET', 'POST'])
def post_form(post_id):
    form = PostForm()  # instanciando la clase de postform
    if form.validate_on_submit():
        #dato del formulario para publicar un post
        title = form.title.data
        precio = form.precio.data
        title_slug = form.title_slug.data
        descripcion = form.descripcion.data

        post = {'title': title, 'precio': precio,
                'title_slug': title_slug, 'descripcion': descripcion}
        posts.append(post)

        return redirect(url_for('index'))

    mensaje = 'agregar productos'
    return render_template('admin/add_producto.html', form=form, mensaje=mensaje)


#sesiones
@login_manager.user_loader
def load_user(user_id):
    login_manager = LoginManager(app)
    login_manager.login_view = "login"
    for user in users:
        if user.id == int(user_id):
            return user
    return None


# ejecutable del la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
