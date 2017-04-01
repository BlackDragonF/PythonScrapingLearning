#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# service args which might be useful: --ignore-ssl-errors=true --ssl-protocol=any
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
#driver.set_window_size(800, 600)
#driver.maximize_window()
driver.get("http://www.pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(1)
print(driver.find_element_by_id('content').text)
driver.close()

