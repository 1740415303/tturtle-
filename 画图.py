from PIL import Image,ImageDraw
import random
#创建画布
imge1=Image.new('RGBA',(800,800),(100,200,100,100))

#创建一个画画的人
draw=ImageDraw.Draw(imge1)


#画颜色 point(坐标，颜色)
# for i in range(1000):
#     for j in range(600):
#         draw.point((i,j),(0,0,0))
def rad():
    x=random.randint(1,255)
    y=random.randint(1,255)
    z=random.randint(1,255)
    return x,y,z
for i in range(600):#线汇成面
    for j in range(600):#点汇成线
        draw.point((i,j),rad())


imge1.show()