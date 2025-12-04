import requests
from bs4 import BeautifulSoup

def randomFact():
    url='https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'
    response=requests.get(url)
    articles=BeautifulSoup(response,'html.parser')
    