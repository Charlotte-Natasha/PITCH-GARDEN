from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate
import psycopg2 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

# Initializing Application
def create_app():
    app = Flask(__name__) 
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='natasha245',pw='tasha',url='localhost',db='pitch')
    
    app.config['SECRET_KEY'] = 'charlotte'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


    

