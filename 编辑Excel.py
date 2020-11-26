import xlrd
import xlwt
#打开成绩表
rwb=xlrd.open_workbook('fill/成绩表.xlsx')
mysheep=rwb.sheet_by_index(0)


#添加总分单元格
mysheep.put_cell(0,4,xlrd.XL_CELL_TEXT,'总分',None)
mysheep.put_cell(19,0,xlrd.XL_CELL_TEXT,'平均分',None)
for i in range(1,19):
    score=mysheep.row_values(i,1,4)
    mysheep.put_cell(i, 4, xlrd.XL_CELL_NUMBER,sum(score), None)
for j in range(1,5):
    score1=mysheep.col_values(j,1,19)
    mysheep.put_cell(19, j, xlrd.XL_CELL_NUMBER, sum(score1)/len(score1), None)
#编辑的实质是  读取 编辑  写入一个新的Excel文件

wwb=xlwt.Workbook(encoding='utf-8')
new_sheet=wwb.add_sheet('1班')
for i in range(mysheep.nrows):
    for j in range(mysheep.ncols):
        value=mysheep.cell_value(i,j)
        new_sheet.write(i,j,value)
wwb.save('fill/新成绩表.xls')





