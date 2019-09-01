#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
pytest是python自动化测试一个工具库
作用：
1、调整测试用例的运行顺序
2、对测试用例传入测试数据
3、对测试用例设置断言
4、pytest与allure生成测试报告
特点：
   灵活、支持的插件丰富
"""

import pytest
"""
自动化测试用例指的是？
   指的是一个函数，必须以test开头
"""

def test_0():
    """计算100之内的和"""
    n=0
    for i in range(1,101):
        n += i
        #预期结果是5050
        #实际结果是n

        #断言指的是：那实际结果与预期结果进行对比的过程

    assert n == 5050   #断言

#AssertionError 断言错误


#执行测试用例
"""
pytest  -v test_1.py
py.test  -v test_1.py
"""
#生成测试用例
"""
1、 pytest test1.py --alluredir ./result/    #运行测试用例，保存到指定目录
2、allure generate ./result/ -o ./report/ --clean  #生成测试报告
3、allure open -h 127.0.0.1 -p 8083 ./report/   # 打开测试报告
"""

import pytest


# def test_1():
#     a = 1
#     b = 2
#     c = a + b
#     # 实际结果是3，预期结果是2
#     # 设定断言
#     assert c == 2
#
#
# def test_2():
#     str_1 = "hello pytest"
#     str_2 = "python"
#     # 设定断言，判断str_2 在 str_1内
#     assert str_2 in str_1