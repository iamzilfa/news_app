from flask import render_template
from app import app
from .request import my_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    myNewsdata = my_news()
    return render_template('index.html',)