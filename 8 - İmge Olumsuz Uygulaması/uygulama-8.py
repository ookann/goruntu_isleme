import cv2
import numpy as np

def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    olumsuz = np.zeros((boy,en,3))
 
    for i in range(en):
        for j in range(boy):
            olumsuz[j][i] = 255 - img[j][i]    
    return olumsuz


img = cv2.imread('rgb.jpg')
cv2.imshow('Resim',img)

olumsuz = donustur(img)

olumsuz = olumsuz.astype(np.uint8)
cv2.imshow('Olumsuz',olumsuz)

cv2.waitKey()


