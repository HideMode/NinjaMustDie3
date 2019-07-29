#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys

code = sys.argv[1]
print('兑换码=>' + code)
url='http://statistics.pandadastudio.com/player/giftCode'
uids=[]
flag=True
with open('uids.txt', 'r') as file:
    while flag:
        line = file.readline() # 整行读取数据
        if not line:
            break
            pass
        uids.append(line)
        r = requests.get(url, params={"uid": line, "code": code})
        result=r.json()
        # 417: 礼包不存在 424: 过期
        if result['code'] == 417 or result['code'] == 424:
            flag=False
            print(result['msg'])
            break
   