from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app.models import Post
from . import admin_bp
from .forms import PostForm



# rutas para publicar post/productos y editar post/productos
@admin_bp.route('/admin/post/', methods=['GET', 'POST'], defaults={'post_id': None})
@admin_bp.route('/admin/post/<int:post_id>/', methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()  # instanciando la clase de postform
    if form.validate_on_submit():
        # photo = form.photo.data
        # filename = secure_filename(photo.filename)
        # photo.save(app.root_path+"/static/productos/"+filename)
        title = form.title.data
        precio = form.precio.data
        content = form.content.data

        post = Post(user_id=current_user.id, title=title, precio=precio, content=content)
        post.save()

        return redirect(url_for('public.index'))

    mensaje = 'agregar productos'
    return render_template('admin/add_producto.html', form=form, mensaje=mensaje)



@admin_bp.route('/user_admin')
def user_admin():
    return render_template('admin/dashadmin.html')


# interfaz de administracion en pruebas
@admin_bp.route('/admin/')
def admin():
    # si tiene un rol diferente pero de administracion mostrara el mensaje con dicho rol
    usuario = 'administrador'
    mensaje = 'Hola ' + usuario + \
        ' Bienvenidos a la interfaz de administracion, aqui podras administrar los productos, usuarios y roles'
    return render_template('admin/admbase.html', mensaje=mensaje, usuario=usuario)

# ruta para la vista de la tabla de productos


@admin_bp.route('/table-product')
def product_admin():
    mensaje = 'administracion de la tabla de productos'
    return render_template('admin/table_product.html', mensaje=mensaje)


