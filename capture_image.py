import cv2

camera = cv2.VideoCapture(0)

success, frame = camera.read()

if success:
    print("Image captured successfully")
else:
    print("Failed to capture image")

camera.release()
