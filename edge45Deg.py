

import cv2,numpy as np

# img=cv2.imread("edge.jpg",0)
img=cv2.imread("cross.png",0)

imgNew=img.copy()

plus45= [[2,-1,-1],[-1,2,-1],[-1,-1,2]]
neg45 = [[-1,-1,2],[-1,2,-1],[2,-1,-1]]

h,w=img.shape[:2]

for i in range(1,h-1):
    for j in range(1,w-1):
        Gx=0
        Gy=0
        for m in range(3):
            for n in range(3):
                Gx += (plus45[m][n] * img[i-1+m][j-1+n])
                Gy += (neg45[m][n] * img[i-1+m][j-1+n])
        imgNew[i][j] = (Gx**2 + Gy**2)**0.5

show=np.hstack((img,imgNew))
cv2.imshow("edge45.png",show)