from PIL import Image
im=Image.open('test1.png')
im_rgb=im.convert('RGB')
r,g,b=im_rgb.getpixel((150,90))
print(r,g,b)