from PIL import Image

img1=Image.open('tupian/213813-154168429376d5.jpg')
img2=Image.open('tupian/xz.jpg')
img2.show()
#粘贴 图片1.paste(图片2，(位置))
img1.paste(img2,(300,300))
img1.show()