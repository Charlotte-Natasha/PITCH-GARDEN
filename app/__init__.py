from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import sqlite3
#from flask_login import LoginManager

# Initializing Application
def create_app():
    app = Flask(__name__)


    from .views import views
    from .request import request
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(request, url_prefix="/")

    return app
    

