import threading
from hand_tracking import HandTracker


class CameraThread:
    def __init__(self):
        self.tracker = HandTracker()
        self.running = True

        self.flap = False
        self.previous = False

        self.thread = threading.Thread(target=self.update)
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while self.running:

            current = self.tracker.get_flap()

            if current and not self.previous:
                self.flap = True
            else:
                self.flap = False

            self.previous = current

    def get_flap(self):
        return self.flap

    def stop(self):
        self.running = False
        self.thread.join()
        self.tracker.release()