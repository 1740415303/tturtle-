import xlrd

#打开excel文件
workbook=xlrd.open_workbook('fill/成绩表.xlsx')


#获取目标sheet对象
sheet=workbook.sheet_by_index(0)


#获取celg相关内容
cell=sheet.cell(1,1)#下标从0开始
# print(cell)
# cell1=sheet.row_slice(1,1,3)#包含第一不包含第三
# print(cell1)
# for i in cell1:
#     print(i.value)
# print(sum([i.value for i in cell1]))
cell2=sheet.col_slice(2,1,5)#包含第一不包含第五
print(cell2)
print(sheet.cell_value(2,2))#获取第二行第二列的值
print(sheet.row_values(3,1,3))
print((sum(sheet.col_values(1,1,sheet.nrows)))/len(sheet.col_values(1,1,sheet.nrows)))


print(sheet.cell(0,1).ctype)
print(sheet.cell(2,2).ctype)