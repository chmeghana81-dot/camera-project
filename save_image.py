import cv2

camera = cv2.VideoCapture(0)

success, frame = camera.read()

if success:
    cv2.imwrite("my_photo.jpg", frame)
    print("Image saved successfully")

camera.release()
