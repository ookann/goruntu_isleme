import cv2
import numpy as np

def kirpma(img,x,y):
    boy = img.shape[0]
    en = img.shape[1]
    kirpilmis = np.zeros((en,boy,3))
 
    for i in range(1,90):
        for j in range(1,90):
            kirpilmis[j][i]=img[j+x][i+y]   
    return kirpilmis


x = int(input("Satır: "))
y = int(input("Sütun: "))


img = cv2.imread('rgb.jpg')
cv2.imshow('Orjinal Resim',img)

kirp = kirpma(img,x,y)

yeniresim = kirp.astype(np.uint8)

cv2.imshow('Yeni Resim',yeniresim )

cv2.waitKey()

cv2.destroyAllWindows()
