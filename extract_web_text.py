# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:31:43 2019

@author: Yasuyuki
"""
import requests
from bs4 import BeautifulSoup

url = "https://ejje.weblio.jp/content/extract"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
text = soup.find("div", class_="summaryM descriptionWrp").text
#text = text.replace("\n", "")
print(text)
