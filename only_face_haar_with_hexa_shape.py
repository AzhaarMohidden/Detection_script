import numpy as np
import cv2
from drwhx import cv_draw_hex as drw

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("rtsp://admin:cltadmin12@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1")

B = 150; G = 200; R = 0
text = "Person"
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    for (x,y,w,h) in faces:
        drw.drawHex(x+int(w*(0.7)),y, (int(h/2)), B ,G, R, 1,  img, text)
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
