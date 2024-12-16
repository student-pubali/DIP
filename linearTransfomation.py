import cv2
import numpy as np

img=cv2.imread('lena.jpg',0)

h,w=img.shape
hr,wr = h//4,w//4

imgNew=np.roll(img, wr, 1)
imgNew[:,:wr]=0
imgNew=np.roll(imgNew, hr, 0)
imgNew[:hr,:]=0

cv2.imwrite("Translate.png",imgNew)

