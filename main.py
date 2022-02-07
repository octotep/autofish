import cv2
import mss
import numpy
import time
from pynput.mouse import Button, Controller

mouse = Controller()

with mss.mss() as sct:
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

    while True:

        # Snap the screen and turn it into data OpenCV can work with
        image = numpy.array(sct.grab(monitor))

        # Remove the alpha channel from the screenshot
        image = image[:,:,:3]

        template = cv2.imread("tests/true.png")

        result = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
        min_v, _, _, _ = cv2.minMaxLoc(result)

        print(min_v)
        if min_v < 5000000:
            print("Match found!")
            mouse.click(Button.right)
            time.sleep(1)
            mouse.click(Button.right)

