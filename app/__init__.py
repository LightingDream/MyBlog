from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .admin import admin
from .main import main
from .auth import auth
from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.debug=True
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')
    return app