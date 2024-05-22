class Article:

    all = []
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author

        self.magazine = magazine
        self.title = title
        Article.add_new_article(self)
    
    #@property 
    #def author(self):
    #    return self._author

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title must be of type str")
        if len(new_title) < 5 or len(new_title) > 50:
            raise ValueError("Title must be between 5 and 50 characters inclusive")
        self._title = new_title

    @classmethod
    def add_new_article(cls, new_article):
        cls.all.append(new_article)
        cls.all_articles.append(new_article)


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))




class Magazine:

    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all_magazines.append(self) # add the magazine instance to all_magazines list on instantiation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type str")
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be of type str")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = new_category
    
    def articles(self):
        return self._articles

    def contributors(self):
        authors = [article.author for article in self._articles]
        return list(set(authors))
    
    def article_titles(self):
        return [article.title for article in self._articles] 

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        unique_authors = set(authors)
        return [author for author in unique_authors if authors.count(author) > 2]
    
    def add_article(self, author, title):
        article = Article(author, self, title) # create article instantce
        self._articles.append(article) #  add new article to all list
        return article
    
    @classmethod
    def top_publisher(cls):
        if not cls.all.magazines:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))
    