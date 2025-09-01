from PIL import Image,ImageEnhance,ImageFilter

img=Image.open("test.png")
blurred=img.filter(ImageFilter.BLUR)
blurred.show()