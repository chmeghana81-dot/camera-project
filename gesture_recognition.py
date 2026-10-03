import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

camera = cv2.VideoCapture(0)


def detect_gesture(hand_landmarks):

    landmarks = hand_landmarks.landmark

    fingers = []

    # Index
    fingers.append(
        landmarks[8].y < landmarks[6].y
    )

    # Middle
    fingers.append(
        landmarks[12].y < landmarks[10].y
    )

    # Ring
    fingers.append(
        landmarks[16].y < landmarks[14].y
    )

    # Pinky
    fingers.append(
        landmarks[20].y < landmarks[18].y
    )

    count = sum(fingers)

    if count == 0:
        return "Fist"

    elif count == 1:
        return "One Finger"

    elif count == 2:
        return "Two Fingers"

    elif count == 3:
        return "Three Fingers"

    elif count == 4:
        return "Open Palm"

    else:
        return "Unknown"


while True:

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(rgb_frame)

    gesture = "No Hand"

    if results.multi_hand_landmarks:

        hand_landmarks = results.multi_hand_landmarks[0]

        gesture = detect_gesture(hand_landmarks)

        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Gesture Recognition",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
