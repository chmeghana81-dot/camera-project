# import cv2

# camera = cv2.VideoCapture(0)
# while True:
#     success, frame = camera.read()
#     if not success:
#         print("Camera could not be opend ")
#         break

#     cv2.imshow("My camera", frame)

#     if cv2.waitKey(1) & 0xFF == ("q"):
#         break
#     camera.release()
#     cv2.destroyAllWindows()


import cv2

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        print("Could not access camera")
        break

    cv2.imshow("My Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
