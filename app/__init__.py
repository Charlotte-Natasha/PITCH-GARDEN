from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate
# import psycopg2 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

# Initializing Application
def create_app():
    app = Flask(__name__) 
    # DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='natasha245',pw='tasha',url='localhost',db='pitch')
    
    app.config['SECRET_KEY'] = 'charlotte'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(100), nullable=False, unique=True)
        username = db.Column(db.String(100))
        password = db.Column(db.String(100))
        name = db.Column(db.String(100), nullable=False)
        date_added = db.Column(db.DateTime, default=datetime.utcnow)


        def __repr__(self): 
            return '<Name %r>' %self.name    

    class UserForm(FlaskForm):
        name = StringField("Name", validator=[DataRequired()])
        email = StringField("Email", validator=[DataRequired()])
        submit = SubmitField("Submit")

    return app


    

