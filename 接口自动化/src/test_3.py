#!/usr/bin/python
#-*- coding:utf-8 -*-
import pytest
from until.readdate3  import s
import allure
import requests
from until.log import get_logger
log=get_logger(filename='test_3.py')
@pytest.mark.parametrize("x,y",s)
@allure.feature("模块二")
@allure.story("这是一个牛逼的测试用例")
def test_3(x,y):
    url = "http://v.juhe.cn/weather/index"

    #querystring = f"cityname={x}&key={y}"
    querystring = {"cityname":f"{x}","key":f"{y}"}
    log.info("传入参数")
    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.json())
    try:
        assert response.json()["reason"]=="successed!"
    except:
        assert response.json()["reason"]=="错误的请求KEY"
    log.info("进行断言，断言成功")

