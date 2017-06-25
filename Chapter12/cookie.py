#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

