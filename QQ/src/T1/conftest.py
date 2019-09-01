#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
import  pytest
from time import sleep
@pytest.fixture(scope="module")
def lianjie():
    d={
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.tencent.mobileqq",
      "appActivity": ".activity.SplashActivity",
      "noReset": "true"
    }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    sleep(10)
    return dr
