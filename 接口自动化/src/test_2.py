#!/usr/bin/python
#-*- coding:utf-8 -*-
import pytest
import requests
from until.readdate1  import s


@pytest.mark.parametrize("x,y",s)
def test_2(x,y):
    url = "http://web.juhe.cn:8080/environment/water/river"

    querystring = f"river={x}&key={y}"

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "70498527-3132-402d-89d9-0b52c30fca88,f633c24f-a4dc-4ccd-81a1-3ff16b2c372b",
        'Host': "web.juhe.cn:8080",
        'Cookie': "JSESSIONID=BCC0488C2279D56835D327A524751856",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # cc=response.json()
    # print(cc)
    # try:
    #     assert cc["resultcode"]=="200"
    # except:
    #     assert cc["resultcode"] == "101"
    print(response.text)
    try:
        assert "200" in response.text
    except:
        assert  "101" in response.text