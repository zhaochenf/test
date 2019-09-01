#!/usr/bin/python
#-*- coding:utf-8 -*-
from appium import  webdriver
def swipe_left(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.2
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    driver.swipe(x2,y1,x1,y1,duration=t)
def swipe_right(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.1
    x2 = l["width"] * 0.9
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    driver.swipe(x1,y1,x2,y1,duration=t)
def swipe_down(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.8
    driver.swipe(x1,y1,x1,y2,duration=t)
def swipe_up(driver,t=700):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.15
    y2 = l["height"] * 0.9
    driver.swipe(x1,y2,x1,y1,duration=t)