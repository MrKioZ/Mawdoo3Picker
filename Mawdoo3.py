from requests import get
from random import choice
from bs4 import BeautifulSoup
from random import choice
from random import shuffle

class mawdoo():

    def __init__(self):
        self.url = 'https://mawdoo3.com/'
        self.website = get(self.url).content
        self.content = BeautifulSoup(self.website, 'html.parser')
        self.categories = self.content.find_all("div", {"class":"category"})
        self.scrapped_categories = []
        self.scrapped_articles = []

    def GetArticle(self):

        for category in self.categories:
            for category_item in category.find_all('li'):
                if not category_item.find('a')['href'].startswith('http'):
                    self.scrapped_categories.append(category_item.find('a')['href'])
        shuffle(self.scrapped_categories)
        self.Choosen_Category = self.url + choice(self.scrapped_categories)

        self.website = get(self.Choosen_Category).content
        self.soup = BeautifulSoup(self.website, 'html.parser')
        self.articles = self.soup.find("ul", {'class': "row categories-list"}).find_all('a')
        self.scrapped_articles = []

        for article in self.articles:
            if not article['href'].startswith("http"):
                self.scrapped_articles.append(article['href'])

        shuffle(self.scrapped_articles)
        self.OpenArticle(self.url+choice(self.scrapped_articles))

    def OpenArticle(self, url):
        """Opens a new tab"""
        """It uses a the default"""
        import webbrowser
        webbrowser.open_new(url)


if __name__ == '__main__':
    mawdoo().GetArticle()
