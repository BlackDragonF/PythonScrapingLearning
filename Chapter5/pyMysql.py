#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/run/mysqld/mysqld.sock', user='root', passwd=None, db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()

