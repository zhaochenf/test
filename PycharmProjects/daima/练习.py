# -*- coding: utf-8 -*-
# 水仙花100~1000
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if i==a**3 + b**3 + c**3:
#         print(i)
#1000之内的因数和等于本身
# for i in range(1,1001):
#     n=0
#     for j in range(1,i):
#         if i%j==0:
#             n +=j
#     if n==i:
#         print(i)
# 判断几位数并倒着显示
# A=int(input("请输入一个数"))
# a=A//10000
# b=A%10000//1000
# c=A%1000//100
# d=A%100//10
# e=A%10
# if a!=0:
#     print("5位数",e,d,c,b,a)
# elif b!=0:
#     print("4位数",e,d,c,b)
# elif c!=0:
#     print("3位数",e,d,c)
#1~100的和
# tmp=0
# for i in  range(1,101):
#     tmp=tmp+i
# print(tmp)

# print(sum(range(1,101)))


# i=0
# j=0
# while i<100:
#     i=i+1
#     j=i+j
# print(j)

# print(sum(range(1,101)))
#判断输入的字符串是否是回文？
# a=input("请输入数字")
# x=len(a)
# m=0
# for i in range(x):
#     if a[i]==a[-(i+1)]:
#         pass
#     else:
#         m=m+1
# if m==0:
#     print("是回文")
# else:
#     print("不是回文")


#1`100的质数和
# b=0
# for i in range(2,101):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         b+=i
# print(b)

# b=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         b=b+i
# print(b)


#显示1~100之间的质数
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#




#阶乘之和
# a=0
# for i in range(1,6):
#     b=1
#     for j in range(1,i+1):
#         b=b*j
#     a=a+b
# print(a)

# a=0
# b=1
# for i in range(1,6):
#     b=b*i
#     a=a+b
# print(a)


#99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={j*i}\t",end="")
#     print()

#例：python 使用input(),输入一段英文，每个英文单词以空格分割，求最后一个单词长度
# a=input("请输入一段英文")
# s=a.split(" ")
# print(f"最后一个单词长度：{len(s[-1])}")

#使用input（)输入一段话，将字符串转换为列表，判断列表中的元素有多少个是数字、首字符大写,求出相应个数
# a=input("请输入一段话")
# c=a.split(" ")
# print(c)
# # b=list(c)
# b1=len(c)
# num=0
# num1=0
# for i in range(b1):
#     if c[i].isdigit():
#         num+=1
#     elif c[i].istitle():
#         num1+=1
# print(f"数字个数{num}")
# print(f"首字母大写个数{num1}")


# if __name__ == '__main__':
#     a = []
#     for i in range(10):
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     for i in range(10):
#         a[i][0] = 1
#         a[i][i] = 1
#     for i in range(2,10):
#         for j in range(1,i):
#             a[i][j] = a[i - 1][j-1] + a[i - 1][j]
#     from sys import stdout
#     for i in range(10):
#         for j in range(i + 1):
#             stdout.write(str(a[i][j]))
#             stdout.write(' ')
#         print()

 #商品、价格 、总价
# a=input("输入购买商品名称")
# c=int(input("输入购买商品个数"))
# ad=["方便面","火腿","矿泉水","笔记本"]
# ad1=[100,50,20,15]
# for i,j in enumerate(ad):
#     if a==j :
#         k=c*ad1[i]
#         print(k)

# a = input("输入商品名")
# b = input("购买数量")
# i = ['方便面','矿泉水']
# j = [100,200]
# for m,n in enumerate(i):
#     print(m,n)
#     if n == a:
#         zongjia = j[m] * int(b)
#         print(f"商品名:{a},数量:{b},单价:{j[m]},总价:{zongjia}")
#         break
# else:
#     print("商品不存在")

# 多种商品价格
# a = input("请输入你购买的商品名：")
# n = input("请输入购买量：")
# b = ["矿泉水","方便面","面包","辣条","西瓜"]
# c = [3,5,10,4,30]
# x = a.split()
# y = n.split()
# h = 0
# for o in range(0, len(x)):
#     e = 0
#     d = 0
#     for k, l in enumerate(list(b)):
#         if x[o] == l:
#             print(f"{l}  商品单价：{c[k]}  购买数量：{y[o]}")
#             e = int(c[k]) * int(y[o]) + e
#         else:
#             d = d + 1
#     h = e + h
#     if x[o] != l and d == 5:
#         print(f"{x[o]}:此商品无货")
# print(f"总价{h}")


#冒泡排序
# a1=input(f"请输入数字")
# a=a1.split()
# b=len(a)
# for i in range(b):
#     for j in range(b-1):
#         if int(a[j]) > int(a[j+1]):
#             a[j],a[j+1]=int(a[j+1]),int(a[j])
# print(a)

#选择排序

# a = input("输入一串数")
# c = a.split()
# #print(c)
# d = len(c)
# # print(d)
# for i in range(d):
#    # j = i + 1
#     for j in range(i+1,d):
#         if int(c[i]) > int(c[j]):
#             # m = c[i]
#             # c[i] = c[j]
#             # c[j] = m
#             c[i],c[j] = int(c[j]),int(c[i])  #这是另一种
#
# print(c)





# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
# 第10次反弹多高？
# a=100
# b=100
# c=0
# for i in range(1,11):
#     a=a+c
#     b=b/2
#     c=b*2
# print(f"第10次反弹高度{b}")
# print(f"第10次落地时共经过{a}")



#去除列表中重复的元素
#a=[1,2,3,4,4,3,4,4,4] #输出成[1,2,3,4] 顺序无所谓
#print(list(set(a)))
# for i in a:
#     if a.count(i)>=2:
#         a.remove(i)
#     print(a)

# b=dict.fromkeys(a)
# print(b)
# c=[]
# for i in b:
#     print(i)
#     c.append(i)
# print(c)

# a = [1, 2, 2, 3, 4, 3, 4, 4]
# for i in  a:
#     b=a.count(i)
#     for n in range(b-1):
#         if  b>1:
#             a.remove(i)
# print(a)

# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#输入两字符串，将字符串转列表，第一个列表元素作为字典键，第二个列表元素作为字典的值
#加入key个数多余值个数--->无值设为None
#key个数少于值时
# a=input("请输入字符串1")
# b=input("请输入字符串2")
# c=a.split(" ")
# d=b.split(" ")
# c1=len(c)
# d1=len(d)
# f={}
# if c1==d1:
#     for i in range(c1):
#         f[c[i]]=d[i]
# print(f)
# if c1>d1:
#     for i in range(c1):
#         if i <= d1-1:
#             f[c[i]]=d[i]
#         else:
#             f[c[i]]="None"
#     print(f)
# elif c1<d1:
#     for i in range(d1):
#         if i>=c1:
#             f["bowen"]=d[i]
#         else:
#             f[c[i]]=d[i]
#     print(f)
#


# s = {
#     "key1": [1000, 2000, 3000],
#     2019: [
#         "hello",
#         {"python": ['py2.x', 'py3.x']},
#     ],
# }

# 1、求 key1 对应value的和
# 2、求 python 对应的值，并将每个版本的首字符大写、尾字符大写输出

# b=s["key1"]
# a=0
# for i in b:
#     a+=i
# print(a)
#
# value=s.get(2019)
# print(value)
# c=value[1]
# print(c)
# c1=c["python"]
# print(c1)
# g=str(c1).title()
# print(g)
# c=g[-1]
# for j in g:
#     d=g.replace(c,c.upper())
# print(d)

#如何实现[‘1’,’2’,’3’]变成[1,2,3] ?
# a=['1','2','3']
# b=[int(i) for i in a]
# print(b)





#s = '[Description("衣物挑战5kg")]@        /medal/201906/24/Cloth_Single_5.png         @        /medal/201906/24/Cloth_Single_5_Get.png     @            [Description("衣物挑战10kg")]@        /medal/201906/24/Cloth_Single_10.png        @        /medal/201906/24/Cloth_Single_10_Get.png    @            [Description("衣物挑战15kg")]@        /medal/201906/24/Cloth_Single_15.png       @        /medal/201906/24/Cloth_Single_15_Get.png   @            [Description("衣物挑战20kg")]@        /medal/201906/24/Cloth_Single_20.png       @        /medal/201906/24/Cloth_Single_20_Get.png    @           [Description("衣物挑战25kg以上")]@        /medal/201906/24/Cloth_Single_25.png        @        /medal/201906/24/Cloth_Single_25_Get.png   @            [Description("衣物累计50kg")]@        /medal/201906/24/Cloth_Sum_50.png           @        /medal/201906/24/Cloth_Sum_50_Get.png'

# 题目要求
# 将类似/medal/201906/24/Cloth_Single_5.png的放到一个列表内
# 将类似/medal/201906/24/Cloth_Single_5_Get.png的放到一个列表内
# g=s.split()
# a=[]
# b=[]
# # print(g)
# for i in g:
#     if i.find("Get.png") !=-1:
#         a.append(i)
#     elif i.find("png") !=-1:
#         b.append(i)
# print(a)
# print(len(a))
# print(b)
# print(len(b))

# 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，
# 9*??的结果为3位数。求??代表的两位数，及809*??后的结果

# a=809
# for i in range(10,100):
#     b=a*i
#     if b>=1000 and b<=10000 and 8*i<100 and 9*i>=100:
#         a=eval("b = 800*i + 9*i")
#         print(a)
#         print(b, ' = 800 * ', i, ' + 9 * ', i)

# a = 809
# for i in range(10,100):
#     b = i * a
#     if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
#         print(b,' = 800 * ',i, ' + 9 * ',i)

#用户10个随机数，0~1000之间，出现重复的只保留一个
# import random
# b=set()
# for i in range(10):
#     a = random.randint(0, 1000)  #随机生成一个整数
#     b.add(a)
# print(b)

#数字1,2,3,4能组成多少个不重复的百位数（个十百不同）
# a=[]
# c=0
# for i in range(1,5):
#     for j in range(1,5):
#         for n in range(1,5):
#             if i!=j and j!=n and i!=n:
#                 b=i*100+j*10+n
#                 a.append(b)
#                 c+=1
# print(a)
# print(c)

#输入一个数判断奇偶
# A=int(input("请输入一个数"))
# if A>0:
#     if A%2==0:
#         print("A为偶数")
#     elif A%2 !=0:
#         print("A为奇数")
# else:
#     print("输入的数为0或小于0")

#山峰8843米，一张纸厚度0.08mm,折多少次高度超过8843米（1m=1000mm)
# a=0.00008
# b=8843
# m=0
# while True:
#     if a>=b:
#         break
#     else:
#         a=a*2
#         m+=1
# print(a)
# print(m)

# while a<b:
#     a=a*2
#     m+=1
#     print(a)
# print(m)



#0~100内奇数减偶数的值
# sum=0
# for i in range(0,101):
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
# print(sum)

# bin()  # 二进制
# oct()  # 八进制
# hex()  # 十六进制

#把a里面的数转换成二进制数
# a=[12,23,10,8]
# for i in a:
#     print(i,":",bin(i))

#li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# a.请输出"Kelly"
# b.请使用索引找到 'all'元素并将其修改为"ALL"
# s=li[2][1][1]
# print(s)
#
# a=li[2].index("all")
# li[2][a]="ALL"   #a是一个索引值
# print(li)


#将列表 li=["alex","seven"] 转换成字典且字典的 key 按照 10 开始向后递增
# li=["alex","seven"]
# li_dic = {}
# for k,v in enumerate(li,10):
#    # print(k,v)
#     li_dic[k] = v
# print(li_dic)

#s="12345",不使用int方法，将s转成 s=12345  (考试题）

# s="123452"
# a=0
# b=s[::-1]  #反转
# for i,j in enumerate(b):
#     print(i,j)
#     for n in range(10):
#         if j==str(n):
#             a+=n*(10**i)
# print(a)
#
# a=eval("12345")
# print(a)

# a=input("请输入数字")
# b=0
# while True:
#     b=b+1
#     if str(b)==a:
#         print(a)
#         break
# #
#
#

"""
Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried "Why did you abandon me? I'm going to die any minute. How could you do this to me?"
"""

# 统计字符串长度大于5的
# 将e全部替换成博文
# 截取第一个逗号前的所有单词，并将首字符大写
# 删除除包含英文o的单词
#a="""Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried "Why did you abandon me? I'm going to die any minute. How could you do this to me?" """
# b=a.split()
# c=[]
# for i in b:
#     if len(i)>5:
#         c.append(i)
# print(c)

# print(a.replace("e","博文"))

# b=a.split(",")
# print(b[0].title())

# b=a.split(" ")
# d = []
# for i in range(len(b)):
#     if "o" in b[i]:
#         d.append(b[i])
# print(d)
"""
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
"""
# 求国家个数
# 求所有学生的身高范围
# 求统计男女比例
# 求平均身高
# 查询身高在170到180之间的学生名字
#1、
# print(d["data"])
# a=d["data"]
# b=a["msg"]
# c=set()
# for i in b:
#     a=i["country"]
#     c.add(a)
# print(len(c))

#2、
# a=d["data"]
# b=a["msg"]
# a1=[]
# i=0
# for j in b:
#     i+=1
#     c=j[f"s_{i}"]
#     c1=c[3]
#     a1.append(c1)
# a1.sort()
# print(f"身高范围：{a1[0]}--{a1[-1]}")
#
# e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][-1])
# e.sort()
# print(f"身高范围{e[0]}-{e[-1]}")

#3、
# e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][1])
# # print(e)
# m = e.count("男") .e.count("女")
# print(f"男女比列{m}")

# a=d["data"]
# b=a["msg"]
# a1=[]
# i=0
# for j in b:
#     i+=1
#     c=j[f"s_{i}"]
#     c1=c[1]
#     a1.append(c1)
# m=a1.count("男")/a1.count("女")
# print(m)
#4、
# a=d["data"]
# b=a["msg"]
# a1=[]
# i=0
# for j in b:
#     i+=1
#     c=j[f"s_{i}"]
#     c1=c[-1]
#     a1.append(c1)
# m=0
# for n in a1:
#     m=int(n.replace("cm"," ")) +m
#     g=m / len(a1)
# print(g)
#
#5、

# a=d["data"]
# b=a["msg"]
# a1=[]
# i=0
# for j in b:
#     i+=1
#     c=j[f"s_{i}"]
#     c1=c[-1]
#     if 170<=int(c1.replace("cm"," ")) <=180:
#         print(c[0],c[-1])

# 设计一个商场的销售、会员充值系统
# 1、展示在售商品，包含商品名、价格、库存量
# 2、用户根据商品编号选择商品、输入购买数量
# 3、结账功能，用户不 是会员按照原价结算、是会员按照会员等级进行打折
# 4、使用会员时，判断是否是会员，是会员展示帐户余额，会员帐户默认金额1000，计算帐户剩余金额
# 5、用户输入X或x结束操作

"""
m=["面包","方便面","矿泉书","牛奶","水杯"]
t=["1","2","3","4","5"]
n=[10,15,5,14,12]
w=[130,200,300,150,50]
hy=[12345,23456,34567]
v=[1000,]
print(f"商品\t   编号\t  单价\t   库存")
for a in range(0,5):
    print(f"{m[a]}\t\t{t[a]}\t\t{n[a]}\t\t{w[a]}")
while True:
    b = input(f"是否购买商品(y/no):")
    if b=="no":
        print("您已退出")
        break
    elif b=="y":
        c=int(input("请输入购买商品编号"))
        if c<0 or c>6:
            o=int(input("您所购买的商品不存在,请重新输入："))
        d=int(input("请输入购买数量"))
        if w[c - 1] < d:
            z=input("亲，库存不足，请重新输入购买数量：")
        a1=input("结账，您是否为会员(y/no)")
        if a1=="y":
            s=int(input(f"请输入会员号"))
            sn=0
            while s not in hy:
                g=input("账号错误，重新输入,输入超过5次，退出")
                sn+=1
                if sn==5:
                    break
            while s in hy:
                print("您是会员,八折优惠")
                k=0.8*d*n[c-1]
                if v[0]<k:
                    print("您的金额不足，请充值，充值请输yes，不充值输no")
                    czh = input("请选择是否充值")
                    if czh == "yes":
                        print("亲，请输入充值金额")
                        chje = int(input("请输入充值金额"))
                        v[0] = v[0] + chje
                        print(f"充值成功，请稍等,本次充值金额{chje}￥，余额总计{v[0]}")
                    else:
                        print("无法购买，请保证金额充足")
                        break
                else:
                    print("金额充足")
                print(f"您购买的商品编号为{c},数量为{d},消费金额{k},余额为{v[0]-0.8*d*n[c-1]},剩余库存{w[c-1]-d}")
                break
        elif a1!="y":
            print("您不是会员")
            k = d * n[c - 1]
            if v[0] < k:
                print("您的金额不足，请充值,充值请输yes，不充值输no")
                czh=input("请选择是否充值")
                if czh=="yes":
                    print("亲，请输入充值金额")
                    chje=int(input("请输入充值金额"))
                    v[0]=v[0]+chje
                    print(f"充值成功,请稍等,本次充值金额{chje}￥，余额总计{v[0]}")
                else:
                    print("无法购买，请保证金额充足")
            else:
                print("金额充足")
            print(f"您购买的商品编号为{c},数量为{d},消费金额{ k},余额为{v[0]-d*n[c-1]},剩余库存{w[c-1]-d}")


# print(f"{j}x{i}={j * i}\t", end="")

"""

#函数形式的

# def add(a):
#     b=a.split(",")
#     c=len(b)
#     for i in range(c):
#         for j in range(c-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1]=b[j+1],b[j]
#     print(b)
#
# add("123,32,9,234")

#冒泡
# def add(a):
#     b=a.split(",")
#     c=len(b)
#     for n in range(c):
#         b[n]=int(b[n])
#     for i in range(c):
#         for j in range(c-1):
#             if b[j] > b[j + 1]:
#                 b[j], b[j + 1] = b[j + 1], b[j]
#     print(b)
#add("1234,32,76,10")


#选择
# def a(*args):   #以元祖形式
#     b = list(args)
#     for i in range(len(b)):
#         for j in range(i+1,len(b)):
#             if int(b[i]) > int(b[j]):
#                 b[i],b[j] = b[j],b[i]
#     print(b)
#     return b
# print(a(123,321,34,9))


#批量验证用户账号和用户密码是否符合要求的脚本

# def k(a,b):
#     a1=len(a)
#     c=[]
#     d=[]
#     if len(a)<len(b):
#         m=len(a)
#     else:
#         m=len(b)
#     for i in range(m):
#         if len(a[i])>5 and len(a[i])<8:
#             if len(b[i])>6 and len(b[i])<9:
#                 c.append(a[i])
#                 d.append(b[i])
#     return c,d
# a1=input("输入字符串1")
# b1=input("输入字符串2")
# a=a1.split()
# b=b1.split()
#
# # a=["asd","qwsasq","jdncnc","ncwnhdoihc"]
# # b=["knkwk","123qqqq","nwndow12","ankknka"]
# k1=k(a,b)
# print(f"符合条件的有{len(k1[0])}个")
# for j in range(len(k1[0])):
#     print(f"符合的用户为{k1[0][j]},密码为{k1[1][j]}")


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

# class qwe(object):
#     def add(self):
#         a=0
#         b=1
#         for i in range(1,6):
#             b=b*i
#             a=a+b
#         print(a)
# a=qwe()
# a.add()


# def add(x):
#     a = 0
#     b = 1
#     for i in range(1, x):
#         b = b * i
#         a = a + b
#     print(a)
# add(9)


# class add(object):
#     def ac(self):
#         b=0
#         for m in range(1,101):
#             b=m+b
#         print(b)
# s=add()
# s.ac()


# class add(object):
#     def a(self):
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 print(f"{j}x{i}={j * i}\t", end="")
#             print()
# s=add()
# s.a()

# class add(object):
#     def a(self):
#         b=0
#         for i in range(2,101):
#             for j in range(2,i+1):
#                 if i%j==0:
#                     break
#             if i == j:
#                 b += i
#         print(b)
# s=add()
# s.a()

# class add(object):
#     def a(self):
#         b=0
#         for i in range(1,101):
#             c=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     c+=1
#             if c== 2:
#                 b += i
#                 print(b)
#         print(b)
# s=add()
# s.a()

# class add(object):
#     def __init__(self,n,m):
#         self.n=n
#         self.m=m
#     def sum(self):
#         c=self.n+self.m
#         print(c)
#         a=lambda n,m:(n+m)*m
#         return a
#         print(a)
# d=add(4,5)
# print(d.sum())




# class add(object):
#     def __init__(self,name):
#         self.name=name
#     def read(self):
#         f=open(file=self.name,encoding="utf-8")
#         text=f.read()
#         print(text)
# b=add('a.txt')
# b.read()

#将hello python shell 反着输出 shell python hello
# a='hello python shell'
# b=a.split()
# print(b[::-1])
# c=" ".join(b[::-1])
# print(c)

# 判断字母t的索引值
# name = " gouguotQ"
# v = len(name)
# for n in range(v):
#     if (name[n]) != "t":
#         continue
#     else:
#         print (n,name[n])

#print("hello, python")
# a = "hello"
# b = "python"
# print(a+',',b)

#连接linux
"""
import paramiko
class asd(object):
    s=paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    def __init__(self):
        self.s.connect(
            hostname='192.168.10.11',
            port=22,
            username='root',
            password='123456'
        )
    def qwe(self):
        stdin, stdout, stderr = self.s.exec_command('ls -al')
        a=stdout.read().decode()
        #print(a)
        return a
q=asd()
print(q.qwe())
"""

#连接数据库

"""
# python发送电子邮件
# 使用到的模块：smtplib      email
import smtplib
from email.mime.text import  MIMEText
from email.header  import  Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
# 设置服务器所需要的信息
# 邮件的服务的地址
mail_host="smtp.163.com"
# 用户名
muser= "13592386651@163.com"
# 客户端授权码或者密码
mail_pass = "981007li"
# 设置服务器端口号
mail_port=465
# 邮件发送方地址
send='13592386651@163.com'
# 邮件接收方地址
receivres=['1778632232@qq.com']  #可以写多个


# 设置邮件信息如下
# 设置邮件主题
subject = "python测试"
# # 设置邮件正文
# a = "这是我发送的邮件"
# # 三个参数：第一个为文本内容，第二个plain 设置文本格式，第三个： utf-8 设置编码
# message = MIMEText(a,'plain','utf-8')
#
# # 发送邮件时填写收件人，发件人，主题
# # Header():填写邮件的头部
# # 发送方信息
# message['From'] = Header(send)
# # 接收方信息
# message['To'] = Header(str(";".join(receivres)))
# # 主题绑定
# message['Subject'] = Header(subject)
#
# # 登录并发送邮件
# try:
#     #第一步：登录邮箱
#         #第一种：不使用授权码
#     # s1=smtplib.SMTP()
#         #   连接到服务器
#     # s1.connect(mail_host,25)
#     # 第二种：使用授权码
#     smtpObj =smtplib.SMTP_SSL(host=mail_host,port=mail_port)
#     #登录服务器:输入用户名，密码
#     smtpObj.login(user=muser,password=mail_pass)
#     #发送    as_string（）  ：以字符串的形式发送出去
#     smtpObj.sendmail(send,receivres,message.as_string())
#     #退出
#     smtpObj.quit()
#     print("发送成功")
# except smtplib.SMTPException as e:
#     print("error:",e)  # 打印错误

# 添加一个MIMEMultipart(),处理正文和机附件，添加到邮件里
message = MIMEMultipart()
# 发送方信息
message['From'] = Header(send)
# 接收方信息
message['To'] = Header(str(";".join(receivres)))
# 主题绑定
message['Subject'] = Header(subject)

# 使用HTML格式的正文内容，添加附件
with  open('abc.html','r',encoding="utf-8") as f:
    content = f.read()
# 设置HTML格式参数
part1 =MIMEText(content,'html','utf-8')
# 以下都是附件代码
# 添加TXT附件
with open('b.txt','r',encoding="utf-8") as h:
    content2 = h.read()
# 设置TXT参数
part2 =MIMEText(content2,'plain','utf-8')

# 附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="b.txt"'

# 添加图片附件   MIMEImage(): 加载二进制图片，用于附件传输
with open('123.png','rb') as fp :
    picture = MIMEImage(fp.read())
picture['Content-Type'] = 'application/octet-stream'
picture['Content-Disposition'] = 'attachment;filename="123.png"'
# 将内容附件加到邮件主体中
# attach（添加的内容）  ：
# 将HTML添加到邮件中
message.attach(part1)
# 将文本添加到邮件中
message.attach(part2)
# 将图片添加到邮件中
message.attach(picture)
# 登录并发送邮件
try:
    #第一步：登录邮箱
        #第一种：不使用授权码
    # s1=smtplib.SMTP()
        #   连接到服务器
    # s1.connect(mail_host,25)
    # 第二种：使用授权码
    smtpObj =smtplib.SMTP_SSL(host=mail_host,port=mail_port)
    #登录服务器:输入用户名，密码
    smtpObj.login(user=muser,password=mail_pass)
    #发送    as_string（）  ：以字符串的形式发送出去
    smtpObj.sendmail(send,receivres,message.as_string())
    #退出
    smtpObj.quit()
    print("发送成功")
except smtplib.SMTPException as e:
    print("error:",e)  # 打印错误
"""
