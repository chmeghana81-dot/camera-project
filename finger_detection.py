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


def count_fingers(hand_landmarks):

    fingers = 0

    landmarks = hand_landmarks.landmark

    # Index finger
    if landmarks[8].y < landmarks[6].y:
        fingers += 1

    # Middle finger
    if landmarks[12].y < landmarks[10].y:
        fingers += 1

    # Ring finger
    if landmarks[16].y < landmarks[14].y:
        fingers += 1

    # Pinky
    if landmarks[20].y < landmarks[18].y:
        fingers += 1

    return fingers


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

    if results.multi_hand_landmarks:

        hand_landmarks = results.multi_hand_landmarks[0]

        fingers = count_fingers(hand_landmarks)

        cv2.putText(
            frame,
            f"Fingers: {fingers}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

    cv2.imshow("Finger Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
