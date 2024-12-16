import cv2
import numpy as np

img = cv2.imread("darkerImg.jpg",0)
img_new = img.copy()
h,w=img.shape

def LogTransDyna(pixel):
    return ((255/np.log10(256))*np.log10(pixel+1))

for i in range(h):
    for j in range(w):
        img_new[i,j] = LogTransDyna(img[i,j])

cv2.imwrite("logTrans.png",img_new)


