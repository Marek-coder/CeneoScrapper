#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json
import pandas
#funkcja do ekstrakcji skladowych
def extract_feature(opinion,selector,atribute=None):
    try:
        if atribute:
            return opinion.select(selector).pop()[atribute].strip()
        else:
            return opinion.select(selector).pop().text.strip()
    except IndexError:
        return None
#pobranie kodu pojedynczej strony z opinia
url_prefix ='https://www.ceneo.pl'
url_postfix ='/85910996#tab=reviews_scroll'
url=url_prefix+url_postfix


#wodbycie z kodu strony fragmentow odpowiadajacych opiniom konsumentow
all_opinions=[]

while url:
    #dla wszystkich opinii wydobycie jej skladowych
    
    response =requests.get(url)
    page_dom =BeautifulSoup(response.text,'html.parser')
    opinions = page_dom.select('li.js_product-review')

    for opinion in opinions:
        opinion_id=opinion["data-entry-id"]
        author =extract_feature(opinion,('div.reviewer-name-line'))
        
        recommendation= extract_feature(opinion,('div.product-review-summary>em'))
        
        stars =extract_feature(opinion,('span.review-score-count'))
        content = extract_feature(opinion,('p.product-review-body'))
        
        cons = extract_feature(opinion,('div.cons-cell > ul'))
       
        
        pros = extract_feature(opinion,('div.pros-cell > ul'))
       
        useful = extract_feature(opinion,('button.vote-yes > span'))
        useless = extract_feature(opinion,('button.vote-no > span'))
        opinion_date = extract_feature(opinion,('span.review-time > time:nth-child(1)'),atribute='datetime')
       
        purchase_date = extract_feature(opinion,('span.review-time > time:nth-child(1)'),atribute='datetime')
    

        features={
            "opinion_id":opinion_id,
            "author":author,
            "recommendation":recommendation,
            "stars":stars,
            "content":content,
            "cons": cons,
            "pros": pros,
            "useful":useful,
            "useless":useless,
            "opinion_date":opinion_date,
            "purchase_date":purchase_date
        }
        all_opinions.append(features)

   
    try:
        url= url_prefix+page_dom.select('a.pagination__next').pop()['href']
    except IndexError:
        url=None
    with open('opinions.json','w',encoding='UTF-8')as fp:
        json.dump(all_opinions,fp,indent=4,ensure_ascii=False)
        print(len(all_opinions))
        print(url)

