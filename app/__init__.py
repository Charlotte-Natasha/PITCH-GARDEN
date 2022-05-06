from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from app.config import DevConfig

# Initializing Application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from .views import views
app.register_blueprint(views, url_prefix="/")