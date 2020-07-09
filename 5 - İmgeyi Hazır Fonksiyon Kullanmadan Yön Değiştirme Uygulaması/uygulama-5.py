import cv2
import numpy as np

def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    sabit_en = en-1
    yeni = np.zeros((boy,en,3))
    a=0
    for i in range(-1,boy-1,1):
        for j in range(-1,en-1,1):
            yeni[i+1][j+1][:]=img[i+1][sabit_en-a][:] 
            a=a+1
        a=0
                  
    return yeni
img = cv2.imread('rgb.jpg')
cv2.imshow('Orjinal Resim',img)

yeni = donustur(img)
yeni_img = yeni.astype(np.uint8)

cv2.imshow('Yeni Resim',yeni_img)

cv2.waitKey()
