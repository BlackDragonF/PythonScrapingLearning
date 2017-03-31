#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

params = {'username': 'BlackDragon', 'password':'password'}
'''
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(r.cookies.get_dict())
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r.cookies)
print(r.text)
'''

session = requests.Session()
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(s.cookies.get_dict())
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

