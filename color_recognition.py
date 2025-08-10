import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture("ved1.mp4")
while True:
    # Read each frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for RED color in HSV
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 + mask2

    # Bitwise-AND mask and original image
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Show results
    cv2.imshow("Original", frame)
    cv2.imshow("Red Objects", red_result)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
