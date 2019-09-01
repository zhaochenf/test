#!/usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from until.mylog import get_logger
import pytest
log=get_logger(filename='test_1.py')
def test_1(lianjie):
    lianjie.get('https://www.visvachina.com/#/square')
    lianjie.maximize_window()
    sleep(2)
    log.info(f"登录Ta在网址")
    a=lianjie.find_element_by_xpath('//*[@id="button-group"]/div[1]').text
    assert a=="密码登录"
    log.info(f"断言进入Tazai界面成功")

def test_2(lianjie):
    lianjie.find_element_by_xpath('//*[@id="button-group"]/div[1]').click()  # 点击密码登录
    sleep(2)
    lianjie.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/input").send_keys("17792759651")  # 账号
    sleep(2)
    lianjie.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/input").send_keys("fei820515")  # 密码
    sleep(1)
    lianjie.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]").click()  # 确认登录
    sleep(5)
    log.info(f'密码登录软件')
    b=lianjie.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[2]').text
    assert b=="关于我们"
    log.info(f"断言登录成功")
def test_3(lianjie):
    lianjie.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[2]').click()  # 关于我们
    for i in range(0, 400, 75):
        js = f"var q=document.documentElement.scrollTop={i}"
        lianjie.execute_script(js)
        sleep(2)
    log.info(f"点击我们进行滑动")
def test_4(lianjie):
    lianjie.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[3]').click()  # 加入我们
    for i in range(0, 700, 127):
        js = f"var q=document.documentElement.scrollTop={i}"
        lianjie.execute_script(js)
        sleep(2)
    log.info(f"点击加入我们进行滑动查看")
def test_5(lianjie):
    lianjie.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[4]').click()
    for i in range(0, 1000, 120):
        js = f"var q=document.documentElement.scrollTop={i}"
        lianjie.execute_script(js)
        sleep(2)
    log.info(f"点击关于公司进行滑动")
def test_6(lianjie):
    lianjie.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]').click()
    sleep(3)
    log.info(f"点击首页")
    lianjie.find_element_by_class_name('add-component').click()  # 点击加号
    sleep(2)

    se = lianjie.find_elements_by_class_name('el-dropdown-menu__item')
    # for i in se:
    #     print(i.text)
    #     sleep(2)
    se[1].click()  # 提问
    sleep(3)
    lianjie.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/input[1]').send_keys('python')
    sleep(2)
    log.info(f"编辑主题")
    lianjie.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/textarea').send_keys('高级编程语言')
    sleep(3)
    log.info(f"编辑内容")
    lianjie.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[6]/div[2]').click()
    sleep(4)
    AD=lianjie.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[2]').text
    assert AD=="发布成功"
    log.info(f"断言提问发布成功")
    sleep(2)
    lianjie.find_element_by_xpath('/html/body/div[3]/div/div[1]/button').click()






