# import paramiko
# d=paramiko.Transport(("192.168.10.11",22))
# d.connect(username='root',password='123456')
# sftp=paramiko.SFTPClient.from_transport(d)
# x1='/home/zhaocf/fei.txt'
# x2='D:\daima/aa.txt'
# sftp.get(x1,x2)
# d.close()

import pymysql
connect=pymysql.connect(
    host='192.168.10.11',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    database='stu1993'
)
cu=connect.cursor()
sql="create table koo(name char(15))"
cu.execute(sql)
sql1="insert into koo values ('李四')"
cu.execute(sql1)
sql1="select *from ao"
cu.execute(sql1)
b=cu.fetchall()
print(b)
connect.commit()


import socket

#服务器端
ip_port=('127.0.0.1',6662)
s=socket.socket()
s.bind(ip_port)
s.listen(5)
print('启动socket服务，等待客户端连接……')
coon,address=s.accept()
while True:
    c_date = coon.recv(1024).decode('utf-8')  #第一步接收客户端发送的数据
    print(f"客户端向服务器发送的内容是{c_date}")
    #服务器向客户端发送数据
    t = input('输入发送到客户端的信息').strip()
    if t=='1':
        print('关闭服务器')
        break
    else:
        coon.sendall(t.encode())
s.close()

#客户端
ip_port=('127.0.0.1',6662)
c=socket.socket()   #创建套接字
c.connect(ip_port)
while True:
    t = input('输入发送的信息').strip()# 发送数据到服务器，接收服务器数据
    if t=='1':#设置一个条件跳出死循坏
        break
    else:
        print(f"客户端向服务器发送的信息")# 发送信息到服务器
        c.sendall(t.encode())
    s_date = c.recv(1024).decode('utf-8')#处理服务器已经发送到客户端上的信息
    print(s_date)
c.close()

#获取目录下有多少普通 链接 目录 文件
# import os
# class qwe(object):
#     def asd(self,name):
#         res=os.listdir(name)
#         a=0
#         b=0
#         c=0
#         for i in res:
#             if os.path.isdir(i):  #目录文件
#                 a+=1
#             elif os.path.isfile(i): #普通文件
#                 b+=1
#             elif os.path.islink(i):  #链接文件
#                 c+=1
#         print(f"目录：{a}个，文件：{b}个，链接文件：{c}个")
# a=qwe()