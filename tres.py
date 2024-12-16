import cv2,numpy as np
img = cv2.imread("j.jpg",0)

h,w=img.shape[:2]
m=np.mean(img)
print(h,w)

for i in range(h):
    for j in range(w):
        if(img[i][j]>m):
            img[i][j]=255
        else:
            img[i][j]=0
cv2.imwrite("thres.png",img)
