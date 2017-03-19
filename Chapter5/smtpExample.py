#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "obsidian@zhihaochen.com"
msg['To'] = "574712047@qq.com"

s = smtplib.SMTP('localhost')
s.seng_message(msg)
s.quit()

