from . import admin
from flask import redirect, render_template, url_for


@admin.route('/')
def hello_admin():
    return 'hello admin'


@admin.route('/write_article/<int:id>')
def write_article(id):
    return redirect(url_for('main.detail', id = id))
    pass

