import cv2
import numpy as np
"""
def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    yeni = np.zeros((boy,en,3))
    
    for i in range(boy):
        for j in range(en):
            yeni[i][j][:]=img[i][j][:]   
        

    return yeni
"""

img = cv2.imread('rgb.jpg')
cv2.imshow('Orjinal Resim',img)
#yeni = donustur(img)
boy = img.shape[0]
en = img.shape[1]
yeni = np.zeros((boy,en,3))

for i in range(boy):
    for j in range(en):
        yeni[i][j]=img[i][j]   

yeni_img = yeni.astype(np.uint8)

cv2.imshow('Yeni Resim',yeni_img)

cv2.waitKey()
cv2.destroyAllWindows() 
