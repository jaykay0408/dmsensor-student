# USAGE
# python imagestill.py

# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os

vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(1.0)
i = 0                           # Image sequence

# loop over the frames from the video stream
while True:
    # grab the frame from video stream
    frame = vs.read()

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # if the `s` key was pressed, save current image
    if key == ord("s"):
        filename = "test" + str(i) + ".png"
        cv2.imwrite("./data/" + filename, frame)
        print(filename + " is saved.")
        i += 1

cv2.destroyAllWindows()
vs.stop()
