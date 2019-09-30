#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys
import json
import threading
from uitls import chunks

class JobThread(threading.Thread):

    def __init__(self,func,args=()):
        super(JobThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

def job(uids, code):
    """获取指定ip对应的地理位置"""
    flag=True
    result = []
    for uid in uids:
        if not flag:
            break
        url='http://statistics.pandadastudio.com/player/giftCode'
        infoUrl = 'http://statistics.pandadastudio.com/player/simpleInfo?uid=203895417'
        giftCodeReq = requests.get(url, params={"uid": uid, "code": code})
        giftCodeRes=giftCodeReq.json()
        # # 417: 礼包不存在 424: 过期
        if giftCodeRes['code'] == 417 or giftCodeRes['code'] == 424:
            print(giftCodeRes['msg'])
            result.append(giftCodeRes['msg'])
            flag = False
            break
        else:
            # 获取基本信息
            infoReq = requests.get(infoUrl, params={"uid": uid})
            infoRes=infoReq.json()
            if infoRes['msg'] == 'success':
                print(uid, giftCodeRes['msg'], infoRes['data']['name'])
                result.append(uid + ' ' + giftCodeRes['msg'] + ' ' + infoRes['data']['name'])
            else:
                print(uid, giftCodeRes['msg'])
                result.append(uid + ' ' + giftCodeRes['msg'])
    return result

# if __name__ == "__main__":
#     threads = []
#     uids=[]
#     code=sys.argv[1]
#     print('兑换码=>' + code)
#     with open('uids.txt', 'r') as f:
#         uids = f.read().splitlines()
#     for _uids in chunks(uids, 5):
#         t = threading.Thread(target=job, args=(_uids, code))
#         threads.append(t)
#         t.start()

#     [thread.join() for thread in threads]

def executeJob(code):
    threads = []
    uids=[]
    print('兑换码=>' + code)
    with open('uids.txt', 'r') as f:
        uids = f.read().splitlines()
    for _uids in chunks(uids, 5):
        t = JobThread(func=job, args=(_uids, code))
        threads.append(t)
        t.start()
    reuslt = []
    for thread in threads:
        thread.join()
        reuslt.append(thread.get_result())
    return json.dumps(reuslt, ensure_ascii=False)
    # [thread.join() for thread in threads]