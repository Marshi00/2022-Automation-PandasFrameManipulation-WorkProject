
import functools
from flask import session , redirect

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect('/#login')
        return func(*args, **kwargs)

    return secure_function

def not_logged_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "user_id" in session:
            return redirect('/')
        return func(*args, **kwargs)

    return secure_function