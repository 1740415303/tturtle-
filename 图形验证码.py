from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import string
 #创建空画布
imge1=Image.new('RGBA',(120,60),(255,255,255,100))
#创建画画 的对象
draw=ImageDraw.Draw(imge1)
def rad():
    x=random.randint(1,255)
    y=random.randint(1,255)
    z=random.randint(1,255)
    return x,y,z

 #渲染背景
for i in range(120):#线汇成面
    for j in range(60):#点汇成线
        draw.point((i,j),rad())

 #渲染效果
# imge1=imge1.filter(ImageFilter.BLUR)

 #渲染文字
#创建一个字体对象
font=ImageFont.truetype('font/bb.ttf',25)
#将0-9之间任意数字  4次
# list1=['天','地','朽','而','我','不','死','日','月','灭']
# for i in range(4):
#     num=random.randint(0,9)
#     num=random.randint(0,9)
strings=list(string.ascii_letters)
for i in range(10):
    strings.append(str(i))
    #sample(列表，随机次数)n
    nun = random.randint(10,50)
x=''.join(random.sample(strings,4))
nun=random.randint(10,50)
draw.text((nun*3, nun), x, font=font,fill=rad())
 #显示保存
imge1.show()
