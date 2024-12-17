#Histogram Equalization
import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread("low_cont1.png",0)
h,w = img.shape
hist = cv2.calcHist([img],[0],None,[256],[0,255])
plt.plot(hist)
plt.show()
print(h,w)
Freq_Count = [0]*256
for i in range(h):
    for j in range(w):
        Freq_Count[img[i][j]] += 1
total = np.sum(Freq_Count)
Freq_Count = ((Freq_Count/total))
Freq_Count = np.cumsum(Freq_Count)
Freq_Count = np.ceil(Freq_Count*255)
newImg = np.zeros(img.shape,img.dtype)
for i in range(h):
    for j in range(w):
        newImg[i][j] += Freq_Count[img[i][j]]
cv2.imwrite("eq.jpg",newImg)
hist = cv2.calcHist([newImg],[0],None,[256],[0,255])
plt.plot(hist)
plt.show()
