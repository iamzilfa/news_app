class Config:

    NEWS_SOURCE_URL = 'https://newsapi.org/v2/sources?category=general&apiKey={}'
    NEWS_ARTICLE-URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    

class ProdConfig:
    pass
    
  
class DevConfig:

    DEBUG = True
    