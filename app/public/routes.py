from  flask import abort, render_template

from app.models import Post
from . import public_bp


@public_bp.route('/')
def index():  # acciones => reg
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route('/p/<string:slug>/')
def post_view(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template('public/post_view.html', post=post)
# ruta para la vista de un producto seleccionado


@public_bp.route('/buscar', methods=['GET'])
def buscar_producto():
    return render_template('public/busqueda.html')


