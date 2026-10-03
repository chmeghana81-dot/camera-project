import cv2

# Read image
image = cv2.imread("my_photo.jpg")

if image is None:
    print("❌ Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert grayscale image
inverted = cv2.bitwise_not(gray)

# Blur the inverted image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
inverted_blur = cv2.bitwise_not(blur)

# Create pencil sketch
sketch = cv2.divide(
    gray,
    inverted_blur,
    scale=256.0
)

# Save sketch
cv2.imwrite("pencil_sketch.jpg", sketch)

print("✅ Sketch saved as pencil_sketch.jpg")

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
