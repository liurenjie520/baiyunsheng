# -*- coding: utf8 -*-
import json
import os
import requests
def main_handler(event, context):
    URL = 'https://saas.lianyuplus.com/saas20/api/201410011/AptGuest/customer/tenant/listContract'
    params = {
        'customerId': 1241533,
        'localeType': 'zh',
        'withPic': 'true',
        'withPreDeposit': 'true'
    }

    Cookie = os.environ.get('Cookie')
    intebox_sso_tkt = os.environ.get('intebox_sso_tkt')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        'Cookie': Cookie,
        'intebox_sso_tkt': intebox_sso_tkt
    }
    resp = requests.post(URL, params=params,
                         verify=False, headers=headers, timeout=10)
    js = resp.json()
    js = js['data'][0]['preDeposit']
    if float(js) <= 0:
        print('没电费了')
        requests.get(
            "http://wxpusher.zjiecode.com/api/send/message/?appToken=AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e&content=没电费了&uid=UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi")
        requests.get("https://api.day.app/xQvkTS3VuhXsNBP74GVX78/没电费了！")
    else:
        print('还有电费')
    
    
