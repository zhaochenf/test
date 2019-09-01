#!/usr/bin/python
#-*- coding:utf-8 -*-
from until.ReadData import  s
from until.滑动 import swipe_up
from until.滑动 import swipe_down
from until.滑动 import swipe_left
from until.滑动 import swipe_right
import pytest
from time import sleep

def test_1(lianjie):
    swipe_up(lianjie)
    sleep(5)
    swipe_down(lianjie)
    sleep(5)
    swipe_left(lianjie)
    sleep(4)
    swipe_right(lianjie)