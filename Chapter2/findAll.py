#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html5lib")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

nameList2 = bsObj.findAll(text = "the prince")
print(len(nameList2))

