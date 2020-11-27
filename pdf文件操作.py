from PyPDF2 import PdfFileReader,PdfFileWriter

#因为PyPDF2 针对已经存在的 所以先要读取
#PdfFileReader(文件路径/文件)
reader=PdfFileReader('files/MySQL.pdf')

#获取mysql.pdf有几页

number=reader.getNumPages()
# print(number)

#获取指定的页码
first_Page=reader.getPage(1)
# print(first_Page)
# #获取指定表单域
# reader.getFormTextFields()

#往里写
writer=PdfFileWriter()

writer.addPage(first_Page)
writer.addBlankPage()

#新建pdf文件
#从一个已经存在的pdf文件中 读取第一页，然后写进来
f=open('files/new.pdf','wb')
writer.write(f)


