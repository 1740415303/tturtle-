import xlwt
import random
#创建workbook对象
workbbok=xlwt.Workbook(encoding='utf-8')

#创建一个sheet对象
sheet=workbbok.add_sheet('成绩表')

#添加表头
sheet.write(0,0,'姓名')
sheet.write(0,1,'语文')
sheet.write(0,2,'数学')
sheet.write(0,3,'英语')
for i in range(1,11):
    for j in range(1,4):
        sheet.write(i,j,random.randint(50,100))


#保存成Excel文件
workbbok.save('fill/scores.xls')
