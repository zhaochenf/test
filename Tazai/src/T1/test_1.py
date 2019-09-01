#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import yaml
from until.ReadData import s
from until.划 import swipe_up
from until.划 import swipe_down
from until.划 import swipe_left
from until.划 import swipe_right
from selenium.common.exceptions import NoSuchElementException
import pytest
from time import sleep
from until.mylog import get_logger
log=get_logger(filename='test_1.py')

with open(file=r"D:\Tazai\element\login.yaml",mode="r",encoding="utf-8") as fb:
    e=yaml.load(fb,Loader=yaml.FullLoader)
"""
#登录测试
def test_1(lianjie):


    lianjie.find_element_by_id(e['shouji']).click()
    sleep(3)
    lianjie.find_element_by_id(e["mmd"]).click()
    sleep(4)
@pytest.mark.parametrize("zh,mm",s)
def test_2(zh,mm,lianjie):
    # lianjie.find_element_by_id(e['shouji']).click()
    # sleep(3)
    # lianjie.find_element_by_id(e["mmd"]).click()
    # sleep(4)
    lianjie.find_element_by_id(e["hama"]).clear()
    lianjie.find_element_by_id(e["hama"]).send_keys(zh)
    lianjie.find_element_by_id(e["mima"]).clear()
    lianjie.find_element_by_id(e["mima"]).send_keys(mm)
    lianjie.find_element_by_id(e["login"]).click()
    try:
        assert lianjie.find_element_by_id(e["dmm"]).text == "忘记密码"
        log.info(f"登录失败，断言成功")
    except NoSuchElementException:
        pass
    try:
        b = lianjie.find_element_by_id(e["dy"]).find_elements_by_class_name(e["dy1"])
        c = b[1].text
        assert c=="圈子"
        log.info(f"登录成功，断言成功")
    except NoSuchElementException :
        pass

"""
#登录tazai
"""
def test_3(lianjie):
    lianjie.find_element_by_id(e['shouji']).click()
    sleep(3)
    lianjie.find_element_by_id(e["mmd"]).click()
    sleep(4)
    lianjie.find_element_by_id(e["hama"]).clear()
    lianjie.find_element_by_id(e["hama"]).send_keys("17792759651")
    lianjie.find_element_by_id(e["mima"]).clear()
    lianjie.find_element_by_id(e["mima"]).send_keys("fei820515")
    lianjie.find_element_by_id(e["login"]).click()
    #lianjie.find_element_by_id(e["tux"]).click()
    sleep(8)
    b=lianjie.find_element_by_id(e["dy"]).find_elements_by_class_name(e["dy1"])
    c=b[1].text
    #print(c)
    # for i in b:
    #    print(i.text)
    assert c=="我趣"
"""
#退出账号
"""
def test_4(lianjie):
    lianjie.find_element_by_id(e["tux"]).click()
    sleep(5)
    swipe_up(lianjie)
    lianjie.find_element_by_id(e["seting"]).click()
    lianjie.find_element_by_id(e["tchu"]).click()
    lianjie.find_element_by_id(e["qding"]).click()
"""
# 验证 分享 我趣 同好之间的滑动
"""
def test_5(lianjie):
    #分享
    swipe_up(lianjie)
    sleep(2)
    swipe_down(lianjie)
    sleep(3)
    #圈子
    swipe_left(lianjie)
    sleep(2)
    swipe_up(lianjie)
    sleep(2)
    #合拍
    swipe_left(lianjie)
    sleep(4)
    swipe_up(lianjie)
    swipe_down(lianjie)
    #CIQ
    lianjie.find_element_by_id(e["xid"]).click()
    sleep(2)
    assert lianjie.find_element_by_id(e["ciq"]).text=="CIQ"
    log.info(f"进入CIQ，断言成功")
    swipe_up(lianjie)
    sleep(2)
    lianjie.find_element_by_id(e["cfi"]).click()

"""

"""
#加号里面的提问模块
def test_6(lianjie):
    lianjie.find_element_by_id(e["jiahao"]).click()
    lianjie.find_element_by_id(e["twen"]).click()
    sleep(3)
    lianjie.find_element_by_id(e["wenn"]).click()
    sleep(3)
    lianjie.find_element_by_id(e["wenn"]).send_keys("python的作用")
    lianjie.find_element_by_id(e["fab"]).click()
    b = lianjie.find_element_by_id(e["dy"]).find_elements_by_class_name(e["dy1"])
    c = b[0].text
    assert c == "分享"
"""
"""
#铃铛图像里的
def test_7(lianjie):
    lianjie.find_element_by_id(e["lingt"]).click()
    hr=lianjie.find_element_by_id(e["xxi"]).text
   # print(hr)
    assert hr =="消息"

    lianjie.find_element_by_id(e["pingl"]).click()  #评论
    lianjie.find_element_by_id(e["fanh"]).click()
    lianjie.find_element_by_id(e["huid"]).click()  #回答
    lianjie.find_element_by_id(e["fanh"]).click()
    lianjie.find_element_by_id(e["GM"]).click()     #GMM
    lianjie.find_element_by_id(e["fanh"]).click()
    lianjie.find_element_by_id(e["bscang"]).click()    #被收藏
    lianjie.find_element_by_id(e["fanh"]).click()
    lianjie.find_element_by_id(e["ggao"]).click()      #官方公告
    swipe_up(lianjie)
    sleep(3)
    lianjie.find_element_by_id(e["fanh"]).click()
"""
"""
def test_8(lianjie):
    lianjie.find_element_by_id(e["scang"]).click()
    h1=lianjie.find_element_by_id(e["wsc"]).text
    assert h1=="我的收藏"
    log.info(f"跳转我的收藏，断言成功")
    sleep(2)
    lianjie.find_element_by_id(e["scping"]).click()
    swipe_up(lianjie)
    sleep(3)
    log.info(f"点击评论，进行滑动")
    lianjie.find_element_by_id(e["zhuanf"]).click()
    sleep(2)
    lianjie.find_element_by_id(e["zhuanqv"]).click()
    lianjie.find_element_by_id(e["fanh"]).click()
    h1 = lianjie.find_element_by_id(e["wsc"]).text
    assert h1 == "我的收藏"
    log.info(f"返回我的收藏主面，断言成功")
"""
"""
#更换图像
def  test_9(lianjie):
    lianjie.find_element_by_id(e["tux"]).click()
    lianjie.find_element_by_id(e["bianj"]).click()
    sleep(5)
    lianjie.find_element_by_id(e["xtux"]).click()
    sleep(2)
    lianjie.find_element_by_id(e["xtp"]).click()
    sleep(3)
    lianjie.find_elements_by_id(e["xname"])[2].click()
    lianjie.find_element_by_id(e["wcheng"]).click()
    lianjie.find_element_by_id(e["duih"]).click()
    sleep(15)
    lianjie.find_element_by_id(e["baoc"]).click()
    ah=lianjie.find_element_by_id(e["bianj"]).text
    assert ah=="编辑"
    log.info(f"更换图像完成，断言成功")
"""
"""
#更改个人信息
def test_10(lianjie):
    lianjie.find_element_by_id(e["tux"]).click()
    lianjie.find_element_by_id(e["bianj"]).click()
    lianjie.find_element_by_id(e["xbi"]).click()
    lianjie.find_element_by_id(e["nnb"]).find_elements_by_class_name(e["nni"])[1].click() #男0 女 1 取消2
    log.info(f"更改性别")
    lianjie.find_element_by_id(e["shd"]).click()
    lianjie.find_element_by_id(e["niaid"]).click()
    swipe_up(lianjie)
    lianjie.find_element_by_id(e["qid"]).click()
    log.info(f"更改生日")
    sleep(2)
    lianjie.find_element_by_id(e["gzid"]).clear()
    lianjie.find_element_by_id(e["gzid"]).send_keys("运维工程师")
    log.info(f"更改工作")
    sleep(2)
    lianjie.find_element_by_id(e["gxid"]).click()
    lianjie.find_element_by_id(e["nqid"]).send_keys("走自己路，让别人去说")
    lianjie.find_element_by_id(e["wcid"]).click()
    log.info(f"更改签名")
    lianjie.find_element_by_id(e["baoc"]).click()
    sleep(2)
    assert  lianjie.find_element_by_id(e["dyid"]).text=="我的兴趣图谱"
    log.info(f"修改个人资料成功")
"""
















