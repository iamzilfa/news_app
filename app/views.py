from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources,get_articles
from .models import sources,articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business = get_sources('business')
    general = get_sources('general')
    technology = get_sources('technology')
    health = get_sources('health')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')
    science = get_sources('science')


    title = 'Home - Welcome to The best News App'
    return render_template('index.html', title = title,business = business,general = general,technology = technology,health = health,entertainment = entertainment,sports = sports,science = science)




@app.route('/sources/<id>')
def articles(id):
    '''
    View article page function that returns the movie details page and its data
    '''
    articles = get_articles(id)
    title = f'You are viewing {id}'
    return render_template('article.html',title = title,articles = articles)

