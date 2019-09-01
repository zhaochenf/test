#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
d={"device": "android",
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "AGYDU18A25001871",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true"
   }
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
sleep(3)
qwe=dr.find_element_by_id("com.tencent.mobileqq:id/recent_chat_list").find_element_by_class_name("android.widget.LinearLayout").click()
dr.find_element_by_id("com.tencent.mobileqq:id/input").send_keys('1147426361')
dr.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click() #点击发送消息
m=dr.find_element_by_id("com.tencent.mobileqq:id/rlCommenTitle").find_elements_by_id("com.tencent.mobileqq:id/name")
m[3].click()    #根据索引   返回
# sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/conversation_head").click()  #点击图像
# sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/settings").click()  #设置
# sleep(3)
# dr.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()  #账号管理
# sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()  #退出当前账号
# dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()   #点击确定
#
