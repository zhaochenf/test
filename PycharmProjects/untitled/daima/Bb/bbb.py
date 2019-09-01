#from A/AA  import aaa
#print(aaa.var)
#aaa.k()


# from daima.A.aaa import var
# print(var)

#from daima.A import aaa
a=input(f"请输入数字")
c=a.split()
a1=len(c)
for i in range(a1):
    for j in range(a1-1):
        if int(c[j])>int(c[j+1]):
            c[j],c[j+1]=int(c[j+1]),int(c[j])
print(c)

