import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,jsonify
import random

app=Flask(__name__)


    
def randomFact():
    url='https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'
    headers = {'User-Agent': 'Mozilla/5.0'} 
    response=requests.get(url,headers=headers)
    articles=BeautifulSoup(response.text,'html.parser')
    
    List=articles.select('.wikitable tr td')
    
    factList=[]
    for j in range(len(List)-1):
        if j%2==0:
            title=List[j].text.strip()
            info=List[j+1].text.strip()

            FactsDict={'title':title, 'info':info}

            factList.append(FactsDict)
        
    return factList

  
@app.route('/')
def home():
   return render_template('randomFactsFrontend.html')

@app.route('/get-fact')
def get_fact_api():
    all_facts=randomFact()

    chosen_fact=random.choice(all_facts)

    return jsonify(chosen_fact)

if __name__=='__main__':
    app.run(debug=True)

 