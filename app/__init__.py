from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os, string, random

db = SQLAlchemy()
DB_NAME = "database.db"


def create_database(app):
    try:
        db.create_all()
    except:
        with app.app_context():
            db.create_all()

def secret_key(app):
    SECRET_KEY  = os.getenv('SECRET_KEY')
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))
    app.config['SECRET_KEY'] = SECRET_KEY



def create_app():
    app = Flask(__name__)
    secret_key(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #from .authentication.views import auth as authentication_blueprint
    from .home.views import views

    #app.register_blueprint(authentication_blueprint, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    #login_manager = LoginManager()
    #login_manager.init_app(app)

    return app


