from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import Menu, ArticleType

app = create_app()
db.create_all()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

app.config['SECRET_KEY'] = '123456'
#Global variables
app.jinja_env.globals['ArticleType'] = ArticleType
# app.jinja_env.globals['article_types'] = article_types
app.jinja_env.globals['Menu'] = Menu
# app.jinja_env.globals['BlogInfo'] = BlogInfo
# app.jinja_env.globals['Plugin'] = Plugin
# app.jinja_env.globals['Source'] = Source
# app.jinja_env.globals['Article'] = Article
# app.jinja_env.globals['Comment'] = Comment
# app.jinja_env.globals['BlogView'] = BlogView

@manager.command
def deploy(deploy_type):
    from flask_migrate import upgrade
    #upgrade()
    db.drop_all()
    db.create_all()
    if deploy_type == 'init':
        pass

    # You must run `python manage.py deploy(product)` before run `python manage.py deploy(test_data)`
    if deploy_type == 'generate_data':
        # step_1:insert navs
        Menu.init_menus()
        ArticleType.init_articleTypes()
        # step_2:insert articleTypes
        # ArticleType.insert_articleTypes()
        # # step_3:generate random articles
        # Article.generate_fake(100)
        # # step_4:generate random comments
        # Comment.generate_fake(300)
        # # step_5:generate random replies
        # Comment.generate_fake_replies(100)
        # # step_4:generate random comments
        # Comment.generate_fake(300)


if __name__ == '__main__':
    l = Menu.query.all()
    for i in l:
        print(i.name)
    manager.run()
