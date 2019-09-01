# -*- coding: utf-8 -*-

#python --套接字
#使用模块：socket
#套接字作用？
# 实现两个或多个应用的数据传输

"""
#服务端
import socket

#指定服务器的ip地址、监听端口号
ip_port=('127.0.0.1',6662)
#建立一个套接字，为了服务器与客户端传输信息
s=socket.socket()
#绑定服务地址和端口号
s.bind(ip_port)
#设置最大连接数
s.listen(5)
#提示服务端已经开启的信息
print('启动socket服务，等待客户端连接……')
#socket 自动处理拥塞控制    #accept()持续开启服务，一直到手动关闭位置
coon,address=s.accept()

# #处理客户端发过来的数据
# #第一步接收客户端发送的数据
# c_date=coon.recv(1024).decode('utf-8')
# print(c_date)
# print(address)
# t=input('输入发送的信息').strip()
# #发送
# s.sendall(t.encode())

#关闭连接
#s.close()
while True:
    #第一步接收客户端发送的数据
    c_date = coon.recv(1024).decode('utf-8')
    print(f"客户端向服务器发送的内容是{c_date}")
    #服务器向客户端发送数据
    t = input('输入发送到客户端的信息').strip()
    if t=='1':
        print('关闭服务器')
        break
    else:
    # 发送信息给客户端  1先找到客户端  2使用sendall
        coon.sendall(t.encode())
#关闭服务器的链接
s.close()

import socket
#客户端

#指定客户端ip，目的端口号
ip_port=('127.0.0.1',6662)
#创建一个套接字，目地接受服务器发送的数据
c=socket.socket()   #创建套接字
#连接服务器
c.connect(ip_port)
#发送数据到服务器，接收服务器数据
#t=input('输入发送的信息').strip()
#发送
#c.sendall(t.encode())
while True:
    # 发送数据到服务器，接收服务器数据
    t = input('输入发送的信息').strip()
    #设置一个条件跳出死循坏
    if t=='1':
        break
    else:
        # 发送信息到服务器
        print(f"客户端向服务器发送的信息")
        c.sendall(t.encode())
    #处理服务器已经发送到客户端上的信息
    s_date = c.recv(1024).decode('utf-8')
    print(s_date)
#关闭连接
c.close()
"""

# python --发送电子邮件
#使用的模块   smtplib 、email

import  smtplib
from email.mime.text import MIMEText
from email.header import  Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
"""
#设置服务器所需要的信息

#邮件服务器的地址
mail_host="smtp.163.com"
#用户名
mail_user="z199405156336@163.com"
#客户端授权码或密码
mail_pass="z17792759651"
#设置服务器端口号
mail_port=465
#邮件发送方的地址
sender="z199405156336@163.com"
#邮件接收方的地址
recivers=['13592386651@163.com']    #可以写多个

# 设置邮件信息如下

#设置邮件主题
subject="python测试邮件"
#设置邮件正文
content="这是我使用python发送的邮件"
#三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8设置编码
message=MIMEText(content,'plain','utf-8')

#发送邮件时填写发件人、发件人、主题
#header():填写邮件头部

#发送发信息
message['From']=Header(sender)
#接收方信息
message['To']=Header(str(";".join(recivers)))
#主题绑定
message['Subject']=Header(subject)

#登录并发送邮件
try:
    #第一步、登录到自己的邮箱
    #不使用授权码
    #smtpObj=smtplib.SMTP()
    #连接到服务器
    #smtpObj.connect(mail_host,25)
    smtpObj=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
    #输入密码登录邮箱
    smtpObj.login(user=mail_user,password=mail_pass)
    #发送邮件   as_string()以字符串的形式发送出去
    smtpObj.sendmail(sender,recivers,message.as_string())
    #发送邮件之后退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e)  #打印错误
"""
"""
class A(object):
    #def qwe(self):
    mail_host = "smtp.163.com"
    mail_user = "z199405156336@163.com"
    mail_pass = "z17792759651"
    mail_port = 465
    sender = "z199405156336@163.com"
    recivers = ['13592386651@163.com']

    def asd(self):
        subject = "python测试邮件"
        content = "这是我使用python发送的邮件"
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header(self.sender)
        message['To'] = Header(str(";".join(self.recivers)))
        message['Subject'] = Header(subject)

        try:
            smtpObj = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)
            smtpObj.login(user=self.mail_user, password=self.mail_pass)
            smtpObj.sendmail(self.sender, self.recivers, message.as_string)
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误
q=A()
q.asd()
"""

"""
mail_host="smtp.163.com"
#用户名
mail_user="z199405156336@163.com"
#客户端授权码或密码
mail_pass="z17792759651"
#设置服务器端口号
mail_port=465
#邮件发送方的地址
sender="z199405156336@163.com"
#邮件接收方的地址
recivers=['13592386651@163.com']    #可以写多个

#添加一个MIMEMultipart类，处理正文及附件添加到邮件里
message=MIMEMultipart()
#发送发信息
message['From']=Header(sender)
#接收方信息
message['To']=Header(str(";".join(recivers)))
subject="python测试邮件"
#主题绑定
message['Subject']=Header(subject)
#使用html格式的正文内容，添加附件
with open('abc.html','r',encoding="utf-8") as f:
    connect=f.read()
#设置html 格式参数
part1=MIMEText(connect,'html','utf-8')
#以下都是附件代码：

#添加一个txt文件附件
with open('b.txt','r',encoding="utf-8") as h:
    connect2=h.read()
#设置txt参数
part2=MIMEText(connect2,'plain','utf-8')
# 附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="b.txt"'
#添加照片附件
with open('123.png','rb') as fp:
    #MIMEImage 加载二进制图片，用于附件传输
    picture=MIMEImage(fp.read())
picture['Content-Type'] = 'application/octet-stream'
picture['Content-Disposition'] = 'attachment;filename="123.png"'
#将内容添加到邮件主体中  attach(添加的内容）

#将html添加到邮件里
message.attach(part1)
message.attach(part2)
message.attach(picture)
try:
    smtpObj = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
    smtpObj.login(user=mail_user, password=mail_pass)
    smtpObj.sendmail(sender,recivers, message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)  # 打印错误
"""
