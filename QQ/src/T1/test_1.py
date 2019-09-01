#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import yaml
import pytest
with open(file=r"D:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
    e=yaml.load(fb,Loader=yaml.FullLoader)
#    # print(e) #显示字典
# d={
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.tencent.mobileqq",
#   "appActivity": ".activity.SplashActivity",
#   "noReset": "true"
# }
# #建立连接并开启QQ程序
# dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
# #等待程序启动
# sleep(10)
# #执行退出账号的操作
# dr.find_element_by_xpath(e['tou']).click()
# sleep(1)
# dr.find_element_by_id(e['setting']).click()
# sleep(1)
# dr.find_element_by_id(e['zhanghao']).click()
# sleep(1)
# dr.find_element_by_id(e['tuihao']).click()
# sleep(1)
# dr.find_element_by_id(e['tuichu']).click()
# sleep(1)
# # dr.find_element_by_id(e['qvxiao']).click()
# # sleep(1)
#
# b=dr.find_element_by_accessibility_id(e['xinyonghu']).text
# print(b)
# dr.quit()

"""
def test_2(lianjie):
    #lian==lianjie
    # 执行退出账号的操作
    sleep(10)
    lianjie.find_element_by_xpath(e['tou']).click()
    sleep(1)
    lianjie.find_element_by_id(e['setting']).click()
    sleep(1)
    lianjie.find_element_by_id(e['zhanghao']).click()
    sleep(1)
    lianjie.find_element_by_id(e['tuihao']).click()
    sleep(1)
    lianjie.find_element_by_id(e['tuichu']).click()
    sleep(1)
    b = lianjie.find_element_by_accessibility_id(e['xinyonghu']).text
    print(b)
    lianjie.quit()
    assert b=="用户注册"
"""
def test_3(lianjie):
    #先清除之前输入的数据
    lianjie.find_element_by_accessibility_id(e["hao"]).clear()
    #在向输入框内输入账号
    lianjie.find_element_by_accessibility_id(e["hao"]).send_keys("1147426361")
    #输入密码
    lianjie.find_element_by_id(e["mima"]).clear()
    lianjie.find_element_by_id(e["mima"]).send_keys("Fei820515")


    #点击登录
    lianjie.find_element_by_id(e["login"]).click()



