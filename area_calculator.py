import numpy
from PIL import Image
width=10
height=4
array=numpy.zeros([height,width,3],dtype=numpy.uint8)
img=Image.fromarray(array)
img.save("test.png")
array1=numpy.zeros([100,200,3],dtype=numpy.uint8)
array1[:,:100]=[255,128,0]
array1[:,100:]=[0,0,255]
img=Image.fromarray(array1)
img.save("test1.png")