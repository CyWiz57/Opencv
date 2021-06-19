import numpy as np
import cv2

img = cv2.imread("Resources/IMG_20200729_193358.jpg")
img = cv2.resize(img, (500, 400))

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("img", img)
cv2.imshow("img1", imgHor)
cv2.imshow("img2", imgVer)
cv2.waitKey(0)