from flask import Blueprint
from flask import render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<h1>Login</h1>"


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/sign-up')
def sign_up():
    return "<h1>sign-up</h1>"