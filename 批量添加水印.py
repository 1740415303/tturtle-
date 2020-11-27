from PyPDF2 import PdfFileReader,PdfFileWriter
import os

#准备水印
water_page=PdfFileReader('files/water1.pdf').getPage(0)


#遍历文件夹里的文件 然后添加水印
all_file=os.listdir('files/inputs')

for i in all_file:
    path='files/inputs/'+i
    # print(path)

    reader=PdfFileReader(path)
    number=reader.getNumPages()
    writer=PdfFileWriter()
    for j in range(number):
        page3 = reader.getPage(j)
        page3.mergePage(water_page)
        writer.addPage(page3)
    writer.write(open('files/outpus/'+i,'wb'))