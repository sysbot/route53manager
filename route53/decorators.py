from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.identity.name == 'anon':
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function