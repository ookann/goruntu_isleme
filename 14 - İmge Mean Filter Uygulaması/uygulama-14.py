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
  


def meanFilter(img):
    yeni = np.zeros((boy, en))
    
    for i in range(boy-1):
        for j in range(en-1):
            if ((i == 1) or (j == 1) or (i == boy) or (j == en)):
                yeni[i][j] = img[i][j]
                continue
            
            top = img[i-1][j-1] + img[i-1][j] + img[i][j-1] + img[i][j] + img[i-1][j+1] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1]
            ortalama = top / 9
            yeni[i][j] = ortalama
    return yeni


gri = donustur(img)
imgGray = gri.astype(np.uint8)
cv2.imshow('Gri',imgGray)

meanUygula = meanFilter(gri)        
mean = meanUygula.astype(np.uint8)
cv2.imshow('Mean', mean)
cv2.waitKey(0)
