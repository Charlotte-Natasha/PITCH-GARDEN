from flask import render_template
from flask import Blueprint

views = Blueprint("views", __name__)

#Views
@views.route('/')
@views.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')