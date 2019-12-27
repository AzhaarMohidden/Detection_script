import cv2
def drawHex(x, y, size, B, G, R, line_thick, img):
        #scale dependes on the angle of slant of the line and is the inverse tangent of the angle
        l_scale = int(size/1.73)
        size_s = size - (size/2)
        ls_scale = int(size_s/1.73)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        #initaiate position of each line starting point => x, y
        x2 = x + l_scale; x3 = x2 - l_scale; x4 = x3 - size; x5 = x4 - l_scale; x6 = x; xf = x+ls_scale
        y2 = y + size; y3 = y2 + size; y4 = y3; y5 = y4 - size; y6 = y; yf = y-size + size_s - 4
# draw line
# Hexagon
        cv2.line(img,(x,y),(x+l_scale,y+size),(B,G,R),line_thick)
        cv2.line(img,(x2,y2),(x2-l_scale,y2+size),(B,G,R),line_thick)
        cv2.line(img,(x3,y3),(x3-size,y3),(B,G,R),line_thick)
        cv2.line(img,(x4,y4),(x4-l_scale,y4-size),(B,G,R),line_thick)
        cv2.line(img,(x5,y5),(x5+l_scale,y5-size),(B,G,R) ,line_thick)
        cv2.line(img,(x6,y6),(x6-size,y6),(B,G,R),line_thick)
#Name line
        cv2.line(img,(x,y),(x+ls_scale,y-size + size_s),(B,G,R),line_thick)
        cv2.line(img,(x+ls_scale,y-size + size_s),(x+size*2,y-size + size_s),(B,G,R),line_thick)
#text
        cv2.putText(img,'sample text',(xf,yf), font, fontScale, (B,G,R), line_thick, cv2.LINE_AA)
