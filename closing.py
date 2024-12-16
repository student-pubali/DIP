import cv2,numpy as np


def erotion(image,structEle,iter):
    imgNew= image.copy()
    length=len(structEle)
    t=length//2
    
    for k in range(iter):
        for i in range(t,h-t):
            for j in range(t,w-t):
                ele=[]
                for m in range(length):
                    for n in range(length):
                        if(structEle[m][n] ==1) :
                            ele.append(image[i-2+m][j-2+n])
                imgNew[i][j]=np.min(ele)

        image=imgNew.copy()
    return imgNew

def dilation(image,structEle,iter):
    imgNew= image.copy()
    
    length=len(structEle)
    t=length//2
    
    for k in range(iter):
        for i in range(t,h-t):
            for j in range(t,w-t):
                ele=[]
                for m in range(length):
                    for n in range(length):
                        if(structEle[m][n] ==1) :
                            ele.append(image[i-2+m][j-2+n])
              
                imgNew[i][j]=np.max(ele)
        image=imgNew.copy()
    return imgNew

def closing(image,structEle,iter):
    image=dilation(image,structEle,iter)
    image=erotion(image,structEle,iter)
    return image
img=cv2.imread("circle.jpg",0)
imgNew=img.copy()

structEle = [[1,1,1],
             [1,1,1],
             [1,1,1]
             ]

h,w=img.shape[:2]

imgNew = closing(img,structEle,5)

cv2.imwrite("coseded.png",imgNew)
