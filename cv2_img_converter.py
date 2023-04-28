import cv2
grayImage = cv2.imread('jimmy.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('jimmy.png', grayImage)
