from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news_source,get_news_article

# Views
@app.route('/')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    general = get_news_source('general')
    entertainment = get_news_source('entertainment')
    business = get_news_source('business')
    health = get_news_source('health')
    sports - get_news_source('sports')
    science = get_news_source('science')
    technology = get_news_source('technology')

    title ='Exclusive News Headlines'

    return render_template('source.html',general = general, entertainment = entertainment, business = business, health = health, sports = sports, science = science, technology = technology )

@app.route('/news/<id>')
def articles(id):
    '''
    view articles
    '''

    articles = get_news_article(id)
    title = 'Articles'

    return render_template('articles.html', articles = articles, title = title)
