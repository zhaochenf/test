#!/usr/bin/python
#-*- coding:utf-8 -*-
import allure
import pytest
#  讲解网站  测试报告   https://testerhome.com/topics/15649

#featuure : 标注测试用例是属于哪一个模块的
@allure.feature("模块一")
def test_1():
    assert  0==0
@allure.feature("模块一")
def test_2():
    assert  0<1
#story :对一个测试用例的详细描述
@allure.feature("模块二")
@allure.story("这是一个很牛逼的测试用例")
def test_3():
    assert 0 >19293

@allure.feature("模块二")
@allure.story("这是一个垃圾的测试用例")
def test_4():
    """
    这是对函数的参数、返回值的一个注释
    自我感觉老牛逼
    """
    #测试用例的描述是通过 函数的注释时来获取到的
    assert "香港是中国的"


#测试用例的优先级
"""
Blocker级别：阻塞中断缺陷（客户端程序无响应，无法执行下一步操作）
Critical级别：临界缺陷（严重）
Normal级别：普通缺陷（数值计算错误）
 Minor级别：次要缺陷（界面错误与UI需求不符）
 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
"""
#severity   标注测试用例优先级

@allure.feature("模块三")
@allure.severity("blocker")
def test_5():
    assert 0==0
@allure.feature("模块三")
@allure.severity("normal")
def test_6():
    assert 0==0

@allure.feature("模块三")
@allure.severity("critical")
def test_7():
    assert 0==0
@allure.feature("模块三")
@allure.severity("minor")
def test_8():
    assert 0==0
@allure.feature("模块三")
@allure.severity("trivial")
def test_9():
    assert 0==0
#Git --svn ---Jenkins-- 执行python代码--报告--访问某个网址

#step 记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
#isinstance()  判断数据类型的类，参数一和参数二是否是同一个类型，是的话--true    不是--flase

@allure.step("字符串相加：{0},{1}")
def str_add(str1, str2):
    if not isinstance(str1, str):
        return f"{str1}不是字符串类型"
    if not isinstance(str2, str):
        return f"{str2}不是字符串类型"
    return str1+str2
@allure.feature("模块四")
def test_10():
    str1="hello"
    str2="world"
    assert str_add(str1,str2)=="helloworld"

#issue 和 testcase
#对issue和testcase 生成一个网址
@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('模块五')
@allure.story('test_story_01')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")  #详细问题
@allure.testcase("http://www.testlink.com") #测试用例
def test_11():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'
#file = open(r'D:\Tazai\baogao\report\data\test.png', 'rb').read()
file = open('../test.png', 'rb').read()
allure.attach('test_img', file, allure.attach_type.PNG)
"""
在报告中增加附件：allure.attach(’arg1’,’arg2’,’arg3’)：
arg1：是在报告中显示的附件名称 
arg2：表示添加附件的内容 
arg3：表示添加的类型(支持:HTML,JPG,PNG,JSON,OTHER,TEXTXML)
"""



