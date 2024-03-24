import cv2
from time import time


class Scanner:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.qr_detector = cv2.QRCodeDetector()

    def read_input(self):
        while True:
            _, image = self.video_capture
            data, bbox, _ = self.qr_detector.detectAndDecode(image)

            if bbox is not None:
                if data:
                    print("data:", data)
                    return data
