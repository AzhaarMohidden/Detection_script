#!/usr/bin/env python
# Shows webcam without any changes:
# testing if webcam opencv module works:
#> result view of the webcam

import numpy as np
import cv2

cap = cv2.VideoCapture("rtsp://admin:cltadmin12@192.168.1.193/cam/realmonitor?channel=1&subtype=1")

from pkg_resources import parse_version
OPCV3 = parse_version(cv2.__version__) >= parse_version('3')

def capPropId(prop):
  return getattr(cv2 if OPCV3 else cv2.cv,
    ("" if OPCV3 else "CV_") + "CAP_PROP_" + prop)

cap.set(capPropId("FRAME_WIDTH"), 640)
cap.set(capPropId("FRAME_HEIGHT"), 480)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('fra1me',frame)
        cv2.imwrite(filename='room_ser.jpg', img=frame)
        cv2.waitKey(10)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
