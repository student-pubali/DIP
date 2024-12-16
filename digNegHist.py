import cv2 
import numpy as np 

img = cv2.imread('mono.jpg',0)

h,w = img.shape
print (h,w)


for i in range(h):
    for j in range(w):
        img[i,j] = 255 - img[i,j]
            
cv2.imwrite("neg.png",img)