#！/usr/bin/python
#-*- coding:utf-8 -*-
a="12345"
b=a[::-1]
c=0
for i,j in enumerate(b):
    for n in range(10):
        if str(n)==j:
            c+=n*10**i
print(c)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={i*j}\t",end="")
#     print()

# a=[]
# for i in range(1,5):
#     for j in range(1,5):
#         for n in range(1,5):
#             if i!=j and j!=n and i!=n:
#                 a1=i*100+j*10+n
#                 a.append(a1)
# print(a)
# print(len(a))

# import paramiko
# connect=paramiko.c


#import os
#os.mkdir("aaa")
# with open(file=r"D:\untitled\aaa\a.txt",mode='w',encoding='utf8') as fb:
#     for i in range(1,10):
#         for j in range(1,i+1):
#            fb.write(f"{j}x{i}={j*i}\t")
#         fb.write('\n')
# with open(file=r"D:\untitled\aaa\a.txt",mode='r',encoding='utf8') as fb:
#     b=fb.read()
#     print(b)
#os.remove(r'D:\untitled\aaa\a.txt')
#os.rmdir("aaa")





# import  paramiko
# class add(object):
#     def qwe(self):
#         d=paramiko.Transport(('192.168.10.8',22))
#         d.connect(username='root',password='123456')
#         sftp=paramiko.SFTPClient.from_transport(d)
#         # x1='/home/zhaocf/fei.txt'
#         # x2=r'D:\untitled\b.txt'
#         # sftp.get(x1,x2)
#         # d.close()
#         x1 = ['/home/zhaocf/fei.txt','/home/zhaocf/chen.txt']
#         x2 = ['D:/untitled/b.txt', 'D:/untitled/c.txt']
#         for i in range(len(x1)):
#             sftp.get(x1[i], x2[i])


#q=add()
#q.qwe()

# import os
# class qwe(object):
#     def asd(self,name):
#         res=os.listdir(name)
#         a=0
#         b=0
#         for i in res:
#             if os.path.isdir(i):  #目录文件
#                 a+=1
#             elif os.path.isfile(i): #普通文件
#                 b+=1
#         print(f"目录：{a}个，文件：{b}个")
# a=qwe()
# a.asd(r"D:\untitled")

# import  xlwt
# f1=xlwt.Workbook()
# table=f1.add_sheet("234")
# with open(file='b.txt',mode='r',encoding='utf-8') as f:
#    a=f.read()
# a1=a.split('\n')
# a2=[]
# for i in a1:
#     a2.append(i.split(","))
# for i in range(len(a2)):
#     for j in range(len(a2[i])):
#         table.write(i,j,a2[i][j])
# f1.save("bi.xls")
"""

import pymysql, requests, re


class add(object):

    def qwe(self):
        req = requests.get(
            r'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.48498904&x-zp-page-request-id=5d3adb3d803a48978ee33ed373e60afd-1562671210360-559078&x-zp-client-id=2b6969d6-4354-4ead-8150-5d0dc8a4ddb8',
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"})
        res = req.text
        s = re.compile(
            r'"jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',
            re.S)
        s1 = re.findall(s, res)
        # print(s1)
        return s1

    def foo(self):
        al = self.qwe()
        # print(al)
        connect = pymysql.connect(
            host="192.168.0.189",
            port=3306,
            user="root",
            password="123456",
            charset="utf8",
           database='stu1994')

        cu = connect.cursor()
        # sql = "create database stu1994 default charset utf8 collate utf8_general_ci"
        #cu.execute(sql)

        sql2 = "create table no1(zhiwei char(25),gs char(25),dq char(10),xz char(10),xl char(15),nianx char(15))"
        cu.execute(sql2)

        for i in al:
            asd = f"insert into no1 values {i}"
            cu.execute(asd)
        connect.commit()


a = add()
a.qwe()
a.foo()


# import  smtplib
# from email.mime.text import MIMEText
# from email.header import  Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# mail_host="smtp.163.com"
# mail_user="z199405156336@163.com"
# mail_pass="z17792759651"
# mail_port=465
# sender="z199405156336@163.com"
# recivers=['18317822978@163.com']
# message=MIMEMultipart()
# message['From']=Header(sender)
# message['To']=Header(str(";".join(recivers)))
# subject="python测试邮件"
# message['Subject']=Header(subject)
# with open('b.txt','r',encoding="utf-8") as h:
#     connect2=h.read()
# part2=MIMEText(connect2,'plain','utf-8')
# part2['Content-Type'] = 'application/octet-stream'
# #设置附件头，添加文件名
# part2['Content-Disposition'] = 'attachment;filename="b.txt"'
# message.attach(part2)
# try:
#     smtpObj = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
#     smtpObj.login(user=mail_user, password=mail_pass)
#     smtpObj.sendmail(sender,recivers, message.as_string())
#     smtpObj.quit()
#     print('success')
# except smtplib.SMTPException as e:
#     print('error', e)  # 打印错误


# import  requests, re
# class add(object):
#     def qwe(self):
#         url = f'https://www.qiushibaike.com/text/'
#         header={
#                 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
#                 }
#         html = requests.get(url=url,headers=header)
#         date=html.content.decode('utf-8')
#         # print(date)
#         return date
#
#     def koo(self,):
#         req=re.compile('<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
#         res=req.findall(self.qwe())
#         for i in res:
#             a1 = i.strip()
#             a2=a1.replace("<br/>","\n")
#             print(a2)
#             with open('百科.txt',mode='a',encoding='utf-8')as fs:
#                 fs.write(a2)
# a=add()
# a.qwe()
# a.koo()

# import pymysql
# class add(object):
#     def test1(self):
#         con = pymysql.connect(
#             host='192.168.10.8',
#             port=3306,
#             user='root',
#             password='123456',
#             charset='utf8',
#             database='stu1993',
#         )
#         self.cur = con.cursor()
#
#     def test2(self):
        # self.test1()
        # sql_create = 'create table test9(id varchar(32),num varchar(32),nam varchar(32),age varchar(32)) '
        # self.cur.execute(sql_create)
        # a = []
#         with open('a.txt', encoding='utf-8') as fc:
#             txt_date = fc.read()
#             a.append(txt_date)
#             print(a)
#             txt_list = a.split(',')
#         for i in txt_list:
#             txt_list_1 = i.split(',')
#             sql_2 = f"insert into test9 values {tuple(txt_list_1)}"
#             self.cur.execute(sql_2)
# a=add()
# a.test1()
# a.test2()

"""
