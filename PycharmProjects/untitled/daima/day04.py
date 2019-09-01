"""

a = {1:["香蕉",11,123],
     2:["苹果",25,120],
     3:["橘子",17,243],
     4:["西瓜",10,178],
     5:["桃子",15,210],
     6:["葡萄",13,188]
}
k = {666:2000,
     111:3678,
     777:8000,
     999:20000,
     2333:17900
}
# a = ["香蕉","苹果","橘子","西瓜","桃子","葡萄"]
# b = [11,25,17,10,15,13]
# c = [123,120,243,178,210,188]
# e = [1,2,3,4,5,6]
# print(a[1])
# while True:
print(f" 编号\t           商品\t            单价\t           库存")
for b in range(1,7):
    print(f" {b}\t               {a[b][0]}\t            {a[b][1]}\t               {a[b][2]}")
while True:
    c = input("是否要购买商品，是的输入Y,退出输入B：")
    if c == "Y" :
        d = input("请输入购买的编号：")
        while  int(d) > 6  or int(d) < 1:
            d = input("商品不存在，请输入有效编号：")
        e = input("请输入购买数量：")
        while int(e) > a[int(d)][2] and int(e) > 0:
            e = input("你输入数量超过库存，请重新购买")
        g = input("结账，会员输入卡号，不是请输入N:")
        h = a[int(d)][1] * int(e)
        if g == "N":
            print(f"你购买了:{a[int(d)][0]} 数量:{e} 应付金额:{h} 剩余库存:{a[int(d)][-1] - int(e)}")
            i = int(input("请付款："))
            while i <= h:
                i = int(input("你钱不够，请重新付款："))
            print(f"找零{i - h} ")
        else:
            l = 0
            while int(g) not in k.keys():
                g = input("错误卡号，请重新输入，超过5次退出系统:")
                l += 1
                if l == 4:
                    break
            if l < 4:
                if h * 0.8 > k[int(g)]:
                    print(f"卡内余额不足，应支付{h * 0.8},卡内余额{k[int(g)]}")
                    print(f"会员卡号:{g}，购买商品:{a[int(d)][0]} 数量:{e} 剩余库存:{a[int(d)][-1] - int(e)} 应付金额:{h} 八折优惠,实付:{h * 0.8} 卡内余额:{k[int(g)]} ")
                    i = int(input(f"请补足付款{h * 0.8 - k[int(g)]}:"))
                    while i < h * 0.8 - k[int(g)]:
                        i = int(input("你钱不够，请重新补足余款："))
                    print(f"找零{i - (h * 0.8 - k[int(g)])} ")
                else:
                    print(f"会员卡号:{g}\t购买了:{a[int(d)][0]}\t数量:{e}\t剩余库存:{a[int(d)][-1] - int(e)}\t应付金额:{h}，八折优惠,实付:{h * 0.8}\t卡内余额:{k[int(g)] - (h * 0.8)} ")
            else:
                pass
    elif c == "B":
        break

"""
#嵌套循环输出10-50中个位带有1-5的所有数字
# for i in range(10,50):
#     if str(i)[1] in ["1","2","3","4","5"]:
#         print (i)

# for i in range(1,5):
#     for j in range(1,6):
#         print(str(i)+str(j))


# class cat:
#     def eat(self):
#         print("小猫爱吃鱼")
#     def drink(self):
#         print("小猫爱喝水")
# tom=cat()
# tom.eat()
# tom.drink()