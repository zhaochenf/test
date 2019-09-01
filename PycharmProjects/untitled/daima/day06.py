
"""
import pymysql
#第一步链接数据库
connect=pymysql.connect(
    host="192.168.10.34", #数据库所在的主机IP地址/域名（云服务器--mysql数据库）
    port=3306,   #mysql的端口号
    user="root",  #mysql的用户名
    password="123456",   #mysql 的用户密码（有授权的话输入远程授权密码）
    charset="utf8",  #mysql数据的编码方式
    #database="库名",   #指定数据库，不写这个参数，默认使用所有的数据库
)
cu=connect.cursor()   #游标 类似于mysql> 命令行模式

sql = "create database stu1903"
#执行sql语句
cu.execute(sql)
"""
"""
class add(object):
    def __init__(self,connect):
        import pymysql
        self.connect=pymysql.connect(
            host="192.168.10.34",
            port=3306,
            user="root",
            password="123456",
            charset="utf8",
            #database="库名",
        )
    def create_database(self,):
        cu=self.connect.cursor()
        sql="create database stu1903"
        cu.execute(sql)
    def create_table(self):
        cu1=self.connect.cursor()
        sql1="use stu1903"
        sql2="create table ad(name char(10))"
        cu1.execute(sql1)
        cu1.execute(sql2)
    def insert_info(self):
        cu2 = self.connect.cursor()
        sql3 = "use stu1903"
        sql4='''insert into ad values ("lisi")'''
        cu2.execute(sql3)
        cu2.execute(sql4)

    def create_tables(self):
        cu1=self.connect.cursor()
        sql1="use stu1903"
        sql2="create table msg(xvhao int(10),name char(10),xingbie char(10),age int(10),shengao int(10),country char(15))"
        cu1.execute(sql1)
        cu1.execute(sql2)
    def insert_infos(self):
        cu2 = self.connect.cursor()
        sql3 = "use stu1903"
        sql4='''insert into msg values ("5","akali","nv",17,175,"wukelan")'''
        cu2.execute(sql3)
        cu2.execute(sql4)
my=add("ac")
my.insert_infos()
"""
"""
class add(object):
    def __init__(self,connect):
        import pymysql
        self.connect=pymysql.connect(
            host="192.168.10.34",
            port=3306,
            user="root",
            password="123456",
            charset="utf8",
            #database="库名",
        )

    def create_database(self ):
        cu = self.connect.cursor()
        sql = "create database stu1904 default charset utf8 collate utf8_general_ci"
        cu.execute(sql)
    def create_tables(self):
        cu1=self.connect.cursor()
        sql1="use stu1904"
        sql2="create table msgs(name char(10),xingbie char(10),age int(10),shengao char(10),country char(15))"

        cu1.execute(sql1)
        cu1.execute(sql2)
    def insert_info(self):
        cu2 = self.connect.cursor()
        sql3 = "use stu1904"
        a=0
        for i in A:
            a = a + 1

            k=i[f"s_{str(a)}"]
            k.append(i["country"])
            c=tuple(k)
           # print(c)
            sql4=f"insert into msgs values {c}"
            cu2.execute(sql3)
            cu2.execute(sql4)

        #保存数据到数据库
            self.connect.commit()
    #查询
    def cha(self):
        #写查询sql
        sql="select*from msgs"
        cu2 = self.connect.cursor()
        sql4="use stu1904"
        #执行sql
        cu2.execute(sql4)
        cu2.execute(sql)
        #输出查询结果
        self.b=cu2.fetchall()#查询执行sql语句获得所有结果
        #fetchall() fetchmany()  fetchone() #返回的结果是一个元祖，包含若干个小元祖
        #print(b)
        #c=cu2.fetchmany(size=4) #查询指定条
        # c=cu2.fetchone()   #只查询一条
        # print(c)
        #print(a)
    #修改
    def close(self):
        #与数据库断开连接
        self.connect .close()
    #写入文件
    def wirtes(self):
        self.cha()
        f = open(file="b.txt", mode="w", encoding="utf-8")
        f.write(f"name\t    sex\t    age\t  shenggao\t  country\n")
        for i in self.b:
            for j in i:
                f.write(f"{j} \t")
            f.write("\n")
        f.close()



d = {
    "data": {
        "msg":
        [
            {
                "s_1": ["Jim", "男",  19, "175cm"],
                "country": "美国"
            },
            {
                "s_2": ["Kity", "女",  17, "165cm"],
                "country": "法国"
            },
            {
                "s_3": ["Tom", "男",  19, "173cm"],
                "country": "美国"
            },
            {
                "s_4": ["拖拉斯基", "男",  18, "180cm"],
                "country": "俄罗斯"
            },
            {
                "s_5": ["阿卡丽", "女",  17, "175cm"],
                "country": "乌克兰"
            },
            {
                "s_6": ["牙买稻子", "女",  18, "161cm"],
                "country": "日本"
            },
            {
                "s_7": ["龟田一郎", "男",  19, "175cm"],
                "country": "日本"
            },
            {
                "s_8": ["张三", "男",  20, "180cm"],
                "country": "中国"
            },
            {
                "s_9": ["李秀琴", "女",  19, "175cm"],
                "country": "中国"
            },
            {
                "s_10": ["宋仲基", "女",  19, "175cm"],
                "country": "韩国"
            },
            {
                "s_11": ["金正鞋", "男",  19, "168cm"],
                "country": "朝鲜"
            },
            {
                "s_12": ["卡列夫斯基", "男",  21, "190cm"],
                "country": "俄罗斯"
            },
        ]
    },
}



A=d["data"]["msg"]
my=add("ac")
#my.cha()
my.wirtes()
#my.close()
# my.create_database()
# my.create_tables()
# my.insert_info()
"""



#python 操作Excel表格

"""
1、python读取Excel表格中的数据--需要使用的第三方包：xlrd
"""
"""
import xlrd

#打开Excel文件
#open_workbook(filename=文件名）
d=xlrd.open_workbook(filename="data.xlsx")
#获取Excel,返回的是一个包含所有Excel的列表
#假设文件中存在两个Excel表，那么列表中['sheet1','sheet2']
table=d.sheets()[0]
#获取表中数据 row_values():  获取整行数据，必须指定获取的行号
x=table.row_values(0)
#print(table)
#print(x)

#获取某个单元格的值  先通过row（）获取某一行 ，返回一个列表，再通过列表的索引
#获取到元素，.value  获取到具体的值
dan=table.row(0)[0].value
print(dan)
#获取某一列的值    先通过col（） 获取某一列，返回一个列表，再通过列表的索引
#获取到元素，.value  获取到具体的值
asd=table.col(0)[1].value
print(asd)
#获取某一行某一列的值
add=table.cell(0,1).value
print(add)
#获取行数
qwe=table.nrows
print(qwe)
#获取列数
koo=table.ncols
print(koo)
#通过行数获取所有的数据
for i in range(qwe):
    print(table.row_values(i))
#通过列数获取所有的数据
c=table.col_values(1)  #获取整列的数据
print(c)
for i in range(koo):
    print(table.col_values(i))
#打印/输出Excel表的名字
#d 打开的Excel文件  sheet_names()  找出文件中所有表的名字
print(d.sheet_names())
#通过索引获取列表
#假设一个文件中存在两个表 sheet1  sheet2 ，sheet_by_index(): 0 打开的是sheet1
table1=d.sheet_by_index(0)
print(table1)
"""
"""
import xlrd
class Excel(object):
    def __init__(self,name,num):
        #第一步代开文件
        self.d=xlrd.open_workbook(filename=name)
        #使用一张表
        self.t=self.d.sheet_by_index(num)
    #data 方法的作用，获取一张表中的所有数据
    def data(self):
        #将所有数据装到一个列表中

        r=[]
        n=self.t.nrows
        for i in range(n):
            #print(self.t.row_values(i))
            r.append(self.t.row_values(i))
        return r


dui=Excel("data.xlsx",1)
print(dui.data())
"""

#将表中数据写入txt文件中

# class Excel(object):
#     def __init__(self,name,num):
#         import xlrd
#         self.d=xlrd.open_workbook(filename=name)
#         self.t=self.d.sheet_by_index(num)
#     def data(self):
#         r=[]
#         n=self.t.nrows
#         for i in range(n):
#             #print(self.t.row_values(i))
#             r.append(self.t.row_values(i))
#         return r
# class Txt(Excel):
#     def wirtes(self):
#         f = open(file="a.txt", mode="w", encoding="utf-8")
#         shujv = self.data()
#         for i in shujv:
#             for j in i:
#                 #f.write(f"{j} \t")
#                 f.write(f"{str(j)} \t")
#             f.write("\n")
# #t1=Txt('26.xls',0)
# t1=Txt('data.xlsx',0)
# t1.wirtes()


"""
#python  向Excel文件中写入数据  pip install xlwt

import  xlwt
#新建一个Excel文件
d=xlwt.Workbook()
#新建一个Excel表  add_sheet（工作表的名字）必填
table=d.add_sheet("表一")
#写入数据到Excel表中
#一次写入一个单元格
table.write(0,0,"张三")
#保存文件  save("文件名") 必填
d.save("73.xls")
"""
#导入其他文件脚本
# 1、from 文件夹名字  import  脚本名
#  脚本名.XX-->所有代码
#2、from 文件名.脚本名 import  所有代码
#   变量名
#   函数
#   类
#   导用本脚本
#3、from 文件名.脚本名 import *



#插入数据到表中
"""
import  xlwt
a=[["序号","姓名","年龄","性别"],
   [1,"李四",23,"男"],[2,"王六",19,"男"],[3,"张思",20,"女"],[4,"赵华",18,"女"]]
d=xlwt.Workbook()
table=d.add_sheet("表一")
for i in range(len(a)):
    for j in range(len(a[i])):
        table.write(i,j,a[i][j])
d.save("72.xls")
"""
"""
import xlwt
class Txt(object):
    d = xlwt.Workbook()
    def __init__(self,biao,shujv):
        self.table = self.d.add_sheet("表")
        self.biao=biao
        self.shujv=shujv
    def foo(self):
        for i in range(len(self.shujv)):
            for j in range(len(self.shujv)-1):
                self.table.write(i, j, self.shujv[i][j])
        self.d.save(self.biao)
a= Txt("23.xls",[["序号","姓名","年龄","性别"],
   [1,"李四",23,"男"],[2,"王六",19,"男"],[3,"张思",20,"女"],[4,"赵华",18,"女"]])
# a=Txt("23.xls",[["序号","姓名","年龄","性别"],[5,"木森",24,"男"],
#                 [6,"扎黑",21,"男"],[7,"道",20,"男"]])
a.foo()

"""

import xlrd
import xlwt
a=([2,"textadmin","textpassword"])
class add(object):
    def __init__(self):
        self.d = xlrd.open_workbook(filename="24.xls")
        self.t = self.d.sheet_by_index(0)
    def date(self):
        print(self.t.row_values(1))
        return self.t.row_values(1)
    def qwe(self):
        self.d = xlwt.Workbook()
        table = self.d.add_sheet("sheet1")
        for i in range(len(a)):
            table.write(1,i,a[i])
        self.d.save("24.xls")
b=add()
b.qwe()


#99乘法表写入表格
"""
import  xlwt
class add(object):
    def __init__(self):
        self.d = xlwt.Workbook()
        self.table = self.d.add_sheet("sheet1")
    def qwe(self):
        for i in range(1,10):
            for j in range(1,i+1):
                self.table.write(i-1,j-1,f"{j}x{i}={j*i}")
        self.d.save("26.xls")
a=add()
a.qwe()
"""
"""
class add(object):
    def qwe(self):
        f = open(file="b.txt", mode="w", encoding="utf-8")
        for i in range(1,10):
            for j in range(1,i+1):
                f.write(f"{j}x{i}={j*i}\t")
            f.write("\n")
        f.close()
a=add()
a.qwe()
"""
"""
# 使用python 远程操作Linux系统
#需要的模块：paramiko    pip install paramiko

import paramiko

#第一步，连接Linux系统

#第二种链接liunx的方式  使用ssh
# 建立连接第一步，创造一个sshclient对象
s=paramiko.SSHClient()
#建立连接第二步，允许信任liunx主机,类似xshell第一次连接的保存信息
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#建立连接第三步，使用connect（）连接远程Liunx主机
s.connect(
    hostname='192.168.10.35',
    port=22,
    username='root',
    password='123456'
)

#第二步，执行liunx命令
#exec_command('需要执行的命令')：执行命令的方法，命令要写成字符串类型
# x=s.exec_command('ls -al')
# print(x)
#输入  输出   错误   decode(解码）
stdin,stdout,stderr=s.exec_command('ls -al')   #三个变量名字可以随便写
print(stdout.read().decode())

#第三步：文件上传、下载
#SFTPClient()  ： sftp客户端方法，参数：指的是我们之前建立的连接 s

#第二种链接liunx的方式 使用端口号链接 22
#套字节编程（网络编程）
#Transport(参数)：端口号链接liunx系统， 参数：包含ip地址、端口号的元组
t=paramiko.Transport(('192.168.10.35',22))
t.connect(username='root',password='123456')
#SFTPClient.from_transport(参数)：sftp客户端方法
#参数：指的是一个套字节服务端口 t
sftp=paramiko.SFTPClient.from_transport(t)  #创建一个文件传输通道

x1='/home/zhaocf/fei.txt' #liunx 远程文件位置
x2=r'D:\daima/b.txt'   #保存本地位置
#get(远程文件、本地文件）：下载
#sftp.get(x1,x2)

#put(本地文件、远程文件)：上传文件
sftp.put(x2,x1)

#关闭连接、断开连接
# t.close()
# s.close()
"""

"""
import paramiko
class add(object):
    def __init__(self):
        self.t=paramiko.Transport(('192.168.10.4',22))
        self.t.connect(username='root', password='123456')
    def qwe(self):
        x = self.t.exec_command('ls -al')
        print(x)
        # stdin, stdout, stderr = self.t.exec_command('ls -al')
        # print(stdout.read().decode())
    def koo(self,x1,x2):
        sftp = paramiko.SFTPClient.from_transport(self.t)
        x1 = '/home/zhaocf/fei.txt'
        x2 = r'D:\daima/b.txt'
        self.sftp.get(x1, x2)
a=add()
a.qwe()
"""

"""
import paramiko
class linux_1(object):
    def __init__(self,a1,a2,a3,a4):
        self.b1 = paramiko.Transport((a1,a2))
        self.b1.connect(username=a3,password=a4)
    def linux_2(self):
        stdin,stdout,stderr = self.b1.exec_command('ls -al')
        print(stdout.read().decode())
        self.b1.close()
    # def linux_3(self,b3,b4):
    #     b2 = paramiko.SFTPClient.from_transport(self.b1)
    #     b2.get(b3,b4)
    #     self.b1.close()
cx = linux_1("192.168.10.4",22,"root","123456")
cx.linux_2()
"""

"""
import paramiko
class As(object):
    t = paramiko.Transport("192.168.10.22", 22)
    d=t.connect(username="root", password="123456")
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def sd(self):
        sftp = paramiko.SFTPClient.from_transport(self.t)
        x1 = self.name1      # linux远程文件
        x2 = self.name2
        sftp.get(x1,x2)
        self.t.close()

a = As("/home/zhaocf/fei.txt",r"D:\daima/c.txt")
a.sd()
"""

"""
#python 与系统的交互
#系统包括：windows  、mac 、Unix
#python的内置模块-->python 自带的、下载时包含的
#os

import os

#获取当前目录——>liunx: pwd ; os.get()
a=os.getcwd()
print(a)

#切换到指定目录：os.chdir(目录名字）
os.chdir('A')
b=os.getcwd()
print(b)

#返回上一级目录： os.curdir(目录名字）
os.chdir('A')
b=os.getcwd()
print(b)
#当前目录：os.curdir 代表的是'.'
os.curdir(os.curdir)
c=os.getcwd()
print(c)
#上一级目录: os.pardir 代表的是'..'
os.chdir(os.pardir)
c=os.getcwd()
print(c)

#获取操作系统类型  os.name
#nt 是windows
n=os.name
print(n)

#创建多级目录
#os.makedirs('AAA/BBB/CCC')
#创建一个目录
#os.mkdir("tas")
#删除 多个目录  :只删除空目录
#os.removedirs("AAA/BBB/CCC")
#删除单个目录：只删除空目录
#os.rmdir("AA")
#查看当前路径下所有的文件、目录、包括隐藏文件 类似：ls -al   返回一个列表
#res=os.listdir('D:/daima/B')
#print(res)
#对文件、目录进行重命名
#os.rename('D:/daima/B','D:/daima/Bb')
#删除文件
#os.remove('D:/daima/c.txt')
#执行系统命令
k=os.popen('ls -al')
print(k.read())
#目录树-->类似于tree
for root,dirs,files in os.walk(r'D:\daima'):
    print(dirs)
v=os.walk(r'D:\daima')
print(v)
"""
"""
#os.path 类   对文件的操作
import os

#1、返回文件的绝对路径
#abspath(文件名)
b = os.path.abspath('c.txt')
print(b)
#2、返回文件的上一级目录名
c=os.path.dirname(r'D:\daima\day01.py')
print(c)
#3、返回当前文件的文件名
d=os.path.basename('D:\daima\day02.py')
print(d)
#4、判断文件是否存在-->返回布尔值
e=os.path.exists('D:\daima\day02.py')
print(e)
#5、判断是否为目录
f=os.path.isdir('A')
print(f)
#6、判断是否为文件
g=os.path.isfile('73.xls')
print(g)
#7、判断是否为链接文件
h=os.path.islink('asd')
print(h)
#8、文件路径拼接
i=os.path.join('b.txt','a.txt')
print(i)
#9、文件路径分离  将前一个文件/目录与最后一个进行分割，返回一个元组
l=os.path.split(r'D:\daima\day02.py')
print(l)
#10、分割文件的后缀名  返回一个元组
j=os.path.splitext('D:\daima\day02.py')
print(j)

#统计当前目录下有多少个文件、目录
class qwe(object):
    def asd(self,dir):
        res=os.listdir(dir)
        sum=0
        sum1=0
        for i in res:
            if os.path.isdir(i):
                sum+=1
            elif os.path.isfile(i):
                sum1+=1
        print(f"目录文件：{sum}个，文件：{sum1}个")
c=qwe()
c.asd('D:\daima')

class A(object):
    res = os.listdir('D:\daima')
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def count(self):
        for i in self.res:
            if os.path.isdir(i):
                self.x+=1
            elif os.path.isfile(i):
                self.y+=1
        return self.x,self.y
a=A(0,0)
print(a.count())

"""
"""
# python 对时间的操作
#time
#https://docs.python.org/zh-cn/3/library/time.html


import time

#1、睡眠  sleep(数)    浮点数、整数 单位秒
print("睡眠之前")
#time.sleep(0.5)
print("睡眠之后")
# 2、cpu运算代码的时间
#print(time.clock())
#3、当前时间
print(time.ctime())
print(time.asctime())
#4、输出时间的详细信息
print(time.localtime())
#5、格式化输出时间
print(time.strftime("%A %d %B %H:%M:%S" ))
#6、根据格式解析表示时间的字符串
print(time.strptime("30 Nov 00","%d %b %y"))
#7、距离计算机元年过去的秒的总和
print(time.time())

"""

#python 对日期的操作
#datetime
"""
#import  datetime
from datetime import datetime,date,timedelta

#1、获取当前时间、riqi
print(datetime.now())
#2、获取指定的时间、日期
print(datetime(1994,5,15,12,1,1))
#3、字符串时间转datetime的日期
t=datetime.strptime('1994-05-15 12:01:01','%Y-%m-%d %H:%M:%S')
print(t)
#4、日期转字符串
s=datetime.now().strftime('%A %d %B %H:%M:%S')
print(s)
#5、日期的加减
now=datetime.now()
q=now+timedelta(days=5)  #days= 天   hours= 小时
print(q)
#6、获取当前日期
print(date.today())
#print(date(1994,5,15).ctime())
#7、对日期进行加减
f=date.today()-timedelta(days=1)
print(f)
"""

