from PIL import Image

img1=Image.open('tupian/213813-154168429376d5.jpg')

#剪切图片
#crop(范围) 范围：左上右下
img2=img1.crop((90,50,950,500))
img2.show()
img2.save('tupian/剪切.jpg')
