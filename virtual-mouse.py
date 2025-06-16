import cv2
import mediapipe as mp
import pyautogui

# Get screen size
screen_w, screen_h = pyautogui.size()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Capture webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            # Get index finger tip (landmark 8)
            index_finger_tip = hand_landmark.landmark[8]
            x = int(index_finger_tip.x * frame_w)
            y = int(index_finger_tip.y * frame_h)

            # Map camera coordinates to screen coordinates
            screen_x = int(index_finger_tip.x * screen_w)
            screen_y = int(index_finger_tip.y * screen_h)

            # Move mouse
            pyautogui.moveTo(screen_x, screen_y)

            # Optional: show circle on fingertip
            cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
