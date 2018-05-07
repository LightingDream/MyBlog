from . import auth
from flask import render_template

@auth.route('/')
def hello_auth():
    return 'hello auth'

@auth.route('/')
def login():
    # return render_template('login.html')
    pass