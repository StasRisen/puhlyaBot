# -*- coding: utf-8 -*-
import requests
import sys
url = 'http://wttr.in'

res = requests.get(url)

temp = res.content.decode('utf-8')



#str = two[90:127]
print(temp[:30])
print(temp[158:160] + '..' +temp[177:179] + '°')