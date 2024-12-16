import cv2,numpy as np

img=cv2.imread("lines.png",0)
imgNew=img.copy()

prewitX = [[-1,-1,-1],[0,0,0],[1,1,1]]
prewitY = [[-1,0,1],[-1,0,1],[-1,0,1]]

h,w=img.shape[:2]

for i in range(1,h-1):
    for j in range(1,w-1):
        Gx=0
        Gy=0
        for m in range(3):
            for n in range(3):
                Gx += (prewitX[m][n] * img[i-1+m][j-1+n])
                Gy += (prewitY[m][n] * img[i-1+m][j-1+n])
        imgNew[i][j] = (Gx**2 + Gy**2)**0.5

show=np.hstack((img,imgNew))
cv2.imshow("prewit.png",show)