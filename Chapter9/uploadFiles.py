#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

files = {'uploadFile': open('./test.jpg', 'rb')}
r = requests.post("http://www.pythonscraping.com/files/processing2.php", files = files)

print(r.text)
