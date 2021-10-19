# coding: utf-8
# -------------------------------------------------------- #
#               Just a basic security camera               #
# -------------------------------------------------------- #

import cv2

# open webcam (import video)
video_capture = cv2.VideoCapture('video.mp4')
# webcam : video_capture = cv2.VideoCapture(0)

# read first frame
_, current_frame = video_capture.read()

# convert to grayscale
current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

# Main UI loop
while True:
    
    # Read in the next valid frame (and convert to grayscale)
    _, current_frame = video_capture.read()
    if current_frame is None:
        break
# TODO : compare two frame
# TODO : display the video/wwebcam feed

cv2.imshow('app', current_frame)
cv2.waitKey(1)

video_capture.release()
cv2.destroyAllWindows