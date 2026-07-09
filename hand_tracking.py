import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.draw = mp.solutions.drawing_utils

    def get_flap(self):

        success, frame = self.cap.read()

        if not success:
            return False

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        flap = False

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                self.draw.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

                tip = hand.landmark[8]

                h, w, _ = frame.shape

                x = int(tip.x * w)
                y = int(tip.y * h)

                cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

                # Finger in upper half = flap
                if y < h // 2:
                    flap = True

        cv2.imshow("Hand Tracking", frame)
        cv2.waitKey(1)

        return flap

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()