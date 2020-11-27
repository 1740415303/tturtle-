from PyPDF2 import PdfFileReader,PdfFileWriter


#读取两个文件
reader1=PdfFileReader('files/pygame.pdf')
reader2=PdfFileReader('files/Pygame的使用.pdf')


#开始写，需要一个写的对象

writer=PdfFileWriter()

#分别获取两个文件的页码  然后循环每一页写入新的页面
number1=reader1.getNumPages()
number2=reader2.getNumPages()

for i in range(number1):
    page=reader1.getPage(i)
    writer.addPage(page)
    # writer.addBlankPage() 创建一个空页面

for j in range(number2):
    page=reader1.getPage(j)
    writer.addPage(page)
    # writer.addBlankPage()

writer.write(open('files/new2.pdf','wb'))