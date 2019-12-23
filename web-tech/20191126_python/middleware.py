from functools import wraps
from flask import g, request, redirect, url_for, make_response

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in g:
            if g.username is None:
                return redirect(url_for('login'), 200)
        return f(*args, **kwargs)
    return decorated_function

