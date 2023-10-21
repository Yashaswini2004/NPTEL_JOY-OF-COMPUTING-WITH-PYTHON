import cv2
img=cv2.imread('input.jpeg')
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
cv2.imwrite('enhanced_img.jpeg',enh_img)