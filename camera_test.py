import cv2

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Set the frame size of the video capture
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read the frames from the camera and display them
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if a frame was successfully read
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press and check if it's the 'q' key to exit
    if cv2.waitKey(1) == ord('q'):
        break
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 49f9f693cca7379c7563a21b54699fb3095b2f33

# Release the camera and close the window
cap.release()

cv2.destroyAllWindows()
main
<<<<<<< HEAD
>>>>>>> 49f9f693cca7379c7563a21b54699fb3095b2f33

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
=======

>>>>>>> 49f9f693cca7379c7563a21b54699fb3095b2f33
