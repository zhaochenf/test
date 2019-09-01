#!/usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Chrome()
#访问网址
#dr.get("https://www.baidu.com")
#获取访问网址的标题
#print(dr.title)
#获取访问的网址
#print(dr.current_url)
#设置浏览器窗口的大小
#dr.set_window_size(400,400)  #宽、高
#设置浏览器的位置
#dr.set_window_position(400,400)
#最大化浏览器
#dr.maximize_window()
#最小化浏览器
#dr.minimize_window()

# sleep(2)
# dr.get("https://www.jd.com")
# sleep(2)
#返回到上一次的页面
#dr.back()
#前进到第二个页面
# dr.forward()

#核心：定位

#id、class_name、name、link_text、tag_name、xpath、css、partial_link_text
#一般 id 、xpath、css、name
#id定位  动作：click（）   send_keys("内容")
#dr.find_element_by_id("kw").send_keys("python")
#dr.find_element_by_id("su").click()

#class_name  定位  唯一的
#dr.find_element_by_class_name("class属性的值")

#name   指的是name属性
#dr.find_element_by_name("name属性的值")

#link_text定位    文本定位   两个标签之间的文字
#dr.find_element_by_link_text("新闻").click()

#partial_link_text    模糊文本     一段文字标题提取其中的关键字
#dr.find_element_by_partial_link_text("一张身份证").click()

#tag_name  标签定位：通常定位一组对象

#xml  可扩展标记语言  内容和html一样
   #作用：储存数据
#xpath  路径标记语言 ：绝对路径、相对路径
#dr.find_element_by_xpath("").click()
#css
#dr.find_element_by_css_selector("#u_sp > a:nth-child(1)")
"""
#定位一组对象  同时定位多个元素  结果是列表
#层级定位：先定位一个大范围，再从大范围中定位元素
# dr.父元素.子元素.动作
#父元素必须是唯一的，子元素可以是一组，也可以是唯一的


#携程网
dr.get("https://www.ctrip.com/")
sleep(2)
#酒店级别
dd=dr.find_element_by_id("searchHotelLevelSelect").find_elements_by_tag_name("option")
for i in dd:
    #i.click()
    print(i.text)
    sleep(2)
#房间
ad=dr.find_element_by_id("J_roomCountList").find_elements_by_tag_name("option")
for i in ad:
    #i.click()
    print(i.text)
    sleep(2)
"""

#京东
# dr.get("https://www.jd.com/")
# sleep(2)
# aa=dr.find_element_by_id("J_cate").find_elements_by_class_name("cate_menu_lk")
# for i in aa:
#     print(i.text)
#     sleep(2)

#访问网址
#dr.get("http://qzone.qq.cm")
#sleep(2)
#iframe 内嵌框架
#切换框架，只可以用id的值或name的值
#没有id，没有name，先定位到框架，再切换
#ww=dr.find_element_by_xpath("//*[@id="login_frame"]")
#dr.switch_to.frame("ww")
#dr.switch_to.frame("login_frame")
#sleep(2)
#退出到上一层框架
#dr.switch_to.parent_frame()
#退出到第一层页面
#dr.switch_to_default.content()

#豆瓣
#dr.get("https://www.douban.com/")
#sleep(2)
"""
#获取当前的窗口的句柄
dd=dr.current_window_handle
print(dd)
dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
sleep(2)
#获取所有窗口的句柄  列表
da=dr.window_handles
print(da)
#切换窗口
dr.switch_to.window(da[-1])
print(dr.title)
#浏览器管理窗口的原理：
#浏览器会对每个打开的窗口生成一个唯一标识窗口的句柄

#谷歌产生的句柄是一对字符串，火狐产生的是一对数字
"""
"""
#访问网址
dr.get("file:///C:/Users/zhaocf/Desktop/abc.html")
sleep(2)
dr.find_element_by_xpath('/html/body/button').click()
sleep(2)
#处理弹出框   alert弹出框
ww=dr.switch_to_alert()
print(ww.text)      #获取弹出框的文本
#ww.accept()   #点击弹出框上的确定
ww.send_keys('python')   #给弹出框上输入内容
ww.accept()
#ww.dismiss()   #点击弹出框上的取消
"""

#执行JavaScript函数
#1.滚动条滚动到指定位置
# dr.get('https://www.ifeng.com/')
# sleep(2)
# dd=dr.find_element_by_xpath('//*[@id="autoNewsList"]/div[1]/a[1]')
# dr.execute_script('arguments[0].scrollIntoView();',dd)
# sleep(2)
# da=dr.find_element_by_xpath('//*[@id="newsList"]/ul[1]/li[1]/h1')
# dr.execute_script('arguments[0].scrollIntoView();',da)
#2.更改页面的高度滑动滚动条   10000指的是高度
# for i in range(0,10000,200):
#     js=f"var q=document.documentElement.scrollTop={i}"
#     dr.execute_script(js)
#     sleep(2)

#访问网址
#dr.get('https://www.jd.com')
#sleep(2)  #强制等待
#智能等待
#unti=ui.WebDriverWait(dr,10)
#定位要出现的元素
#unti.until(lambda dr:dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a').is_displayed())

#移动鼠标
# ww=dr.find_elements_by_class_name('cate_menu_item')
# for i in ww:
#     #动作链:动作链控制鼠标移动到某个元素的中心点
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
#拖拽
dr.get('https://qzone.qq.com/')
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
dr.find_element_by_xpath('//*[@id="u"]').send_keys('9234523')
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('cf5726347')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
ww=dr.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
dr.switch_to.frame(ww)
sleep(2)
dd=dr.find_element_by_id('tcaptcha_drag_button')
ActionChains(dr).drag_and_drop_by_offset(dd,182,0).perform()



