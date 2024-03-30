import cv2
from gpiozero import Button


# Increasing IMAGES_MAX increased the likelyhood that card is correctly read, but increases compute time.
IMAGES_MAX = 5


class Scanner:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.qr_detector = cv2.QRCodeDetector()
        self.button = Button(2)
        self.images = []

    def read_input(self):
        while True:
            _, image = self.video_capture.read()
            self.images.append(image)

            if len(self.images) > IMAGES_MAX:
                self.images.pop(0)

            if self.button.is_pressed:
                for image_previous in self.images:
                    data, bbox, _ = self.qr_detector.detectAndDecode(
                        image_previous)
                    if bbox is not None:
                        if data:
                            return data

                return None
