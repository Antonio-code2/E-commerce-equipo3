from flask import Flask, render_template

app = Flask(__name__)

# ruta para la pagina de inicio o principal
# listado de productos
# listado de productos ==> producto   cuando el usuario seleccione un producto sera redirigido a la interfaz del producto


@app.route('/', methods=['GET'])
def index():# acciones => registrarse o iniciar sesion
    title = 'e-commerce | inicio'
    return render_template('index.html', title=title)


# ruta para el login de acceso

# si el usuario esta logeado se redireccionara a la pagina del home donde estan los productos pero con la vista de usuario donde podra hacer las demas funcionalidades
# si no esta mostrara la pagina del home sin las funcionalidades y se mostrara una alerta de que no esta logeado y si no tiene cuenta sera redireccionando con un boton al formulario de registro
# si es administrador sera redirrecionado a el dashboard administrativo
# login ==> index.html
@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Iniciar sesion'
    return render_template('login.html', title=title)


# ruta para el formulario de registro
# registro ==> index.html   cuando el usuario se registro sera redireccionado a lapagina de inicio o index
@app.route('/register', methods=['GET', 'POST'])
def registe():
    title = "crea una cuenta"
    return render_template('registro.html', title=title)


# ruta para la vista de un producto seleccionado
@app.route('/producto', methods=['GET'])
def producto():
    return render_template('DetalleProducto.html')


@app.route('/buscar', methods=['GET'])
def buscar_producto():
    return render_template('busqueda.html')


@app.route('/user_admin')
def user_admin():
    title = 'tu perfil | e-commerce'
    return render_template('admin/dashadmin.html', title=title)

# interfaz de administracion en pruebas
@app.route('/administracion')
def admin():
    usuario = 'administrador' # si tiene un rol diferente pero de administracion mostrara el mensaje con dicho rol
    mensaje = 'Hola ' + usuario + ' Bienvenidos a la interfaz de administracion, aqui podras administrar los productos, usuarios y roles'
    title = 'Administracion | e-commerce'
    return render_template('admin/admbase.html', mensaje=mensaje, usuario=usuario, title=title)

# ruta para la vista de la tabla de productos


@app.route('/table-product')
def product_admin():
    mensaje = 'administracion de la tabla de productos'
    title = 'Administracion | productos'
    return render_template('admin/table_product.html', mensaje=mensaje, title=title)


# ejecutable del la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
