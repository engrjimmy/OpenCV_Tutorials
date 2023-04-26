import cv2
import time

try:
    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Set the frame size of the video capture
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Check if the camera was opened successfully
    if not cap.isOpened():
        raise Exception("Error opening camera")

    # Get the current frame rate of the video capture
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Current frame rate:", fps)

    # Set the duration of the video capture
    duration = 60  # in seconds

    # Get the start time of the video capture
    start_time = time.time()

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
        if cv2.waitKey(int(1000/fps)) == ord('q'):
            break

        # Check if the duration of the video capture has been reached
        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            break

except Exception as e:
    print(str(e))

finally:
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

