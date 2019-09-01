#!/usr/bin/python
#-*- coding:utf-8 -*-
import pytest
import requests
d=[1,2,3,4,5]
@pytest.fixture(scope='function', params=d)
def read_data(request):
    return request.param
def test_4(read_data):
    url = "http://zuowen.api.juhe.cn/zuowen/typeList"

    querystring = {"key": "955f1fc9d777cb396780c212fb736501", "id": f"{read_data}"}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        # 'Accept': "*/*",
        # 'Cache-Control': "no-cache",
        # 'Postman-Token': "59eacf2c-ccd3-4693-aeb5-d2a1b63e9d4a,617efea1-b060-4d60-9224-ab007de72e35",
        # 'Host': "zuowen.api.juhe.cn",
        # 'Cookie': "aliyungf_tc=AQAAAObGPS3D3w0AL7k4cwSkI+Y3mRy2",
        # 'Accept-Encoding': "gzip, deflate",
        # 'Connection': "keep-alive",
        # 'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    try:
        assert  "success" in response.text
    except:
        assert "参数错误!" in response.text
