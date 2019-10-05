# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:31:43 2019

@author: Yasuyuki
"""
import requests
from bs4 import BeautifulSoup

# make search words list
search_words = ["extract", "word", "English", "tablet", "water", "play", "buoyancy"]

for word in search_words:
    # make url of each search word
    url = "https://ejje.weblio.jp/content/" + word

    # send request to url
    r = requests.get(url)

    # extract texts from web site
    soup = BeautifulSoup(r.content, "html.parser")
    mean_text = soup.find("div", class_="summaryM descriptionWrp").text
    level = soup.find("span", class_="learning-level-content").text

    # print results
    print("--------------------------")
    print("word: ", word)
    print("mean: ", mean_text)
    print("lebel: ", level)
