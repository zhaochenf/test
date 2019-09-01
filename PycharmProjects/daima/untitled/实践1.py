#！/usr/bin/python
#-*- coding:utf-8 -*-
# import socket
#
# #服务器端
# ip_port=('127.0.0.1',6662)
# s=socket.socket()
# s.bind(ip_port)
# s.listen(5)
# print('启动socket服务，等待客户端连接……')
# coon,address=s.accept()
# while True:
#     c_date = coon.recv(1024).decode('utf-8')
#     print(f"客户端向服务器发送的内容是{c_date}")
#     t = input('输入发送到客户端的信息').strip()
#     if t=='1':
#         print('关闭服务器')
#         break
#     else:
#         coon.sendall(t.encode())
# s.close()

import pymysql
class A(object):
    def __init__(self,x1):
        self.x1 = x1
        self.w = pymysql.connect(
            host="192.168.10.8",
            user="root",
            port=3306,
            password="123456",
            charset="utf8",
            database="stu1993",
        )
        self.cur = self.w.cursor()
    def ad(self):
        sql1 = "create table aa3 (name char(20),name2 char(20),name3 char(20),name4 int)"
        self.cur.execute(sql1)
    def aaa(self):
        with open("a.txt", mode="r", encoding="utf-8") as f:
            a = f.read()
            t = a.strip()
            b = t.split("\n")
            print(b)
            print(len(b))
            for i in range(len(b)):
                ww = b[i].split(",")
                r = tuple(ww)
                print(r)
                sql2 = f"insert into aa3 values {r}"
                self.cur.execute(sql2)
        self.w.commit()

a3 = A("a.txt")
#a3.ad()
a3.aaa()

# with open(file='a.txt',mode='w',encoding='utf-8') as fb:
#     fb.write('hello world shell mihao\n'*100)