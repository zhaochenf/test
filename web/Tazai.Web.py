#!/usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Chrome()
#dr.get('https://www.baidu.com')
# sleep(3)
# mouse=dr.find_element_by_partial_link_text('设置')
# ActionChains(dr).move_to_element(mouse).perform()
# move_mouse = dr.find_element_by_xpath(".//*[@id='u1']/a[8]")
# ActionChains(dr).move_to_element(move_mouse).perform()
# dr.find_element_by_name("tj_nuomi").click()


dr.get("https://www.visvachina.com/#/square")
dr.maximize_window()
sleep(2)
dr.find_element_by_xpath('//*[@id="button-group"]/div[1]').click()  #点击密码登录
sleep(2)
dr.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/input").send_keys("17792759651")  #账号
sleep(2)
dr.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/input").send_keys("fei820515") #密码
sleep(1)
dr.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]").click()#确认登录
sleep(5)
#dr.close()
#dr.quit()
"""
for i in range(0,200,20):
    js=f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(2)
#dr.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]').find_element_by_link_text("关于我们").click()
dr.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[2]').click()  #关于我们
for i in range(0,400,75):
    js=f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(2)
dr.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[3]').click() #加入我们
for i in range(0,700,127):
    js=f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(2)
dr.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[4]').click()
for i in range(0,1000,120):
    js=f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(2)
"""
#muse=dr.find_element_by_class_name('notification_button el-popover__reference')
#muse=dr.f.find_element_by_xpath('root > div > div.header-component > div > div.right').find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[3]/span')
#ActionChains(dr).move_to_element(muse).perform()
#root > div > div.header-component > div > div.right > span
# sleep(2)
# qwe=dr.find_elements_by_class_name('item')
# for i in qwe:
#     print(i.text)
#ActionChains(dr).move_to_element(i).perform()
# ActionChains(dr).move_to_element(mouse).perform()
#
# //*[@id="root"]/div/div[1]/div/div[3]


dr.find_element_by_class_name('add-component').click()   #点击加号
sleep(2)

se=dr.find_elements_by_class_name('el-dropdown-menu__item')
# for i in se:
#     print(i.text)
#     sleep(2)
se[1].click() #提问
sleep(3)
dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/input[1]').send_keys('python')
sleep(2)
dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/textarea').send_keys('高级编程语言')
sleep(1)
dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[6]/div[2]').click()
sleep(2)
c=dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[2]').text
print(c)

sleep(2)
dr.find_element_by_xpath('/html/body/div[3]/div/div[1]/button').click()

