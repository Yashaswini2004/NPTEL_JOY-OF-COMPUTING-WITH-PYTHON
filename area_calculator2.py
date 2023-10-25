import scipy.misc
import random
import numpy as np
from PIL import Image
image=scipy.misc.imread("map.png")
count_pun=0
count_ind=0
count=0
while(count<=10000):
    x=random.randint(0,398)
    y=random.randint(0,359)
    z=0
    if(image[x][y][z]==60):
        count_ind=count_ind+1
        count=count+1
    else:
        if(image[x][y][z]==80):
            count_pun=count_pun+1
            count=count+1
area_pun=(count_pun/count_ind)*3287263
print(area_pun)  
