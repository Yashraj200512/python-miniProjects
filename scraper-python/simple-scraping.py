import requests
from bs4 import BeautifulSoup

def scrape():

    url='https://www.example.com'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    title=soup.select_one('p').text
    print(title)

if __name__=='__main__':
 scrape()    