import cv2

img=cv2.imread('jimmy.jpg') #img = cv2.imread('/home/img/python.png')
 
cv2.imshow('sample',img)
 
cv2.waitKey(0) # waits until a key is pressed

cv2.destroyAllWindows() # destroys the window showing image


