# -*- coding: utf-8 -*-
# @Time    : 2020-07-03 17:53
# @Author  : wyq
# @File    : wyqtest2.py
# @Software: PyCharm

import requests, json
from utlis.error_code import RET


def aa(request):
    request_data = request.body
    request_dict = json.loads(request_data.decode('utf-8'))

    debug = request_dict.get('debug')
    env = request_dict.get('env')
    datate = request_dict.get('jstr')
    try:
        data = json.loads(datate)
    except Exception as e:
        errmsg = "入参出现异常,请自行检查数据 %s" % (e)
        reqdata = {'erron': RET.PARAMERR, 'errmsg': errmsg}
        return reqdata
    api = env + data['api']
    head = data['head']
    if debug == 'true':
        data['body']['debug'] = 1
    body = data['body']
    if head.get('version', None):
        version = head.get('version', None)
    else:
        version = head.get('Version', None)
    #   调用加密接口，请求加密
    url = "http://10.160.84.207:8206/husky/system/aes"
    clienttype = head['ClientType']
    inputreq = (json.dumps(body))
    data1 = {
        "type": "0",
        "version": version,
        "clienttype": clienttype,
        "key": "",
        "input": inputreq
    }
    re = requests.post(url, data={'req': json.dumps(data1)})
    redata = re.text.strip()
    data2 = {"req": redata}
    redata = requests.post(url=api, headers=head, data=data2)
    debugInfo = redata.json().get('debugInfo', None)
    oldreq = redata.text
    if debugInfo:
        goods_par = debugInfo.split('misReqEnd')[0].split('misReq:')[1].split('misReq')[0]
        goods_req = debugInfo.split('misResp:')[1].split('misRespEnd')[0]
        reqdata = {'erron': RET.OK, 'datate': datate, 'goods_par': goods_par, 'goods_req': goods_req, 'oldreq': oldreq}
        return reqdata
    else:
        reqdata = {'erron': RET.OK, 'datate': datate, 'oldreq': oldreq}
        return reqdata