#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import pytest
@pytest.fixture(scope="module")
def lianjie():
    #url = "http://192.168.10.53:5000/login"
    url1="http://v.juhe.cn"
    return url1
