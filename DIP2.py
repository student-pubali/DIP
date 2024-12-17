#Contrast Stretching
import numpy as np
import cv2
img = cv2.imread("low_cont1.png",0)
Lmax = 255
Lmin = 0
Mmax = np.max(img)
Mmin = np.min(img)
streched_img = img.copy()
height,width = img.shape
for i in range(height):
    for j in range(width):
        pixel = streched_img[i,j]
        pixel = ((pixel-Mmin)*((Lmax-Lmin)/(Mmax-Mmin)))+(Lmin)
        streched_img[i,j] = pixel

cv2.imwrite("After_Strech.png",streched_img)        
