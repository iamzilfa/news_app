from flask import render_template
from app import app
from .request import my_news_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    myNewsdata = my_news_article()
    print(myNewsdata)
    return render_template('index.html', data = myNewsdata)