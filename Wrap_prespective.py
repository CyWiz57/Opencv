#Wrap prespective
import numpy as np
import cv2

img = cv2.imread("Resources/IMG_20200811_200544.jpg")
img = cv2.resize(img, (500, 500))

width, height = 250, 250
pt1 = np.float32([[100,2], [100,50], [300, 40], [300, 60]])
pt2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pt1, pt2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img1", img)
cv2.imshow("img2", imgOutput)
cv2.waitKey(0)