from PIL import Image
#加载图片
imge1=Image.open('tupian/表白.png')
# imge2=Image.open('tupian/玫瑰.png')
#创建镜像
#左右镜像
imge1_lr=imge1.transpose(Image.FLIP_LEFT_RIGHT)
#上下镜像
# imge2_tb=imge2.transpose(Image.FLIP_TOP_BOTTOM)
#上下左右镜像
imge_lr_tb=imge1_lr.transpose(Image.FLIP_TOP_BOTTOM)
#显示
# imge1_lr.show()
# imge2_tb.show()
imge_lr_tb.show()
#保存
imge1_lr.save('tupian/左右镜像.png')
# imge2_tb.save('tupian/上下镜像.png')
imge_lr_tb.save('tupian/上下左右镜像.png')