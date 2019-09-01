#!/usr/bin/python
#-*- coding:utf-8 -*-
from __future__ import absolute_import
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

"""
if __name__ == '__main__':
    #orgin_url = ['https://pan.baidu.com/']
    driver = webdriver.Chrome()
    driver.get('https://pan.baidu.com/')
    # 将浏览器窗口最大化
    driver.maximize_window()
    #driver.get(orgin_url[0])
    #"TANGRAM__PSP_4__footerULoginBtn"
    time.sleep(5)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(0.5)
     #"TANGRAM__PSP_4__userName"
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(u"17792759651")  # 填入帐号
    #"TANGRAM__PSP_4__password"
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(u"Zhao820515")  # 密码
   # "TANGRAM__PSP_4__submit"
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    elem_submit.click()
    time.sleep(10)
    #driver.close()
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://mail.qq.com/')
    driver.maximize_window()
    time.sleep(5)
    driver.switch_to.frame('login_frame')
    #// *[ @ id = "sendtimepadding"]//*[@id="sendtimepadding"]
    elem_static = driver.find_element_by_id("switcher_plogin")
    elem_static.click()
    time.sleep(0.5)
    elem_username = driver.find_element_by_id("u")
    elem_username.clear()
    elem_username.send_keys("1147426361")
    elem_userpas = driver.find_element_by_id("p")
    elem_userpas.clear()
    elem_userpas.send_keys("Fei820515")
    elem_submit = driver.find_element_by_id("login_button")
    elem_submit.click()
    time.sleep(5)
    #登录之前
    elem_static1 = driver.find_element_by_id("composebtn")
    elem_static1.click()
    time.sleep(0.5)
    # 切换iframe至写信
    driver.switch_to.frame("mainFrame")
    # driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
    time.sleep(3)
    # 添加收件人
    driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys("Z199405156336@163.com")

    # 添加主题
    driver.find_element_by_xpath('//*[@id="subject"]').send_keys("TestCase1")
    # elem_static2 = driver.find_element_by_id("toAreaCtrl")
    # elem_static2.clear()
    # elem_static2.send_keys("Z199405156336@163.com")
    # elem_static3 = driver.find_element_by_id("subject")
    # elem_static3.clear()
    # elem_static3.send_keys("爱")
    driver.switch_to.default_content()
    # 切换Iframe至编辑正文
    driver.switch_to.frame("mainFrame")
    # Body_frame=driver.find_element_by_xpath('//iframe[@scrolling="auto"]')
    Body_frame = driver.find_element_by_class_name("qmEditorIfrmEditArea")
    driver.switch_to.frame(Body_frame)

    # 添加正文
    driver.find_element_by_xpath('/html/body').send_keys("I LOVE Python")
    time.sleep(3)

    # 退回大Frame再点击发送
    driver.switch_to.parent_frame()
    driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()

#//*[@id="toolbar"]/div/a[1]


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)  # 设置检查账号切换按钮超时时间
driver.get('https://mail.qq.com/cgi-bin/loginpage')
driver.switch_to.frame('login_frame')
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位
try:
    # 获取输入框
    input = wait.until(
        # 判断该元素是否加载完成
        EC.presence_of_element_located((By.CSS_SELECTOR, '#switcher_plogin'))
    )
    # 输入查询关键字
    input.click()

    # 获取搜索点击按钮
    submit = wait.until(
        # 判断该元素是否可以点击
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_button'))
    )
    driver.find_element_by_xpath("//*[@id='u']").send_keys("1147426361")
    driver.find_element_by_xpath("//*[@id='p']").send_keys("Fei820515")
    submit.click()
except TimeoutException:
    print('exception')
"""
