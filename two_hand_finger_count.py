import cv2
import mediapipe as mp


# -----------------------------
# MediaPipe setup
# -----------------------------

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


# -----------------------------
# Finger counting function
# -----------------------------

def count_fingers(hand_landmarks, hand_label):

    landmarks = hand_landmarks.landmark

    fingers = 0

    # -------------------------
    # Thumb
    # -------------------------

    if hand_label == "Right":

        if landmarks[4].x < landmarks[3].x:
            fingers += 1

    else:

        if landmarks[4].x > landmarks[3].x:
            fingers += 1

    # -------------------------
    # Index finger
    # -------------------------

    if landmarks[8].y < landmarks[6].y:
        fingers += 1

    # -------------------------
    # Middle finger
    # -------------------------

    if landmarks[12].y < landmarks[10].y:
        fingers += 1

    # -------------------------
    # Ring finger
    # -------------------------

    if landmarks[16].y < landmarks[14].y:
        fingers += 1

    # -------------------------
    # Pinky
    # -------------------------

    if landmarks[20].y < landmarks[18].y:
        fingers += 1

    return fingers


# -----------------------------
# Open camera
# -----------------------------

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("❌ Camera could not be opened")
    exit()


# -----------------------------
# Main loop
# -----------------------------

while True:

    success, frame = camera.read()

    if not success:
        print("❌ Could not read camera")
        break

    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # Convert BGR → RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Detect hands
    results = hands.process(rgb_frame)

    total_fingers = 0

    left_fingers = 0
    right_fingers = 0

    # -----------------------------
    # Check detected hands
    # -----------------------------

    if results.multi_hand_landmarks:

        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            # Get hand name
            hand_label = handedness.classification[0].label

            # Count fingers
            finger_count = count_fingers(
                hand_landmarks,
                hand_label
            )

            # Add to total
            total_fingers += finger_count

            # Store left/right count
            if hand_label == "Left":
                left_fingers = finger_count
            else:
                right_fingers = finger_count

            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # -----------------------------
    # Display information
    # -----------------------------

    cv2.putText(
        frame,
        f"Left Hand: {left_fingers}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Right Hand: {right_fingers}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Total Fingers: {total_fingers}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Show camera
    cv2.imshow(
        "Two Hand Finger Counting",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------

camera.release()
cv2.destroyAllWindows()
hands.close()
