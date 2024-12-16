import cv2,numpy as np,matplotlib.pyplot as plt
img= cv2.imread("low_cont1.png",0)
img1=cv2.imread("eq.jpg",0)

h,w=img.shape
imgNew = np.zeros([h,w],img.dtype)
#img1= cv2.resize(img1,[w,h])

freqCount = np.zeros([256],int)
freqCount1 = np.zeros([256],int)



for i in range(h):
    for j in range(w):
        freqCount[img[i][j]] += 1
        freqCount1[img1[i][j]] += 1
#print(freqCount1)
total = np.sum(freqCount)
total1= np.sum(freqCount1)



freqCount = (freqCount / total)
freqCount1 = (freqCount1 / total1)

freqCount = np.cumsum(freqCount )
freqCount1 = np.cumsum(freqCount1 )

freqCount = np.ceil(freqCount *255)
freqCount1 = np.ceil(freqCount1 *255)


maping =[0]*256

for m in range(256):
    pix=freqCount[m]
    for n in range(256):
        if(pix in freqCount1):
            maping[m]=np.where(freqCount1==pix)[0][0]
            break
        pix += 1

#print(maping)
        
for i in range(h):
    for j in range(w):
        imgNew[i][j] = maping[img[i][j]]
        
cv2.imshow("",imgNew)
cv2.waitKey(0)
