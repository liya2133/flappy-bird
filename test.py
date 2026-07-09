from hand_tracking import HandTracker
import cv2

tracker = HandTracker()

while True:

    flap = tracker.get_flap()

    if flap:
        print("FLAP!")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tracker.release()