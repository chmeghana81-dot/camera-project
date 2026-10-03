import cv2

camera = cv2.VideoCapture(0)

success, frame = camera.read()

if success:
    cv2.imshow("Captured Image", frame)

    cv2.waitKey(0)

camera.release()
cv2.destroyAllWindows()
