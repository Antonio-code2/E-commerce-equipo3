from  flask import abort, render_template

from app.models import productos
from . import public_bp


@public_bp.route('/')
def index():  # acciones => reg
    posts = productos.query.all()
    print("consulta: ", posts)
    return render_template("public/index.html", posts=posts)


@public_bp.route('/p/<string:slug>/')
def post_view(slug):
    post = productos.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template('public/post_view.html', post=post)
# ruta para la vista de un producto seleccionado


@public_bp.route('/buscar', methods=['GET'])
def buscar_producto():
    return render_template('public/busqueda.html')


