import cv2
import numpy as np

  
img = cv2.imread('rgb.jpeg')
cv2.imshow('Orjinal',img)

boy = img.shape[0]
en = img.shape[1]
def donustur(img):
    
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            yeni[j][i] = img[j][i][2]*0.299 + img[j][i][1]*0.587 + img[j][i][0]*0.114 
    return yeni


def norm(img):
    yMin = 0;
    yMax = 100;
    minDegeri = np.amin(img)  
    maxDegeri = np.amax(img)
    
    for i in range(boy):
        for j in range(en):
            I = img[i][j]
            Inew = (I - minDegeri) * ((yMax - yMin) / (maxDegeri - minDegeri)) + yMin
            img[i][j] = Inew
    return img
gri = donustur(img)
imgGray = gri.astype(np.uint8)
cv2.imshow('Gri',imgGray)

normResim = norm(imgGray)    
normResim = normResim.astype(np.uint8)
cv2.imshow('Norm', normResim)
cv2.waitKey(0)
