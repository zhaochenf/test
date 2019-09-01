#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import yaml
import pytest
from until.ReadData import s
from selenium.common.exceptions import NoSuchElementException
from until.mylog import get_logger
log=get_logger(filename='test_2.py')


with open(file=r"D:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
    e=yaml.load(fb,Loader=yaml.FullLoader)
@pytest.mark.parametrize("zh,mm",s)
def test_3(zh,mm,lianjie):
    #先清除之前输入的数据
    lianjie.find_element_by_accessibility_id(e["hao"]).clear()
    sleep(2)
    #在向入框内输入账号
    lianjie.find_element_by_accessibility_id(e["hao"]).send_keys(zh)
    log.info(f"账号是{zh}")
    sleep(2)
    #输入密码
    lianjie.find_element_by_id(e["mima"]).clear()
    sleep(2)
    lianjie.find_element_by_id(e["mima"]).send_keys(mm)
    sleep(2)
    log.info(f"密码是{mm}")

    #点击登录
    lianjie.find_element_by_id(e["login"]).click()
    sleep(8)
    log.info(f"点击登录")
    # if lianjie.find_element_by_accessibility_id(e["xinyonghu"]).text=="用户注册":
    #     assert lianjie.find_element_by_accessibility_id(e["xinyonghu"]).text=="用户注册"
    # elif lianjie.find_element_by_id(e["quer"]).text=="确定":
    #     #lianjie.find_element_by_id(e["quer"]).click()
    #     assert lianjie.find_element_by_id(e["quer"]).text=="确定"
    #     lianjie.find_element_by_id(e["quer"]).click()
    # elif lianjie.find_element_by_id(e["ziduan"]).text=="消息":
        # assert lianjie.find_element_by_id(e["ziduan"]).text=="消息"
    # try:
    #     assert lianjie.find_element_by_accessibility_id(e["xinyonghu"]).text == "用户注册"
    #
    # except NoSuchElementException:
    #     assert lianjie.find_element_by_id(e["quer"]).text == "确定"
    #     lianjie.find_element_by_id(e["quer"]).click()
    #
    # except NoSuchElementException:
    #     assert lianjie.find_element_by_id(e["ziduan"]).text=="消息"

    try:
        assert lianjie.find_element_by_accessibility_id(e["xinyonghu"]).text == "用户注册"
        log.info(f"登录失败，断言成功")
    except NoSuchElementException:
        pass
    try:
        assert lianjie.find_element_by_id(e["quer"]).text == "确定"
        log.info(f"登录失败，断言成功")
        log.info(f"登录失败，单击确定")
        lianjie.find_element_by_id(e["quer"]).click()
    except NoSuchElementException:
        pass
    try:
        assert lianjie.find_element_by_id(e["ziduan"]).text == "消息"
        log.info(f"登录成功，断言成功")
    except NoSuchElementException :
        pass








