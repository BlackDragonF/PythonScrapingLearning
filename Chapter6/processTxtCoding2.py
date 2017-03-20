#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html5lib")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, 'UTF-8')
content = content.decode('UTF-8')
print(content)
