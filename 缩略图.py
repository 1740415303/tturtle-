from PIL import Image
#打开图片
imge1=Image.open('tupian/玫瑰.png')

#设置尺寸
#thumbnail(宽，高)
imge1.thumbnail((150,150))

#显示
imge1.show()

#保存
imge1.save('tupian/meigui.png')