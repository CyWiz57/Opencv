import numpy as np
import cv2

img = cv2.imread("Resources/IMG_20200729_193358.jpg")
print(img.shape)
imgResize = cv2.resize(img, (600,400))
imgCropped = imgResize[0:200, 200:500]

cv2.imshow("img1",imgCropped)
cv2.imshow("img2",imgResize)
cv2.waitKey(10000)