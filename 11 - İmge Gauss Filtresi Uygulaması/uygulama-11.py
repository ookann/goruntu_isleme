import cv2
import numpy as np
import random


image = cv2.imread('rgb.jpeg')

def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            yeni[j][i] = img[j][i][2]*0.299 + img[j][i][1]*0.587 + img[j][i][0]*0.114 
    return yeni

def gaus(img):
    boy = img.shape[0]
    en = img.shape[1]
    yeni = np.zeros((boy,en))
    for i in range(en-1):
        for j in range(boy-1):
            if (j==1) or (i==1) or (j==boy) or (i==en):
                yeni[j][i] = img[j][i]
                continue
            top = img[j-1][i-1]*1 + img[j-1][i]*2 + img[j-1][i+1]*1+img[j][i-1]*2+img[j][i]*4+img[j][i+1]*2+img[j+1][i-1]*1+img[j+1][i]*2+img[j+1][i+1]*1

            ort = top/16
            yeni[j][i] = ort
    return yeni
        


cv2.imshow('Orjinal Resim',image)

gri = donustur(image)
griresim =gri.astype(np.uint8)
cv2.imshow('gri',griresim)


gausImg= gaus(griresim)
gyeni = gausImg.astype(np.uint8)
cv2.imshow('gaus',gyeni)



 
cv2.waitKey(0)