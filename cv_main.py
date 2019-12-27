import cv2
from drwhx import cv_draw_hex as drw
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    B = 150; G = 200; R = 0
    drw.drawHex(150,150, 70, B ,G, R, 2,  img)
    cv2.imshow('image', img)
    cv2.waitKey(10)
cv2.destroyAllWindows()
