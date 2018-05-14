from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate
from app.models import Menu, ArticleType, User, Source

app = create_app()
db.create_all()
manager = Manager(app)
migrate = Migrate(app, db)

app.config['SESSION_TYPE'] = 'filesystem'
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
    db.drop_all()
    db.create_all()

    if deploy_type == 'generate_data':
        # step_1:insert navs
        Menu.init_menus()
        ArticleType.init_articleTypes()
        User.insert_admin('2456700829@qq.com', 'adrui', 'adjsjZBR1996')
        Source.insert_source()


if __name__ == '__main__':
    manager.run()
