class News_Sources:

    def __init__(self,id,name,url,category,description):
        self.news_id = id
        self.news_name = name
        self.news_url = url
        self.news_category = category
        self.news_description = description


class News_Article:

    def __init__(self,id,author,title,description,publishedAt,urlToImage,url,):

        self.new_id = id
        self.news_author = author
        self.news_title = title
        self.news_description = description
        self.news_publishedAt = publishedAt
        self.news_urlToImage = urlToImage
        self.news_url = url