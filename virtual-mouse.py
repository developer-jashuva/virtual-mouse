import cv2
import mediapipe as mp
import pyautogui
import math

# Get screen size
screen_w, screen_h = pyautogui.size()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Capture webcam
cap = cv2.VideoCapture(0)
click_cooldown = 0  # To prevent continuous clicking

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            # Get important landmark positions
            landmarks = hand_landmark.landmark
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]
            middle_tip = landmarks[12]

            # Move mouse using index finger tip
            x = int(index_tip.x * frame_w)
            y = int(index_tip.y * frame_h)
            screen_x = int(index_tip.x * screen_w)
            screen_y = int(index_tip.y * screen_h)
            pyautogui.moveTo(screen_x, screen_y)

            # Draw index point
            cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

            # Calculate distance between thumb & index (for left click)
            ix, iy = int(index_tip.x * frame_w), int(index_tip.y * frame_h)
            tx, ty = int(thumb_tip.x * frame_w), int(thumb_tip.y * frame_h)
            mx, my = int(middle_tip.x * frame_w), int(middle_tip.y * frame_h)

            distance_index_thumb = math.hypot(ix - tx, iy - ty)
            distance_middle_thumb = math.hypot(mx - tx, my - ty)

            # LEFT CLICK
            if distance_index_thumb < 30 and click_cooldown == 0:
                pyautogui.click()
                click_cooldown = 10  # Delay next click

            # RIGHT CLICK
            elif distance_middle_thumb < 30 and click_cooldown == 0:
                pyautogui.click(button='right')
                click_cooldown = 10

    # Cooldown counter to prevent multi-click
    if click_cooldown > 0:
        click_cooldown -= 1

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
