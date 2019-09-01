#!/usr/bin/python
#-*- coding:utf-8 -*-
#import appium
from appium import webdriver
from time import sleep
#python 代码客户端连接手机时所需要的信息
d={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true"
}
#步骤一：与手机建立连接
# "http://127.0.0.1:4723/wd/hub"    "http://localhost:4723/wd/hub"
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
"""
将手机信息发送到appium服务器，使服务器和手机建立一个session
appium与python 客户端建立一个连接
"""
#appium 运行步骤
"""
1.python客户端与appium服务器建立一个连接
2.python代码中的命令由appium服务器转发
3.手机中bootstrap.jar服务接收到转发的命令
4.处理转发命令，将命令下发各uiautomator(手机自带测试框架：执行类似于adb命令）
5.uiautomator  生成一个执行之后的结果
6.结果转发给bootstrap.jar微服务器
7.一直转发到python客户端，appium库解析结果
8.将结果输出来
"""

"""
id:一般是唯一的，标记一个元素
class：标记一组元素，一般是多个
text：是否可以获取文字，有文字代表可以获取
clickable：判断是否可以被点击，true可以被点击，False不可以
"""
#第二步： 执行操作
"""
id不唯一，使用class定位
解决方法：
     向上一级或上上一级查找id唯一、class唯一。
     再使用class进行定位
"""
#先找唯一的id，再找class
#联系人、看点、动态 三个组成的列表[1,2,3]
# sleep(5)
# s=dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
# # for i in s:
#     i.click()
# #消息的可点击的定位
# dr.find_element_by_id("android:id/tabs").find_element_by_class_name("android.widget.RelativeLayout").click()

#获取qq下面的四个功能字段
# sleep(5)
# d=dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.TextView")
# for i in d:
#     print(i.text)

#给QQ置顶的朋友发消息
sleep(3)
qwe=dr.find_element_by_id("com.tencent.mobileqq:id/recent_chat_list").find_element_by_class_name("android.widget.LinearLayout").click()
dr.find_element_by_id("com.tencent.mobileqq:id/input").send_keys('1147426361')
dr.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click() #点击发送消息
m=dr.find_element_by_id("com.tencent.mobileqq:id/rlCommenTitle").find_elements_by_id("com.tencent.mobileqq:id/name")
m[3].click()    #根据索引   返回
dr.find_element_by_id("com.tencent.mobileqq:id/conversation_head").click()  #点击图像
sleep(2)
dr.find_element_by_id("com.tencent.mobileqq:id/settings").click()  #设置
sleep(3)
dr.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()  #账号管理
sleep(2)
dr.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()  #退出当前账号
dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()   #点击确定











