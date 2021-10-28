from flask import app
from werkzeug.utils import send_from_directory
from app import create_app
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

# esta funcion tambien sirve para el proceso de subir las imagenes que se hacen en el archivo admin/route.py
@app.route('/media/posts/<filename>')
def media_posts(filename):
    dir_path = os.path.join(
        app.config['MEDIA_DIR'],
        app.config['POSTS_IMAGES_DIR'])
    return send_from_directory(dir_path, filename)




#esta funcion de aqui si funciona pero no muestra las imagenes, pueden comentar la funcion de arriba y desomentar esta de abajo, junto con lo que les dije en el archivo admin/route.py

# @app.route('/media/productos/<filename>')
# def media_posts(filename):
#     dir_path= os.path.join(
#         app.config['UPLOAD_MEDIA'])
#     return send_from_directory(dir_path, filename)
    
# ejecutable del la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
