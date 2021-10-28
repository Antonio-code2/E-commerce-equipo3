import os
from flask import render_template, redirect, url_for, abort, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.auth.decorators import admin_required
from app.auth.models import User
from app.models import productos
from . import admin_bp
from .forms import PostForm, UserAdminForm



@admin_bp.route('/admin/user/', methods=['GET', 'POST'] )
def user_admin():
    if not current_user.id_admin:
        return redirect('/')
    return render_template('admin/dashadmin.html')



@admin_bp.route('/admin/')
def admin():
    return render_template('admin/admbase.html')


# rutas para publicar post/productos y editar post/productos
@admin_bp.route('/admin/posts/')
@login_required
@admin_required
def list_posts():
    posts = productos.get_all()
    return render_template("admin/table_product.html", posts=posts)

@admin_bp.route("/admin/post/", methods=['GET', 'POST'])
@login_required
# @admin_required   
def post_form():
    form = PostForm()  # instanciando la clase de postform
    if form.validate_on_submit():
        title = form.title.data
        precio = form.precio.data
        descripcion = form.descripcion.data
        file = form.post_image.data
        image_name = None
        # comprueba si la peticion contiene la parte el fichero
        if file:
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['POSTS_IMAGES_DIR']
            #fase de pruebas para subir imagenes, si quieren probar pueden borrar la linea de arriba y descomentar las dos de abajo
            
            # upload_media = "./static/posts"
            # images_dir = current_app.config['UPLOAD_MEDIA'] = upload_media
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)
        post = productos(user_id=current_user.id, title=title, precio=precio, descripcion=descripcion)
        post.image_name=image_name
        post.save()
        return redirect(url_for('admin.list_posts'))

    mensaje = 'agregar productos'
    return render_template('admin/add_producto.html', form=form, mensaje=mensaje)


#actualizar un post 
@admin_bp.route('/admin/post/<int:post_id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def actualizar_post(post_id):
    #actualizar un post existente
    post = productos.get_by_id(post_id)
    if post is None:
        print(f'el post  {post_id} no existe')
        abort(404)
    #formulario con los campos y valores del post
    form = PostForm(obj=post)
    if form.validate_on_submit():
        #actualiza los campos del post existente
        post.title = form.title.data
        post.descripcion = form.descripcion.data
        post.save()
        print(f'guardando el post {post_id}')
        return redirect(url_for('admin.list_posts'))
    return render_template("admin/add_producto.html", form=form, post=post)
        
        
    


#eliminar un post
@admin_bp.route("/admin/post/delete/<int:post_id>/", methods=['POST', 'GET'])
@login_required
@admin_required
def delete_post(post_id):
    print(f'Se va a eliminar el post {post_id}')
    post = productos.get_by_id(post_id)
    if post is None:
        print(f'El post {post_id} no existe')
        abort(404)
    post.delete()
    print(f'El post {post_id} ha sido eliminado')
    return redirect(url_for('admin.list_posts'))



#listado de usuarios regisrados
@admin_bp.route("/admin/users/")
@login_required
@admin_required
def list_user():
    users = User.get_all()
    return render_template("admin/users.html", users=users)
    
# vista para que un administrador pueda colocarle el rol de administrdor
@admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_user_form(user_id):
    # Aquí entra para actualizar un usuario existente
    user = User.get_by_id(user_id)
    if user is None:
        print(f'El usuario {user_id} no existe')
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del usuario.
    form = UserAdminForm(obj=user)
    if form.validate_on_submit():
        # Actualiza los campos del usuario existente
        user.id_admin = form.id_admin.data
        user.save()
        print(f'Guardando el usuario {user_id}')
        return redirect(url_for('admin.list_user'))
    return render_template("admin/user_form.html", form=form, user=user)

#eliminar un usuario

@admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_user(user_id):
    print(f'Se va a eliminar al usuario {user_id}')
    user = User.get_by_id(user_id)
    if user is None:
        print(f'El usuario {user_id} no existe')
        abort(404)
    user.delete()
    print(f'El usuario {user_id} ha sido eliminado')
    return redirect(url_for('admin.list_user'))