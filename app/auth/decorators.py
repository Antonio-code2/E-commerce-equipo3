from functools import wraps
from flask import abort
from flask.scaffold import F
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        id_admin = getattr(current_user, 'id_admin', False)
        if not id_admin:
            abort (401)
        return f(*args, **kws)
    return decorated_function
        
    