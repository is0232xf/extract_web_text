# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:31:43 2019

@author: Yasuyuki
"""
import requests
from bs4 import BeautifulSoup
from operator import itemgetter

# make search words list
search_words = ["wa", "ha", "jfoso", "English", "have", "control"]
result_list = []

def search_listed_words(search_words):
    for word in search_words:
        # make url of each search word
        url = "https://ejje.weblio.jp/content/" + word
    
        # send request to url
        r = requests.get(url)
    
        # extract texts from web site
        soup = BeautifulSoup(r.content, "html.parser")
        mean_text = soup.find("div", class_="summaryM descriptionWrp")
        if mean_text is None:
            mean_text = "None"
        else:
            mean_text = mean_text.text
        
        level = (soup.find("span", class_="learning-level-content"))
        if level is None:
            level = 99
        else:
            level = int(level.text)
    
        result_set = (word, mean_text, level)
        result_list.append(result_set)
    return(result_list)

search_listed_words(search_words)
print(result_list)
sorted_list = sorted(result_list, key=itemgetter(2))
print(sorted_list)
