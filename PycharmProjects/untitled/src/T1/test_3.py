#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
清理测试环境的机制
第一步：在用例执行之前进行环境经清理
第二步:在用例执行之后进行环境清理
"""

# 脚本级别的清理
#setup_module    用例执行之前
#teardown_module   用例执行之后
#  module  本脚本所有的用例执行前、后的操作仅执行一次

import pytest
# def setup_module():
#     print("所有用例执行之前执行一次")
# def test_1():
#     print("用例一执行")
# def test_2():
#     print("用例二执行")
# def test_3():
#     print("用例三执行")
# def teardown_module():
#     print("所有用例执行之后执行一次")

#setup_function   每个测试用例运行之前都要执行一次
#teardown_function  每个测试用例之后都要执行一次
# def setup_function():
#     print("每个用例执行之前执行一次")
# def test_1():
#     print("用例一执行")
# def test_2():
#     print("用例二执行")
# def test_3():
#     print("用例三执行")
# def teardown_function():
#     print("每个用例执行之后执行一次")

#setup 、teardown  在类的范围内使用

#setup -->每个测试用例执行之前运行一次
#teardown--->每个测试用例执行之后运行一次

"""
class TestOne(object):
    def setup(self):
        print("执行setup")
    def teardown(self):
        print("执行teardown")
    def test_4(self):
        print("执行测试四")
    def test_5(self):
        print("执行测试五")
    def test_6(self):
        print("执行测试六")
"""

#setup_class-->类中的所有测试用例执行之前运行一次
#teardown_class -->类中的所有测试用例执行之后运行一次
"""
class TestOne(object):
    def setup_class(self):
        print("执行setup")
    def teardown_class(self):
        print("执行teardown")
    def test_4(self):
        print("执行测试四")
    def test_5(self):
        print("执行测试五")
    def test_6(self):
        print("执行测试六")
"""

#setup_method  --->每个测试用例运行执行之前运行一次 方法级别
#teardown_method-->每个测试用例运行执行之后运行一次
""""
class TestOne(object):
    def setup_method (self):
        print("执行setup_method ")
    def teardown_method(self):
        print("执行teardown_method")
    def test_4(self):
        print("执行测试四")
    def test_5(self):
        print("执行测试五")
    def test_6(self):
        print("执行测试六")
"""

# 测试夹具  fixture
#@pytest.fixture()
"""
scope:装饰器的作用范围 
    function 方法级别、默认   指定测试用例执行之前清理环境
    class  类级别            所有测试用例只执行一次清理环境
    module  脚本级别   所有的测试用例执行之前执行一次，最后一个之前运行 一次
                      使用方式：在测试用例的（放被@pytest.fixture装饰的函数名）

    package  包级别    目录级别
    session  会话级别   会话级别，多个测试用例组合的时候使用
"""

# @pytest.fixture()
# def login():
#     print("login函数开始执行")
# def test_1(login):
#     print("执行用例一")
# def test_2(login):
#     print("执行用例二")
# def test_3(login):
#     print("执行用例三")


# class TestThree(object):
#     @pytest.fixture(scope="class")
#     def login_1(self):
#         print("开始执行login_1方法")
#
#     def test_4(self,login_1):
#         print("执行用例四")
#     def test_5(self,login_1):
#         print("执行用例五")

"""
@pytest.fixture(scope="module")
def start():
    print("所有的测试用例之前运行一次")
@pytest.fixture(scope="module")
def close():
    print("测试用例之前运行一次，只运行一次")

def test_1(start):
    print(1)
def test_2(start):
    print(2)
def test_3(close):
    print(3)
# class  TestOne(object):
#     def test_3(self,close):
#         pass
"""

#conftest.py
"""
conftest.py :   python文件，用来存放公共函数.被不同测试用例使用，test脚本下，
                只有以test开头的脚本，一般只写test开头函数、类、方法
                注意事项：
		            conftest.py必须放在当前测试用例所在的目录下面
		            src/T1/test_1.py， conftest.py必须放在T1下面
		


"""
"""
def test_1():
    print("输入账号、密码")
def test_2(clean):
    print("输入账号、密码")
def test_3(clean):
    print("输入账号、密码")
"""

#参数化--->向测试用例中传入参数的过程
"""
d=[1,2,3,4,5,6,7]
@pytest.fixture(scope='function',params=d)
def read_data(request):
    #request ：必须写成这样，固定写法
    #作用： 取出参数列表中的每一个元素
    #request.param   ：  固定写法
    #作用： 与request结合使用，取出参数
    print(f"当前的传入的参数是{request.param}")
    return request.param  # 1--7
def test_1(read_data):
    t=read_data  #实际结果
    #预期结果
    assert t<6
"""
#传入两个参数
"""
d2=[(1,2),(2,2),(3,4)]
@pytest.mark.parametrize("y1,y2",d2)   #y1 y2 就是列表中的元祖中的两个参数
def test_2(y1,y2):
    print(f"y1的值是{y1}")
    print(f"y2的值是{y2}")
    assert y1==y2
 """
@pytest.fixture(autouse="true")
def myfix():
    print("每个测试用例要跑myfix")
#ids:
#name:
#pytest 跳过某些用例、失败重跑、统计测试覆盖率等
#@pytest.mark.usefixtures("myfix")  等价于 (myfix)
#pytestmark=pytest.mark.usefixtures("myfix")

# def test_1():
#     pass
# def test_2():
#     pass







