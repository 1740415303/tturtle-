from PIL import Image
#创建空白图 new(模式，大小，颜色)
#模式（rgb,rgba）r （255,0,0) red  g (0,255,0) green b (0,0,255) blue a 透明度
empty=Image.new('RGB',(2000,2000),(123,125,120))

#打开图片
imge1=Image.open('tupian/213813-154168429376d5.jpg')
imge2=Image.open('tupian/xz.jpg')
imge3=Image.open('tupian/铅笔画.jpg')
imge4=Image.open('tupian/浮雕.jpg')
# imge1.show()
# imge2.show()

#把图片粘贴到空白图上
empty.paste(imge1,(0,0))
empty.paste(imge2,(1200,0))
empty.paste(imge3,(0,700))
empty.paste(imge4,(0,1400))
empty.show()