
#质数之和
# class a(object):
#     def asd(self,x1,x2):
#         a=0
#         for i in range(1,x2):
#             c=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     c+=1
#             if c==2:
#                 a+=i
#         return a
#         #print(a)
# d=a()
# print(d.asd(1,101))

# b=0
# for i in range(2,101):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         b+=i
# print(b)


#查看文件内容
# class A(object):
#     def __init__(self,name):
#         self.name=name
#     def du(self):
#         f=open(file=self.name,mode='r',encoding='utf-8')
#         f1=f.read()
#         print(f1)
#         f.close()
# c=A('a.txt')
# c.du()

# def add(a):
#     b=a.split(" ")
#     c=len(b)
#     for i in range(c):
#         for j in range(c-1):
#             if int(b[j])>int(b[j+1]):
#                 b[j],b[j+1]=b[j+1],b[j]
#     print(b)
# add("123 23 3 45 21")
"""
class A(object):     #冒泡
    def add(self,a):
        b = a.split(" ")
        c = len(b)
        for i in range(c):
            for j in range(c - 1):
                if int(b[j]) > int(b[j + 1]):
                    b[j], b[j + 1] = b[j + 1], b[j]
        print(b)
    def qwe(self,b):   #选择
        d=b.split(" ")
        e=len(d)
        for i in range(e):
            for j in range(i+1,e):
                if int(d[i])>int(d[j]):
                    d[i],d[j]=d[j],d[i]
        print(d)
    def koo(self,c):    #将“12345”，不使用int输出12345
        a=0
        b=c[::-1]
        for i,j in enumerate(b):
            for n in range(10):
                if j==str(n):
                    a+=n*(10**i)
        print(a)
    def foo(self):    #99乘法表
        for i in range(1,10):
            for j in range(1,i+1):
                print(f"{j}x{i}={i*j}\t", end="")
            print()
    def coo(self):    #100之内奇数减偶数
        sum=0
        for i in range(100):
            if i%2==0:
                sum-=i
            else:
                sum+=i
        print(sum)

a=A()
#a.add("123 21 4 25")
#a.qwe("123 32 5 65")
#a.koo("12345")
a.foo()
#a.coo()
"""
#去除重复的
# a=[1,2,2,3,4,4,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
#阶乘之和
# a=0
# b=1
# for i in range(1,6):
#     b=b*i
#     a=a+b
# print(a)
#因数之和
# for i in range(1,1000):
#     n=0
#     for j in range(1,i):
#         if i%j==0:
#             n+=j
#     if n==i:
#         print(i)

#水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if i==a**3+b**3+c**3:
#         print(i)

#99乘法表写入表格

# import  xlwt
# class add(object):
#     def __init__(self):
#         self.d = xlwt.Workbook()
#         self.table = self.d.add_sheet("sheet1")
#     def qwe(self):
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 self.table.write(i-1,j-1,f"{j}x{i}={j*i}")
#         self.d.save("26.xls")
# a=add()
# a.qwe()

# class add(object):
#     def qwe(self):
#         f = open(file="b.txt", mode="w", encoding="utf-8")
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 f.write(f"{j}x{i}={j*i}\t")
#             f.write("\n")
#         f.close()
# a=add()
# a.qwe()
# with open('b.txt','w',encoding='utf-8') as fb:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             fb.write(f"{j}x{i}={j*i}\t")
#         fb.write("\n")
# with open('b.txt','r',encoding='utf-8') as fb:
#     a=fb.read()
#     #fb.write('abcd')
#     print(a)

# import pymysql
# connect=pymysql.connect(
#     host='192.168.10.30',
#     port=3306,
#     user='root',
#     password='123456',
#     charset='utf8',
#     database='stu1993'
#                       )
# cu=connect.cursor()
# # sql="create table python(name char(15))"
# # cu.execute(sql)
# sql1="select *from ao"
# cu.execute(sql1)
# b=cu.fetchall()
# print(b)

"""
import paramiko
import pymysql
class asd(object):
    def qwe(self):  #连接Linux
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(
                hostname='192.168.0.110',
                port=22,
                username='root',
                password='123456')
        stdin, stdout, stderr = s.exec_command('ls -al')
        print(stdout.read().decode())
    def koo(self):  #连接数据库
        connect = pymysql.connect(
            host="192.168.10.30",
            port=3306,
            user="root",
            password="123456",
            charset="utf8",
            database="stu1993",
        )


        cu = connect.cursor()
        sql = "create database stu1992 default charset utf8 collate utf8_general_ci"
        cu.execute(sql)
        sql1 = "use stu1993"
        sql2 = "create table ao(zhiwei char(25),nianx char(15))"
        cu.execute(sql1)
        cu.execute(sql2)
        sql4 = "insert into ao values ('技工',15)"
        cu.execute(sql4)
        connect.commit()

a=asd()
#a.qwe()
a.koo()
"""

# a="12345"
# #print(int(a))
# a1=a[::-1]
# a2=0
# for i,j in enumerate(a1):
#     #print(i,j)
#     for n in range(10):
#         if str(n)==j:
#             a2+=n*10**i
# print(a2)

#
#连接Linux下载
# import  paramiko
# class add(object):
#     def qwe(self):
#         d=paramiko.Transport(('192.168.10.27',22))
#         d.connect(username='root',password='123456')
#         sftp=paramiko.SFTPClient.from_transport(d)
#         x1 = '/home/zhaocf/fei.txt'
#         x2 = r'D:\daima/b.txt'  D:\untitled\b.txt
#         #sftp.get(x1,x2)    #下载
#         sftp.put(x2, x1)   #上传
#         d.close()
# q=add()
# q.qwe()

#判断回文
# a=input("请输入数字")
# b=len(a)
# m=0
# for i in range(b):
#     if a[i]==a[-(i+1)]:
#         pass
#     else:
#         m+=1
# if m==0:
#     print("是回文")
# else:
#     print("不是回文")

# a=input("请输入数字")
# b=a.split(" ")
# c=len(b)
# for i in range(c):
#     for j in range(c-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=int(b[j+1]),int(b[j])
# print(b)

# a=input("请输入数组")
# b=a.split(" ")
# c=len(b)
# for i in range(c):
#     for j in range(i+1,c):
#         if int(b[i]) >int(b[j]):
#             b[i],b[j]=b[j],b[i]
#
# print(b)

# import xlrd
# from xlutils.copy import copy
# #t=xlwt.Workbook()
# f = xlrd.open_workbook("23.xls")
# new = copy(f)
# table = new.add_sheet('3')
#
# #t1=t.add_sheet("表1")
# for i in range(1,10):
#     for j in range(1,i+1):
#         table.write(i-1,j-1,f"{j}x{i}={j*i}")
# new.save("23.xls")
# a=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         a+=i
# print(a)
#
# a="12345"
# b=a[::-1]
# c=0
# #print(b)
# for i,j in enumerate(b):
#     for n in range(1,10):
#         if str(n)==j:
#             c+=n*10**i
# print(c)

# import smtplib
# from email.mime.text import  MIMEText
# from email.header  import  Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# fwq='smtp.163.com'
# yhm='13592386651@163.com'
# mm='981007li'
# dkh=465
# # fsf='13592386651@163.com'
# jsf=['1778632232@qq.com']
# zt='python邮件'
# zw='你好，世界'
# nr=MIMEText(zw,'palin','utf-8')
# nr['From']=Header(yhm)
# nr['To']=Header(str(';'.join(yhm)))
# nr['Subject']=Header(zt)
# try:
#     a=smtplib.SMTP_SSL(host=fwq,port=dkh)
#     a.sendmail(yhm,jsf,nr.as_string())
#     a.login(user=yhm,password=mm)
#     a.quit()
#     print('发送成功')
# except smtplib.SMTPException as e:
#     print("error:",e)

# a=['python','shell']
# b={}
# for i,j in enumerate(a,10):
#     b[i]=j
# print(b)

# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("biao1")
# for i in range(1,10):
#     for j in range(1,i+1):
#         table.write(i-1,j-1,f"{j}x{i}={j*i}")
        # d.save('25.xls')


# f=open(file='a.txt',mode='w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write(f"{j}x{i}={j*i}\t")
#     f.write('\n')
# f.close()

# a=["python","shell"]
# b={}
# for i,j in enumerate(a,10):
#     b[i]=j
# print(b)

#将表中数据写入txt文件中
# import  xlrd
# class Excel(object):
#     def qwe(self):
#        d=xlrd.open_workbook(filename='73.xls')
#        d1=d.sheet_by_index(0)
#        r=[]
#        a=d1.nrows
#        for i in range(a):
#            r.append(d1.row_values(i))
#            #print(r)
#        return r
# class Txt(Excel):
#     def Write(self):
#         table = self.qwe()
#         f=open(file='aa.txt',mode='w',encoding='utf-8')
#         for i in table:
#             for j in i:
#                 f.write(f"{j}\t")
#             f.write("\n")
#         f.close()
#
# a=Txt()
# a.Write()

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
# a.asd("D:\daima")


# x=1
# while x<=4:
#     print('*'*x)
#     x+=1
# a=3
# while a>0:
#     print('*'*a)
#     a-=1

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end='')
#     print('')
# for i in range(1,4):
#     for j in range(i-1,3):
#         print('*',end='')
#     print('')

#用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# for i in range(50):
#     for j in range(100):
#         for n in range(100):
#             if i*2+j+n*0.5==100 and i+j+n==100:
#                 print(f"公鸡：{i} 母鸡：{j} 小鸡：{n}")

# def add(x2):
#     b=0
#     for i in range(2,x2):
#         for j in range(2,i+1):
#             if i%j==0:
#                break
#         if i==j:
#             b+=i
#     print(b)
# add(10099)


# def add(x):
#     a = 0
#     b = 1
#     for i in range(1, x):
#         b = b * i
#         a = a + b
#     print(a)
# add(6)

#去重并排序
# a=[1,2,3,4,23,32,32,4,4,5,54,45,45,54,]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b)

# while True:
#     a=int(input("第一条边"))
#     b=int(input("第二条边"))
#     c=int(input("第三条边"))
#     if a+b>c and a+c>b and b+c>a:
#         if a**2+b**2<c**2  or a**2+c**2 <b**2 or b**2+c**2<a**2:
#             print('钝角三角形')
#         elif a**2+b**2==c**2  or a**2+c**2==b**2 or b**2+c**2==a**2:
#             print('直角三角形')
#         elif  a**2+b**2>c**2  or a**2+c**2>b**2 or b**2+c**2>a**2:
#             print('锐角三角形')
#     elif a<0 or b<0 or  c<0:
#         break
#     else:
#         print('不是三角形')



# def asd(a1):
#     a2 = []
#     for i in a1:
#         for j in a1:
#             for n in a1:
#                 if i != j and j != n and i != n:
#                     a = i * 100 + j * 10 + n
#                     a2.append(a)
#     print(a2)
#     print(len(a2))
# asd([2,3,4,5])

#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
import random
a=random.randint(0,100)
#print(a)
b=[10,20,34,43]
b.append(a)
for i in range(len(b)):
    for j in range(len(b)-1):
        if b[j] >b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
print(b)
