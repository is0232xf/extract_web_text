# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:31:43 2019

@author: Yasuyuki
"""
import requests
from bs4 import BeautifulSoup

word = "extract"
url = "https://ejje.weblio.jp/content/" + word

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
mean_text = soup.find("div", class_="summaryM descriptionWrp").text
level = soup.find("span", class_="learning-level-content").text
#text = text.replace("\n", "")
print("mean: ", mean_text)
print("lebel: ", level)
