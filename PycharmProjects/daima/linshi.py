
import xlrd
import xlwt
from xlutils.copy import copy
#a=(["序号","user","password"],[1,"admin",888888])
a=([2,"textadmin","textpassword"])
class add(object):
    def __init__(self):
        self.d = xlrd.open_workbook(filename="24.xls")
        self.new_d = copy(self.d)

        self.t = self.d.sheet_by_index(1)
    def date(self):
        print(self.t.row_values(1))
        return self.t.row_values(1)

    def qwe(self):
        #self.d = xlwt.Workbook()
        #table = self.d.add_sheet("sheet1")
        table = self.new_d.get_sheet(1)
        for i in range(len(a)):
            table.write(2,i,a[i])
        self.new_d.save("24.xls")
b=add()
#b.qwe()
#b.date()
b.qwe()



# import xlrd
# import xlwt
# from xlutils.copy import copy
# a=(["序号","user","password"],[1,"admin",888888])
# class add(object):
#     def __init__(self):
#         self.d = xlrd.open_workbook(filename="24.xls")
#         self.new_d = copy(self.d)
#         self.t = self.d.sheet_by_index(1)
#     def ads(self):
#         table = self.new_d.get_sheet(1)
#         for i in range(len(a)):
#             for j in range(len(a[i])):
#                 table.write(i, j, a[i][j])
#         self.d.save("24.xls")
# a=add()
# a.ads()

# class SuperClass(object):
#     def sample(self):
#         print ('SuperClass')
# class SubClass(SuperClass):
#     pass
# sub = SubClass()
# sub.sample()

#coding=utf-8
