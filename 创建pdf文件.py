#注册字体 因为默认不支持中文
from reportlab.pdfbase import pdfmetrics

#指定字体
from reportlab.pdfbase.ttfonts import TTFont

#创建pdf文件
from reportlab.pdfgen import canvas

#注册字体  TTFont('字体名字'，'字体路径')

pdfmetrics.registerFont(TTFont('bb','../dey_2/font/bb.ttf'))

#创建空白文件
pdf_file=canvas.Canvas('files/water.pdf')

#写文字
#1）设置字体
pdf_file.setFont('bb',40)

#2)设置字体的颜色
#0~255   0(0)~1(255)

pdf_file.setFillColorRGB(0.5,0.5,0.5,0.5)

#写文字之前渲染角度
pdf_file.rotate(45)
##写文字
pdf_file.drawString(70,20,'Python是世界上最好的语言')

#保存文件
pdf_file.save()



