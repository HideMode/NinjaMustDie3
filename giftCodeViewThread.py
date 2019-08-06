#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys
import threading
from uitls import chunks

def job(uids, code):
    """获取指定ip对应的地理位置"""
    flag=True
    for uid in uids:
        # print(threading.current_thread()) 
        if not flag:
            break
        url='http://statistics.pandadastudio.com/player/giftCode'
        infoUrl = 'http://statistics.pandadastudio.com/player/simpleInfo?uid=203895417'
        giftCodeReq = requests.get(url, params={"uid": uid, "code": code})
        giftCodeRes=giftCodeReq.json()
        # # 417: 礼包不存在 424: 过期
        if giftCodeRes['code'] == 417 or giftCodeRes['code'] == 424:
            print(giftCodeRes['msg'])
            flag = False
            break
        else:
            # 获取基本信息
            infoReq = requests.get(infoUrl, params={"uid": uid})
            infoRes=infoReq.json()
            if infoRes['msg'] == 'success':
                print(uid, giftCodeRes['msg'], infoRes['data']['name'])
            else:
                print(uid, giftCodeRes['msg'])

if __name__ == "__main__":
    threads = []
    uids=[]
    code=sys.argv[1]
    print('兑换码=>' + code)
    with open('uids.txt', 'r') as f:
        uids = f.read().splitlines()
    for _uids in chunks(uids, 5):
        t = threading.Thread(target=job, args=(_uids, code))
        threads.append(t)
        t.start()

    [thread.join() for thread in threads]