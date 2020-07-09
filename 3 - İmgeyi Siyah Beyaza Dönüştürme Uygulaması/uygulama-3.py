import cv2
import numpy as np

# 1. katman blue
# 2. katman green
# 3. katman red

def gri(img):
    boy = img.shape[0]
    en = img.shape[1]
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            yeni[j][i] = img[j][i][2]*0.299 + img[j][i][1]*0.587 + img[j][i][0]*0.114 
    return yeni
def binary(img,esik):
    boy = img.shape[0]
    en = img.shape[1]
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            if (img[j][i] >= esik):
                yeni[j][i] = 1
            else:
                yeni[j][i] = 0
            
    return yeni

  
img = cv2.imread('rgb.jpg')
cv2.imshow('Orjinal Resim',img)

yeni = gri(img)
img = yeni.astype(np.uint8)

cv2.imshow('Gri Resim',img)
ikilik = binary(img,125)

cv2.imshow('Siyah Beyaz Resim',ikilik)


cv2.waitKey()
