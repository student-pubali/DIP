#Salt-peper noise
import cv2
import numpy as np
import random
img = cv2.imread("low_cont.jpg",0)
imgP = img.copy()
imgSP = img.copy()
h,w = img.shape[:2]
rng = random.randint(h//4,h)
for i in range(rng):
    x1 = random.randint(0,h-1)
    y1 = random.randint(0,w-1)
    x2 = random.randint(0,h-1)
    y2 = random.randint(0,w-1)
    imgSP[x1][y1] = 255
    imgSP[x2][y2] = 0

cv2.imwrite("salt_pep.jpg",imgSP)    
