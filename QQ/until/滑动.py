#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import  webdriver
"""
#获取手机屏幕的大小
l=dr.get_window_size()
#放缩屏幕
x1=l["width"]*0.5
x2=1["width"]*0.75
y1=l["height"]*0.25
y2=l["heigth"]*0.5
#左滑动
dr.swipe(x2,y1,x1,y1,t=500)
#右滑动
dr.swipe(x1,y1,x2,y1)
#上滑动
dr.swipe(y2,x1,y1,x1)
#下滑动
dr.swipe(y1,x1,y2,x1)
"""
def swipe_left(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    driver.swipe(x2,y1,x1,y1,duration=t)
def swipe_right(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    driver.swipe(x1,y1,x2,y1,duration=t)
def swipe_down(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    driver.swipe(x1,y1,x1,y2,duration=t)
def swipe_up(driver,t=700):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    driver.swipe(x1,y2,x1,y1,duration=t)

"""
swipe(self, start_x, start_y, end_x, end_y, duration=None) 
    Swipe from one point to another point, for an optional duration.
    从一个点滑动到另外一个点，duration是持续时间

    :Args:
    - start_x - 开始滑动的x坐标
    - start_y - 开始滑动的y坐标
    - end_x - 结束点x坐标
    - end_y - 结束点y坐标
    - duration - 持续时间，单位毫秒

    :Usage:
    driver.swipe(100, 100, 100, 400)
"""