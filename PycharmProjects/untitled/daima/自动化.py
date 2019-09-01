#!/usr/bin/python
#-*- coding:utf-8 -*-
#自动访问网页  给python放一个执行文件chromedriver
# import  time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.maximize_window()
# time.sleep(10)
# #driver.get("https://www.baidu.com/")
# driver.get("http://127.0.0.1")
# #driver.quit()


from selenium import webdriver
import time

"""
def login():
    dr = webdriver.Chrome()
    #打开登陆163邮箱的网页
    dr.get('https://mail.163.com/')
    #将浏览器窗口最大化
    dr.maximize_window()
    #休息五分钟等待网页加载完毕
    time.sleep(5)
    #找到邮箱账号登录框对应的iframe

    #dr.switch_to.frame('x-URS-iframe')
    #dr.switch_to.frame("switchAccountLogin")
    #dr.switch_to.frame(dr.find_element_by_xpath('//iframe[@scrolling="no"]'))
    #dr.switch_to.frame(dr.find_element_by_xpath('// *[ @ id = "switchAccountLogin"]'))
    dr.find_element_by_id("switchAccountLogin").click()
    #找到邮箱账号输入框
    qwe = dr.find_element_by_name('email')
    #将自己的邮箱地址输入到邮箱账号框中
    qwe.send_keys('Z199405156336')
    #找到密码输入框
    password = dr.find_element_by_name('password')
    #输入自己的邮箱密码
    password.send_keys('Zhao820515')
    #找到登陆按钮
    login_btn = dr.find_element_by_id('dologin')
    #点击登陆按钮
    login_btn.click()
    #等待10秒看是否登陆成功
    time.sleep(10)

if __name__ == '__main__':
    login()
"""
"""
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://mail.163.com"
# 登录163邮箱网址
driver.get(url)
# 窗体最大化
driver.maximize_window()
# 打印html源代码
# print(driver.page_source)
# 等待3s加载
time.sleep(3)
# 点击选择密码登录（默认是二维码扫描）
#driver.find_element_by_id("switchAccountLogin").click()
# 找到登录框对应的iframe
iframe = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
# 切换到登录的iframe表单，这是网易邮箱通用的一个框架
# driver.switch_to_frame("x-URS-iframe")  # 不可用，因为该名称不是固定的了
# driver.switch_to_frame(iframe)  #貌似警告说要被弃用
driver.switch_to.frame(iframe)
# 找到邮箱账号输入框
email_input = driver.find_element_by_name("email")
# 清除输入框
#email_input.clear()
# 输入我的账号
email_input.send_keys("Z199405156336@163.com")  # @之前的
# 找到密码输入框
password_input = driver.find_element_by_name("password")
# 输入密码
password_input.send_keys("Zhao820515")
# 两种登录方式
# 1.回车登录
password_input.send_keys(Keys.ENTER)
# 2.点击登录
# driver.find_element_by_id("dologin").click()   #登录
# driver.back()  # 返回上一页
# driver.forward()  # 进到
"""
dr = webdriver.Chrome()
    #打开登陆163邮箱的网页
dr.get('https://mail.163.com/')
    #将浏览器窗口最大化
dr.maximize_window()
    #休息五分钟等待网页加载完毕
time.sleep(5)
asd=dr.find_element_by_id("switchAccountLogin")
asd.click()
    #找到邮箱账号输入框//*[@id="switchAccountLogin"]
dr.switch_to.frame(0)
time.sleep(2)
qwe = dr.find_element_by_name('email')
qwe.clear()
    #将自己的邮箱地址输入到邮箱账号框中
qwe.send_keys('Z199405156336')
    #找到密码输入框
password = dr.find_element_by_name('password')
    #输入自己的邮箱密码
password.clear()
password.send_keys('Zhao820515')
    #找到登陆按钮
login_btn = dr.find_element_by_id('dologin')
    #点击登陆按钮
login_btn.click()
    #等待10秒看是否登陆成功
time.sleep(10)

