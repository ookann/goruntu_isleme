import cv2
import numpy as np

# 1. katman blue
# 2. katman green
# 3. katman red

def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            yeni[j][i] = img[j][i][2]*0.299 + img[j][i][1]*0.587 + img[j][i][0]*0.114 
    return yeni
  
img = cv2.imread('rgb.jpg')
yeni = donustur(img)

cv2.imshow('Orjinal Resim',img)

yeni_img = yeni.astype(np.uint8)

cv2.imshow('Yeni Resim',yeni_img)

cv2.waitKey()
