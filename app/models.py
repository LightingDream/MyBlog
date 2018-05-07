#-*- coding: UTF-8 -*-
from . import db


class Article():
    pass


class User():
    pass


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