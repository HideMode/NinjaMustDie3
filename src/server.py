#!/usr/bin/python
# -*- coding: UTF-8 -*-

import flask
from flask import request
import giftCodeViewThread
server = flask.Flask(__name__)


@server.route('/', methods=['get'])
def main():
    try:
        code = request.args.get('code')
        result = giftCodeViewThread.executeJob(code)
        return result
    except Exception as err:
        print(err)
        return "失败"

server.run(port=8090,debug=True, host='0.0.0.0')