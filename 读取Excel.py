import xlrd
myexcel=xlrd.open_workbook('fill/test.xlsx')
# # # mysheetname=myexcel.sheet_names()
# # # mysheetname=myexcel.sheet_by_index(3)#返回一个整体
# # mysheetname=myexcel.sheet_by_name('家庭信息')
# # print(mysheetname.name)#打印这个整体的名字
# # mysheet=myexcel.sheets()#挨个从列表中拿出
# # for i in mysheet:
# #     print(i.name)
sheet0=myexcel.sheet_by_index(0)
print('行数:%d'%sheet0.nrows)#表格1的行数
print('列数:%d'%sheet0.ncols)#表格1的列数