import cv2
import numpy as np

import matplotlib.pyplot as plt

def donustur(img):
    boy = img.shape[0]
    en = img.shape[1]
    hist = np.zeros(256) 
    for i in range(en):
        for j in range(boy):
            hist[img[j][i]+1] = hist[img[j][i]+1] + 1  
    return hist

 
img = cv2.imread('rgb.jpg')

hist= donustur(img)

plt.plot(hist)
plt.show()


