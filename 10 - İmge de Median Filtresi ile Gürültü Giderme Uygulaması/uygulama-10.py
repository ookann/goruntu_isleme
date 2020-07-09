import cv2
import numpy as np
import random
from skimage.util import random_noise

image = cv2.imread('rgb.jpg')

def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rnd = random.random()
            if rnd<prob:
                output[i][j] = 0
            elif rnd > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    
    yeni = np.zeros((boy,en))
    for i in range(en):
        for j in range(boy):
            yeni[j][i] = img[j][i][2]*0.299 + img[j][i][1]*0.587 + img[j][i][0]*0.114 
    return yeni

b = int(input("Blok boyutunu giriniz : "))
#image = donustur(image) 
gurultuluresim = random_noise(image, mode='s&p',amount=.01)
gurultuluresim = np.array(255*gurultuluresim, dtype = 'uint8')
cv2.imshow('Salt and pepper',gurultuluresim)
x = []
yr = gurultuluresim.astype('float64')
print(yr.dtype)

for i in range(10):
    for j in range(2):
        x.append(gurultuluresim[i][j])
        x.append(gurultuluresim[i][j+1])
        x.append(gurultuluresim[i][j+2])
        
        x.append(gurultuluresim[i+1][j])
        x.append(gurultuluresim[i+1][j+1])
        x.append(gurultuluresim[i+1][j+2])
        
        x.append(gurultuluresim[i+2][j])
        x.append(gurultuluresim[i+2][j+1])
        x.append(gurultuluresim[i+2][j+2])
        
        aa = np.sum(x, axis = 1)
        print(np.sum(x[0:9]))

"""
y = np.zeros((image.shape[0],image.shape[1]))
noise_img = sp_noise(image, .01)

yeni_img =noise_img.astype(np.uint8)
cv2.imshow('Salt and pepper',yeni_img)



y = cv2.medianBlur(yeni_img,3)
cv2.imshow('Yeni',y)
"""
cv2.waitKey(0)










