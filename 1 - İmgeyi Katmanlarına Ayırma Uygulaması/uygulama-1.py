import cv2
img = cv2.imread('rgb.jpg')

Red = img[:,:,2]
Green = img[:,:,1]
Blue = img[:,:,0]

cv2.imshow('Red',Red)
cv2.imshow('Green',Green)
cv2.imshow('Blue',Blue)

cv2.waitKey()












