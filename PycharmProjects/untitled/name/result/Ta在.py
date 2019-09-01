#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
d={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.vy.visvacn",
  "appActivity": ".user.login.ui.SplashActivity ",
  "noReset": "true"
}
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
sleep(7)
dr.find_element_by_id("com.vy.visvacn:id/rl_phone").click()   #点击手机号登录
dr.find_element_by_id("com.vy.visvacn:id/txt_login_bypassword").click() #点击密码登录
dr.find_element_by_id("com.vy.visvacn:id/et_phone").send_keys("17792759651")  #点击并输手机号
dr.find_element_by_id("com.vy.visvacn:id/et_passwrd").send_keys("fei820515")  #点击并输密码
dr.find_element_by_id("com.vy.visvacn:id/tv_done").click()   #点击登录
dr.find_element_by_id("com.vy.visvacn:id/v3").click()  #点击人像
