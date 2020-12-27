# -*- coding: utf-8 -*-
import requests
import os
import sys

url = 'http://wttr.in'

res = requests.get(url)

temp = res.content.decode('utf-8')

temp = temp.split('\n')


print(len(temp))
for i in range(0, len(temp) - 1):
    if (temp[i].rfind('°C') != -1):
        print(temp[i])
        print(temp[i].find('°C'))
        print(temp[i][80])
        sys.exit()
