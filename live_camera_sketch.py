import cv2

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    inverted = cv2.bitwise_not(gray)

    blur = cv2.GaussianBlur(inverted, (21, 21), 0)

    inverted_blur = cv2.bitwise_not(blur)

    sketch = cv2.divide(
        gray,
        inverted_blur,
        scale=256.0
    )

    cv2.imshow("Original Camera", frame)
    cv2.imshow("Live Pencil Sketch", sketch)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
