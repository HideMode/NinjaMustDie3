#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys
import threading


def job(uid, flag, code):
    """获取指定ip对应的地理位置"""
    if not flag:
        pass
    url='http://statistics.pandadastudio.com/player/giftCode'
    infoUrl = 'http://statistics.pandadastudio.com/player/simpleInfo?uid=203895417'
    giftCodeReq = requests.get(url, params={"uid": uid, "code": code})
    giftCodeRes=giftCodeReq.json()
    


    infoReq = requests.get(infoUrl, params={"uid": uid})
    infoRes=infoReq.json()
    if infoRes['msg'] == 'success':
        print(uid, giftCodeRes['msg'], infoRes['data']['name'])
    else:
        print(uid, giftCodeRes['msg'])

    # # 417: 礼包不存在 424: 过期
    # if result['code'] == 417 or result['code'] == 424:
    #     print(result['msg'])
    #     flag=False
    #     pass
    # else:
    #     print(uid, result['msg'])




if __name__ == "__main__":
    threads = []
    uids=[]
    flag=True
    code=sys.argv[1]
    print('兑换码=>' + code)
    with open('uids.txt', 'r') as f:
        # while True:
        #     line = file.readline() # 整行读取数据
        #     if not line:
        #         break
        #         pass
        #     print(line)
        #     uids.append(line)
        uids = f.read().splitlines()
    
    for uid in uids:
        t = threading.Thread(target=job, args=(uid, flag, code))
        threads.append(t)
        t.start()

    [thread.join() for thread in threads]