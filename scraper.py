#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json

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
        author = opinion.select('div.reviewer-name-line').pop().text.strip()
        try:
            recommendation = opinion.select('div.product-review-summary>em').pop().text
        except IndexError:
            recommendation=None
        stars = opinion.select('span.review-score-count').pop().text
        content = opinion.select('p.product-review-body').pop().text
        try:
            cons = opinion.select('div.cons-cell > ul').pop().text
        except IndexError:
            cons=None
        try:
            pros = opinion.select('div.pros-cell > ul').pop().text
        except IndexError:
            pros= None
        useful = opinion.select('button.vote-yes > span').pop().text
        useless = opinion.select('button.vote-no > span').pop().text
        opinion_date = opinion.select('span.review-time > time:nth-child(1)').pop()['datetime']
        try:
            purchase_date = opinion.select('span.review-time > time:nth-child(1)').pop()['datetime']
        except IndexError:
            purchase_date=None

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

