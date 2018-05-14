from . import main
from flask import redirect, render_template, \
    flash
from flask_login import login_user
from ..models import User, Article, ArticleType


@main.route('/')
def index():
    flash(u'欢迎！', 'success')
    user = User.query.filter_by(username='adrui').first()
    login_user(user)
    return render_template('base.html')
    pass


@main.route('/article/details/<int:id>')
def article_details(id):
    article = Article.query.get(id)
    return render_template('article_detail.html', article=article)
    pass


@main.route('/article/types/<int:id>')
def article_types(id):
    article_type = ArticleType.query.get(id)
    return render_template('article_type.html', article_type=article_type)
    pass


@main.route('/article/sources/<int:id>')
def article_sources(id):
    return 'Source'
    pass


@main.route('/admin')
#@login_required
def edit_article():
    pass
