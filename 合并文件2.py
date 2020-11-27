from PyPDF2 import PdfFileReader,PdfFileWriter


#读取两个文件
reader1=PdfFileReader('files/PIL.pdf')
reader2=PdfFileReader('files/water.pdf')



#准备两个页面
page1=reader1.getPage(0)
page2=reader2.getPage(0)
#
# #将页面page2添加到page1,与之合并
# page1.mergePage(page2)
#
# writer=PdfFileWriter()
# writer.addPage(page1)
# writer.write(open('files/new_page.pdf','wb'))


#将水印覆盖到每一个页面
writer1=PdfFileWriter()

number=reader1.getNumPages()
for i in range(number):
    page3=reader1.getPage(i)
    page3.mergePage(page2)
    writer1.addPage(page3)
writer1.write(open('files/new_page2.pdf','wb'))
