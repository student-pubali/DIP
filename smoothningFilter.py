import numpy as np
import cv2


img = cv2.imread("salt_pep.jpg",0)
img2=img.copy()

h,w = img.shape
mask = np.ones([3,3],int)
img_new = np.zeros([h+2,w+2],int)

for i in range(1,h+1):
  for j in range(1,w+1):
    img_new[i,j]=img[i-1,j-1]

print(img_new)
for i in range(1,h+1):
    for j in range(1,w+1):
        temp = mask.copy()
        for m in range(3):
            for n in range(3):
                temp[m,n]=img_new[i-1+m,j-1+n]


        img2[i-1,j-1]=np.median(temp)
        #img2[i-1,j-1]=temp.min()
        #img2[i-1,j-1]=temp.max()
        # img2[i-1,j-1]=temp.mean()
imgs=np.hstack((img,img2))
cv2.imshow("New",imgs)
cv2.waitKey(0)
