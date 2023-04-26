import cv2

def main():
    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Error opening camera")
        exit()

    # Set the frame size of the video capture
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if a frame was successfully read
        if not ret:
            break

        # Display the frame
        cv2.imshow('Video', frame)

        # Wait for a key press and check if it's the 'q' key to exit
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

