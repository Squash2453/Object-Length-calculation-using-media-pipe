import cv2
import mediapipe as mp
import math


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Middle finger real length (cm)
HAND_LENGTH_CM = 5  

cap = cv2.VideoCapture(0)

# Mode: 1 = one hand, 2 = two hands
mode = 1

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    pixels_per_cm = None
    left_thumb = None
    right_thumb = None

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm = hand_landmarks.landmark
            label = handedness.classification[0].label

            # Middle finger reference
            if label == "Right":
                m_base = (int(lm[17].x * w), int(lm[17].y * h))
                m_tip  = (int(lm[20].x * w), int(lm[20].y * h))


                ref_px = math.dist(m_base, m_tip)

                if ref_px > 0:
                    pixels_per_cm = ref_px / HAND_LENGTH_CM
                    # cv2.line(frame, m_base, m_tip, (255,255,0), 3)

                # Right thumb
                right_thumb = (int(lm[4].x * w), int(lm[4].y * h))
                
                
                



            # Left thumb
            if label == "Left":
                left_thumb = (int(lm[4].x * w), int(lm[4].y * h))
                

            # Index finger
            index_tip = (int(lm[8].x * w), int(lm[8].y * h))
            

    # -------------------------------
    # ONE HAND MODE
    # -------------------------------
    if mode == 1 and right_thumb and pixels_per_cm:
        dist_px = math.dist(right_thumb, index_tip)
        length_cm = dist_px / pixels_per_cm
        cv2.circle(frame, right_thumb, 2, (0,0,255), 3)
        cv2.circle(frame,index_tip,2,(0,0,255),3)
        mid=((right_thumb[0] + index_tip[0])//2,(right_thumb[1] + index_tip[1])//2)
        cv2.line(frame, right_thumb, index_tip, (0,0,255), 2)
        cv2.putText(frame, f"{length_cm:.1f} cm",
                    mid,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)

    # -------------------------------
    # TWO HAND MODE
    # -------------------------------
    if mode == 2 and left_thumb and right_thumb and pixels_per_cm:
        dist_px = math.dist(left_thumb, right_thumb)
        length_cm = dist_px / pixels_per_cm
        cv2.circle(frame, right_thumb, 3, (0,0,255), 3)

        cv2.line(frame, left_thumb, right_thumb, (0,0,255), 2)
        mid = ((left_thumb[0]+right_thumb[0])//2, (left_thumb[1]+right_thumb[1])//2)
        cv2.circle(frame, left_thumb, 3, (0,0,255), 3)

        cv2.putText(frame, f"{length_cm:.1f} cm",
                    (mid[0]-40, mid[1]-20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    # -------------------------------
    # UI
    # -------------------------------
    cv2.putText(frame, f"Mode: {'One Hand' if mode==1 else 'Two Hands'}",
                (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 3)


    cv2.putText(frame, "Press 1 = One Hand   2 = Two Hands   Q = Quit",
                (10, h-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,200,200), 2)

    cv2.imshow("Dual Mode Hand Measurement", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2
    elif key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
