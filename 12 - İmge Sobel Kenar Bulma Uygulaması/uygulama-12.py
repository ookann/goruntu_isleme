import cv2
import numpy as np

def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            yeni[j][i] = img[j][i][2]*0.299 + img[j][i][1]*0.587 + img[j][i][0]*0.114 
    return yeni


def gaus(img):
    B=C
    for i in range(image.shape[0]-2):
        for j in range(image.shape[1]-2):
            Gx=((2*C[i+2][j+1]+C[i+2][j]+C[i+2][j+2])-(2*C[i][j+1]+C[i][j]+C[i][j+2]));
            Gy=((2*C[i+1][j+2]+C[i][j+2]+C[i+2][j+2])-(2*C[i+1][j]+C[i][j]+C[i+2][j]));
          
            B[i][j] = abs(Gx) + abs(Gy)
            
            if (B[i][j] <100):
                B[i][j] =0
            else:
                B[i][j] =255
    return B

image = cv2.imread('rgb.jpeg')
C = donustur(image)

cv2.imshow('Resim',image)

gauss = gaus(C)
gausresim =gauss.astype(np.uint8)
cv2.imshow('Gaus',gausresim)
  

cv2.waitKey(0)