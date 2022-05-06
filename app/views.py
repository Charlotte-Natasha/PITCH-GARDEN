from flask import render_template
from flask import Blueprint
from app import app

views = Blueprint("views", __name__)

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')