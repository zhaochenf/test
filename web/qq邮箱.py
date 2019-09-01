#!/usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

dr=webdriver.Chrome()
dr.get("https://mail.qq.com/cgi-bin/loginpage")
sleep(2)
dr.switch_to.frame("login_frame")
sleep(2)
dr.find_element_by_id("switcher_plogin").click()
sleep(1)
dr.find_element_by_id("u").clear()
dr.find_element_by_id("u").send_keys("1147426361")
sleep(1)
dr.find_element_by_id("p").clear()
dr.find_element_by_id("p").send_keys("Fei820515")
sleep(2)
dr.find_element_by_id("login_button").click()
sleep(2)
dr.find_element_by_id("composebtn").click()  #点击写信
sleep(1)
dr.switch_to.frame("mainFrame")

sleep(2)
dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys("Z199405156336@163.com") #s收件人
dr.find_element_by_xpath('//*[@id="subject"]').send_keys("python") #主题
# dr.switch_to.default_content()
# dr.switch_to.frame("mainFrame")
# Body_frame=dr.find_element_by_class_name("qmEditorIfrmEditArea")
dr.switch_to.frame(0)
dr.find_element_by_xpath('/html/body').send_keys("I LOVE Python")
sleep(3)
dr.switch_to.parent_frame()
dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
