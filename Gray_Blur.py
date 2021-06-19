import cv2

img = cv2.imread("Resources/IMG_20200811_200544.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

cv2.imshow("gray", imgGray)
cv2.imshow("blur", imgBlur)
cv2.waitKey(10000)


