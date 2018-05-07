from . import main
from flask import redirect, render_template, \
    flash
# from .. import db


@main.route('/')
def index():
    flash(u'欢迎！', 'success')
    return render_template('base.html')
    pass


@main.route('/article/detail-<int:id>')
def detail(id):
    pass

@main.route('/admin')
#@login_required
def edit_article():
    pass
