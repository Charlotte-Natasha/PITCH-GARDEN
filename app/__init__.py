from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import path
# from flask_login import LoginManager


# Initializing Application
app = Flask(__name__)


from .views import views
app.register_blueprint(views, url_prefix="/")