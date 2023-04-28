# Import Necessary library
import cv2
import numpy as np

# Read Image MyPic.jpg
img = cv2.imread('jimmy.jpg')
# Convert 0 to 250 pixels from X and Y coordinates to white
img[0:250,0:250] = [255, 255, 255]
# Write Image as MyPicWhitePixel.jpg
cv2.imwrite('MyPicWhitePixel.jpg', img)