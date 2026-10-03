import cv2

image = cv2.imread("my_photo.jpg")

print("Original size:", image.shape)

resized_image = cv2.resize(image, (640, 480))

print("New size:", resized_image.shape)

cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
