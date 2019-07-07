from requests import get
from random import choice
from bs4 import BeautifulSoup
from random import choice
from random import shuffle
import os


url = 'https://mawdoo3.com/'
website = get(url)
website = website.content
soup = BeautifulSoup(website, 'html.parser')


#Picks a random category
scrapped_categories = []
categories = soup.find_all("div", {"class":"category"})
for category in categories:
    for category_item in category.find_all('li'):
        if not category_item.find('a')['href'].startswith('http'):
            scrapped_categories.append(category_item.find('a')['href'])

shuffle(scrapped_categories)
Choosen_Category = url+choice(scrapped_categories)

#Picks a ranadom Article from the Category
website = get(Choosen_Category)
website = website.content
soup = BeautifulSoup(website, 'html.parser')
articles = soup.find("ul", {'class': "row categories-list"})
articles = articles.find_all('a')
scrapped_articles = []

for article in articles:
    if not article['href'].startswith("http"):
            scrapped_articles.append(article['href'])

shuffle(scrapped_articles)
Choosen_Article = url+choice(scrapped_articles)

#Shows the Choosen Article to the user by opening Firefox
os.chdir("C:\Program Files\Mozilla Firefox")
os.system('firefox.exe '+Choosen_Article)
