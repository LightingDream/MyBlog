#-*- coding: UTF-8 -*-
from . import db, loginManager
from flask_login import UserMixin, login_user
from datetime import datetime


class Comment():
    pass


menu_articleType = {
    'ACM':[u'Codeforces', u'牛客网', 'Leetcode', u'计蒜客'],
    u'数据结构':['Tree', 'Stack', 'Queue', u'线性表'],
    'Algorithm':['Kmp', u'AC自动机', u'数论'],
    u'考研笔记':[u'高数', u'计算机网络', u'数据结构', u'计算机组成原理', u'操作系统'],
    'Life': [u'生活记录', u'那些人', u'竞赛'],
    'Program Language':['C++', 'Java', 'Python']
}


class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    types = db.relationship('ArticleType', backref='menu', lazy='dynamic')

    @staticmethod
    def init_menus():
        for name in menu_articleType.keys():
            menu = Menu(name=name)
            db.session.add(menu)
            db.session.commit()

    def __repr__(self):
        return '<Menu: %s>' % self.name
    pass


class ArticleType(db.Model):
    __tablename__ = 'articleType'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), default=None)
    articles = db.relationship('Article', backref='articleType', lazy='dynamic')
    @staticmethod
    def init_articleTypes():
        for menu_name, articleTypes in menu_articleType.items():
            menu = Menu.query.filter_by(name=menu_name).first()
            for name in articleTypes:
                articleType = ArticleType(name=name)
                articleType.menu = menu
                db.session.add(articleType)
        db.session.commit()

    def __repr__(self):
        return '<ArticleType: %s>' % self.name
    pass


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))

    @staticmethod
    def insert_admin(email, username, password):
        user = User(email=email,username=username,password=password)
        db.session.add(user)
        db.session.commit()

    def check_user(self, password):
        return password == self.password
    pass


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Source(db.Model):
    __tablename__ = 'source'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='source', lazy='dynamic')

    @staticmethod
    def insert_source():
        sources = [u'原创', u'转载']
        for s in sources:
            source = Source(name=s)
            db.session.add(source)
            db.session.commit()
    pass


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    content = db.Column(db.Text)
    summary = db.Column(db.Text)
    create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    num_of_view = db.Column(db.Integer, default=0)
    articleType_id = db.Column(db.Integer, db.ForeignKey('articleType.id'))
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    # comments = db.relationship('Comment', backref='article', lazy='dynamic')

    @staticmethod
    def add_view(article, db):
        article.num_of_view += 1
        db.session.add(article)
        db.session.commit()

    def __repr__(self):
        return '<Article %r>' % self.title