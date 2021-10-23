# USAGE
# python CamTest.py

# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os

vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    # grab the frame from video stream
    frame = vs.read()

    # Add your code HERE

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
