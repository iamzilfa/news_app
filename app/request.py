from app import app
import urllib.request,json
from .news import News_Sources,News_Article

# Getting api key
api_key = None

#Getting news base url
news_source_url = None
news_article_url = None

def request-config(app):
    global api_key, news_source_url, news_article_url
    api_key = app.config['NEW_API_KEY']
    news_source_url = app.config["NEWS_SOURCE_URL"]
    news_article_url = app.config['NEWS_ARTICLE_URL']


def my_news_source():

      
def my_news_article():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            # news_results = process_results(movie_results_list)
            
            for item in news_results_list:
                id = item.get('id')
                author = item.get('author')
                title = item.get('title')
                description = item.get('description')
                publishedAt = item.get('publishedAt')
                urlToImage= item.get('urlToImage')
                url = item.get('url')
                
               
                # if poster:
                news_object = News_Article(id,author,title,description,publishedAt,urlToImage,url)
                news_results.append(news_object)

            return news_results
            