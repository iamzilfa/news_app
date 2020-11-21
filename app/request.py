from app import app
import urllib.request,json
from .news import News
from .sources import Source

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the movie base url
base_url = app.config["NEWS_API_LINK"]

bases_url = app.config['SOURCES_API_LINK']


def my_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = bases_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = []

        if get_sources_response['source']:
            source_results_list = get_news_response['sources']
            # news_results = process_results(movie_results_list)

            for item in source_results_list:  
                category = item.get('category')
                name = item.get('name')
                description = item.get('description')
                url = item.get('url')
                # if poster:
                sources_object = Source(category,name,description,url)
                source_results.append(source_object)

            return source_results

def my_news():
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
                urlToImage = item.get('urlToImage')
                title = item.get('title')
                description = item.get('description')
                author = item.get('author')
                publishedAt = item.get('publishedAt')
                url = item.get('url')
                # if poster:
                news_object = News(urlToImage,title,description,author,publishedAt,url)
                news_results.append(news_object)

            return news_results

