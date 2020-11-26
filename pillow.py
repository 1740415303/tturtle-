from PIL import Image,ImageFilter
#相对路径
#imge1=Image.open('tupian/213813-154168429376d5.jpg')
#../上一级
#../../上两级
#绝对路径
# imge1=Image.open('D:\xiazai\玫瑰。jpg')
#加载图片
imge1=Image.open('tupian/213813-154168429376d5.jpg')
#显示图片
# imge1.show()
# #保存图片
# imge1.save('tupian/love.jpg')

#浮雕效果ImageFilter.EMBOSS
# imge2=imge1.filter(ImageFilter.EMBOSS)
# imge2.show()
# imge2.save('tupian/浮雕.jpg')

#铅笔画ImageFilter.CONTOUR
# imge3=imge1.filter(ImageFilter.CONTOUR)
# imge3.show()
# imge3.save('tupian/铅笔画.jpg')


#模糊效果ImageFilter.BLUR
# imge4=imge1.filter(ImageFilter.BLUR)
# imge4.show()
# imge4.save('tupian/模糊.jpg')


#实体加强ImageFilter.EDGE_ENHANCE
# imge5=imge1.filter(ImageFilter.EDGE_ENHANCE)
# imge5.show()
# imge5.save('tupian/EDGE_ENHANCE.jpg')

# 实体加强ImageFilter.SHARPEN
# imge6=imge1.filter(ImageFilter.SHARPEN)
# imge6.show()
# imge6.save('tupian/SHARPEN.jpg')

# EDGE_ENHANCE_MORE
# imge6=imge1.filter(ImageFilter.EDGE_ENHANCE_MORE)
# imge6.show()
# imge6.save('tupian/EDGE_ENHANCE_MORE.jpg')
#
#
# imge6=imge1.filter(ImageFilter.SMOOTH)
# imge6.show()
# imge6.save('tupian/SMOOTH.jpg')


# 自定义效果
# class  WH_PYTHON(ImageFilter.BuiltinFilter):
#     name = "WH_Python"
#     # fmt: off
#     filterargs = (3, 3), 13, 0, (
#         4, 4, 4,
#         4, 10, 4,
#         4, 4, 4,
#     )
#
# imge7=imge1.filter(WH_PYTHON)
# imge7.show()