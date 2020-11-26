from PIL import Image,ImageFont,ImageDraw
#打开图片
imge1=Image.open('tupian/玫瑰.png')


#创建字体truetype(字体文件，字号)
font=ImageFont.truetype('font/青呱石头体.ttf',100)
#255完全不透明，0完全透明


#创建绘画对象Draw(目标图片)
draw=ImageDraw.Draw(imge1)


#渲染文字text(坐标，文字内容，fill=文字颜色，font=字体类型)
draw.text((66,66),'耗子尾汁',(255,0,0 ,100),font)


#保存显示
imge1.show()
imge1.save('tupian/耗子尾汁.png')