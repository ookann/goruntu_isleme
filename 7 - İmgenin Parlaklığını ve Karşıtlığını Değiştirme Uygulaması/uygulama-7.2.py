import cv2
import numpy as np

def donustur(img):
    a1=0.5
    a2=2
    boy = img.shape[0]
    en = img.shape[1]
    k_azalt = np.zeros((boy,en,3))
    k_arttir = np.zeros((boy,en,3))
 
    for i in range(en):
        for j in range(boy):
            k_azalt[j][i] = img[j][i] * a1  
            k_arttir[j][i] = img[j][i] * a2
    return k_azalt,k_arttir


img = cv2.imread('rgb.jpg')
cv2.imshow('Resim',img)

k_azalt,k_arttir = donustur(img)

k_azalt = k_azalt.astype(np.uint8)
cv2.imshow('azalan kontrast',k_azalt)

k_arttir = k_arttir.astype(np.uint8)
cv2.imshow('artan kontrast',k_arttir)

cv2.waitKey()


