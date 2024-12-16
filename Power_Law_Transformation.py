import cv2
import numpy as np

img = cv2.imread("darkerImg.jpg")
img_new = img.copy()
gamma = 1/2.5
c=255
h,w=img.shape[:2]

def PowerLaw(pixel):
    # global gamma,c
    return c*((pixel/255)**gamma)

for i in range(h):
    for j in range(w):
        img_new[i,j]=PowerLaw(img[i,j])

cv2.imwrite("PLT.png",img_new)

