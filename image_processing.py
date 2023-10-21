from PIL import Image
img=Image.open('images.jpeg')
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT) 
transposed_img.save('output.jpeg')