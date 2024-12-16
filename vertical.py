
import cv2,numpy as np
img=cv2.imread("lines.png",0)

imgNew=img.copy()
vertical= [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
h,w=img.shape[:2]

for i in range(1,h-1):
    for j in range(1,w-1):
        p=0
        for m in range(3):
            for n in range(3):
                p += (vertical[m][n] * img[i-1+m][j-1+n])
        imgNew[i][j] = p if p>0 else 0

cv2.imwrite("vertical.png",imgNew)
