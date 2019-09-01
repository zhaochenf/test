#!/usr/bin/python
#-*- coding:utf-8 -*-
import pytest
import requests
from until.readdate import s
@pytest.mark.parametrize("zh,mm",s)
def test_1(lianjie,zh,mm):
    #querystring =f"username={zh},password={mm}"
    #url = "http://192.168.10.53:5000/login"
    payload = f"username={zh}&password={mm}"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "b2c36e6e-95b6-49c6-8c6b-c7d289500138,77d2cbf8-759b-43b0-a414-3bf76b7c58e3",
        'Host': "127.0.0.1:5000",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "30",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    #response=requests.request("get",lianjie,params=payload,headers=headers)
    response = requests.request("POST", lianjie, data=payload,headers=headers)
    #print(response.status_code)  打印状态码

    print(response.text)
    try:
        assert  'welcome' in response.text
    except:
        assert 'login' in response.text
