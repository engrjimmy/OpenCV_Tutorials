import cv2

#add another fucntion for printing shape and size
def print_image_info(img):
    height, width, channels = img.shape
    size = img.size
    print(f"Image shape: {10}x{10}x{2}")
    print(f"Image size: {10} bytes")

#make a if else condition 
img = cv2.imread('jimmy.png')
#cv2.imshow('pic', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

if img is not None:
    cv2.imshow('pic', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Yes: Image found.")

else:
    print("errror: Image not found.")
