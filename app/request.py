from app import app
import urllib.request,json
from .news import News_Sources,News_Article

# Getting api key
api_key = None

#Getting news base url
news_source_url = None
news_article_url = None

def request_config(app):
    global api_key, news_source_url, news_article_url
    api_key = app.config['NEW_API_KEY']
    news_source_url = app.config["NEWS_SOURCE_URL"]
    news_article_url = app.config['NEWS_ARTICLE_URL']


def get_news_source(category):
    """
    Function that gets the json response to our url request
    """
    get_sources_url =  news_source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            source_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news details

    Returns :
        source_results: A list of news objects
    '''

    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        url = sources_item.get.('url')
        category = sources_item.get('category')
        description = sources_item.get('description')

        sources_object = Sources(id,name,url,category,description)
        sources_results.append(sources_object)

    return sources_results
        
 
def my_news_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url =  news_article_url.format(id,api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
                articles_object = process_articles(articles_results_list)
        
    return articles_object



        
def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of articles objects
    '''
            articles_object = []
            for item in results_list:
                id = item.get('id')
                author = item.get('author')
                title = item.get('title')
                description = item.get('description')
                publishedAt = item.get('publishedAt')
                urlToImage= item.get('urlToImage')
                url = item.get('url')
                
               
                if urlToImage:
                        articles_results = News_Article(id,author,title,description,publishedAt,urlToImage,url)
                        articles_object.append(articles_results)

            return articles_object
            