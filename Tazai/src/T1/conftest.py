#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
import pytest
from time import sleep
@pytest.fixture(scope="module")
def lianjie():
    d={
        "device": "android",
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "AGYDU18A25001871",
        "appPackage": "com.vy.visvacn",
        "appActivity": ".user.login.ui.SplashActivity ",
        "noReset": "true",
        "unicodeKeyboard": "true",
        "resetkeKboard": "true"

    }
    # d={
    #   "platformName": "Android",
    #   "platformVersion": "5.1.1",
    #   "deviceName": "emulator-5554",
    #   "appPackage": "com.vy.visvacn",
    #   "appActivity": ".user.login.ui.SplashActivity ",
    #   "noReset": "true",
    #   "unicodeKeyboard": "true",
    #    "resetkeKboard": "true"
    # }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    sleep(10)
    return dr
