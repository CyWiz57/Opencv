import cv2
import numpy as np
img = np.zeros((512,512,3), np.uint8)

# img[10:500] = 255,0,0

cv2.line(img, (0,0), (300,300), (0,255,255), 5)


cv2.imshow("img", img)
cv2.waitKey(0)