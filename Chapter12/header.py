#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = "https://www.whatismybrowser.com/"
req = session.get(url, headers = headers)
bsObj = BeautifulSoup(req.text, "html5lib")
print(bsObj.find("a",{"title":"Your User Agent"}).get_text())

