#!/usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
import  pytest
from time import sleep
@pytest.fixture(scope="module")
def lianjie():
    dr = webdriver.Chrome()
    sleep(5)
    return dr
