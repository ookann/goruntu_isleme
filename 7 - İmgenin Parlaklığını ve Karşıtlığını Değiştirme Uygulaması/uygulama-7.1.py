import cv2
import numpy as np

def donustur(img):
    b1=-50
    b2=50
    boy = img.shape[0]
    en = img.shape[1]
    koyu = np.zeros((boy,en,3))
    acik = np.zeros((boy,en,3))
 
    for i in range(en):
        for j in range(boy):
            koyu[j][i] = img[j][i] + b1  
            acik[j][i] = img[j][i] + b2
    return koyu,acik


img = cv2.imread('rgb.jpg')
cv2.imshow('Resim',img)

koyu,acik = donustur(img)

resim_koyu = koyu.astype(np.uint8)
cv2.imshow('Koyu',resim_koyu)

resim_acik = acik.astype(np.uint8)
cv2.imshow('Acik',resim_acik)

cv2.waitKey()


