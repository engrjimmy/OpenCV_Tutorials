#import OpenCV library 

#import cv2

#img=cv2.imread('jimmy.jpg') #img = cv2.imread('/home/img/python.png')
 
#cv2.imshow('sample',img)
 
#cv2.waitKey(0) # waits until a key is pressed

#cv2.destroyAllWindows() # destroys the window showing image


# Import OpenCV library
#import cv2
# Import Numpy library
#import numpy as np

#Read image named MyPic.jpg
#img = cv2.imread('jimmy.jpg')
# Prints the current value of Blue for that pixel
#print(img.item(150, 120, 0))
# Set the value of Blue for (150,120) pixel to 255
#img.itemset( (150, 120, 0), 255)
# Print value of Blue at (150,120) pixel
#print(img.item(150, 120, 0))




# Import OpenCV library
import cv2
#Import Numpy library
import numpy as np

# Read Image named MyPic.jpg
img = cv2.imread('jimmy.png')
# Define region in my_roi
my_roi = img[0:300, 0:300]
# Replace that region with my_roi
img[300:600, 300:600] = my_roi
# Write Image as ROI.jpg

cv2.imwrite('ROI.png', img)

cv2.imshow('sample',img)
 
cv2.waitKey(0) # waits until a key is pressed

cv2.destroyAllWindows() # destroys the window showing image
