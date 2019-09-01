#！/usr/bin/python
#-*- coding:utf-8 -*-
#客户端
# import socket
# ip_port=('127.0.0.1',6662)
# c=socket.socket()
# c.connect(ip_port)
# while True:
#     t = input('输入发送的信息').strip()
#     if t=='1':
#         break
#     else:
#         print(f"客户端向服务器发送的信息")
#         c.sendall(t.encode())
#     s_date = c.recv(1024).decode('utf-8')
#     print(s_date)
# c.close()

# with open(file='a.txt',mode='w',encoding='utf-8')  as f:
#     f.write('zhe,shi,guo,123\n'*100)
#     #f.write('\n')

with open("a.txt", mode="r", encoding="utf-8") as f:
    a = f.read()
    #print(a)
    t = a.strip()
    b = a.split("\n")
    #print(b)
    #print(len(b))
    for i in range(len(b)):
        #ww = b[i]
        ww = b[i].split(",")
        print(ww)
        r=tuple(ww)
        print(r)

# with open('a.txt', encoding='utf-8') as fc:
#     a = fc.read()
#     t=a.strip()
#     #print(t)
#     b=t.split('\n')
#     print(b)

    # txt_list = a.split('\n')
    # print(txt_list)
    # for i in txt_list:
    #     txt_list_1 = i.split(',')
    #     print(txt_list_1)