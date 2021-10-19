# coding: utf-8
# -------------------------------------------------------- #
#               Just a basic security camera               #
# -------------------------------------------------------- #

import cv2

# open webcam (import video)
video_capture = cv2.VideoCapture('security-camera/video.mp4')
# webcam : video_capture = cv2.VideoCapture(0)

# read first frame
_, current_frame = video_capture.read()

# convert to grayscale
current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

cv2.imshow ('app', current_frame)
cv2.waitKey(0)

video_capture.release()
cv2.destroyAllWindows