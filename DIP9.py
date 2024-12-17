#Erosion
import cv2
import numpy as np
def erotion(image,structEle,iter):
    imgNew = image.copy()
    for k in range(iter):
        for i in range(2,h-2):
            for j in range(2,w-2):
                flag = True
                for m in range(5):
                    for n in range(5):
                        if(structEle[m][n]==1) and (image[i-2+m][j-2+n]!=255):
                            flag = False
                if(flag):
                    imgNew[i][j]= 255
                else:
                    imgNew[i][j] = 0
        image = imgNew.copy()
    return imgNew   

img = cv2.imread("j.png",0) 
imgNew = img.copy()
structEle =[[1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
] 
h,w = img.shape[:2]  
imgNew = erotion(img,structEle,3)   
cv2.imwrite("edore.png",imgNew)                     
