#!/usr/bin/python
#-*- coding:utf-8 -*-
#!/usr/bin/python
#-*- coding:utf-8 -
import logging
import datetime
#日志文件夹/目录

LOG_DIR="D:\\接口自动化\\log\\"

#日期.txt  创建一个日志文件名字
a=LOG_DIR+str(datetime.datetime.now().date())+'.txt'
print(a)
#logging  ---python定义日志的库
#定义日志输出的格式                   秒           等级                名字         多少行        输出信息       输出时间
formatter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formatter)
#logging的两种输出的方式
#第一种 输出到pycharm控制台
c=logging.StreamHandler()
#添加日志的样式
c.setFormatter(formatter)
#第二种输出到文本
w=logging.FileHandler(a,encoding="utf-8")
#添加日志样式
w.setFormatter(formatter)

#
def get_logger(filename):   #可以不写
    #获取执行日志的脚本名字
    l=logging.getLogger(filename)   #换成abc
    #添加输出内容到控制台
    l.addHandler(c)
    #添加输出内容到文本
    l.addHandler(w)
    #定义日志的等级   INFO（建议）—最低等级  DEBUG
    l.setLevel(logging.INFO)
    return l
# log=get_logger()
# log.info("dengji")
# log.error("cuowu")