from app import app
import urllib.request,json
from .news import News


api_key = app.config['NEW_API_KEY']


base_url = app.config["NEWS_API_LINK"]

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
                source = item.get('source')
                author = item.get('author')
                title = item.get('title')
                description = item.get('description')
                publishedAt = item.get('publishedAt')
                url = item.get('url')
                poster = item.get('urlToImage')
               
                # if poster:
                news_object = News(source,author,title,description,publishedAt,url,poster)
                news_results.append(news_object)

            return news_results
            