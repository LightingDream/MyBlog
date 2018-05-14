from . import admin
from flask import redirect, render_template, url_for, flash
from flask_login import login_required
from .forms import WriteArticlesForm
from ..models import ArticleType, Source, Article
from .. import db


@admin.route('/')
@login_required
def index():
    flash(u'欢迎回来', 'success')
    return render_template('admin/admin_base.html')
    pass


@admin.route('/write-articles', methods=['GET', 'POST'])
@login_required
def write_articles():
    form = WriteArticlesForm()

    sources = [(s.id, s.name) for s in Source.query.all()]
    form.source.choices = sources
    types = [(t.id, t.name) for t in ArticleType.query.all()]
    form.type.choices = types

    if form.validate_on_submit():
        title = form.title.data
        type_id = form.type.data
        content = form.content.data
        summary = form.summary.data
        source_id = form.source.data
        source = Source.query.get(source_id)
        articleType = ArticleType.query.get(type_id)
        if source and articleType:
            article = Article(title=title, content=content, summary=summary,
                              source=source, articleType=articleType)
            db.session.add(article)
            db.session.commit()
            flash(u'发表博文成功！', 'success')
            article_id = Article.query.filter_by(title=title).first().id
            return redirect(url_for('admin.index', id=article_id))
        pass
    return render_template('admin/write_articles.html', form=form)
    pass

