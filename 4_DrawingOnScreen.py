import cv2
import numpy as np

capture=cv2.VideoCapture(0)

while True:
    ret,frame=capture.read()
    width=int(capture.get(3))   # capture.get() returns floating point width height hence convert to int for scaling better
    height=int(capture.get(4))

    # drawing lines
    image=cv2.line(frame        ,   (0,0)     ,(width,height), (255,0,0)  ,10)
    # pass image to draw line onto , start,     end     color of line(BGR value), thickness of line(pixels thick)
                # coordinate system in openCV   
                        # top left corner is (0,0) horizontal is x axis, vertical screen y axis


    # drawing multiple lines , use above as base not source frame as base
    image=cv2.line(image, (0,height) ,(width,0),(0,255,0),10)

    cv2.imshow('frameWindow',image)

    if cv2.waitKey(1)==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

#############################################################################
# making crosshair csgo edshot maaashine scream kennys niko s1mple

import cv2

vidCapture=cv2.VideoCapture(0)

while True:

    ret,frame=vidCapture.read()

    width=int(vidCapture.get(3))
    height=int(vidCapture.get(4))

    img=cv2.line(frame,(width//2,height//2-10),(width//2,height//2+10),(255,255,255),3)

    img=cv2.line(img,(width//2-10,height//2),(width//2+10,height//2),(255,255,255),3)

    cv2.imshow('capture',img)
    
    print(f'width{width} height{height}')

    if cv2.waitKey(1)==ord('q'):
        break

vidCapture.release()
cv2.destroyAllWindows()

#############################################################################

# Drawing Rectangle & Circles

import cv2

capture=cv2.VideoCapture(0)

while True:
    ret,frame=capture.read()
    width=int(capture.get(3))
    height=int(capture.get(4))

    image=cv2.line(frame  ,   (0,0)     ,(width,height), (255,0,0)  ,10)
    image=cv2.line(image, (0,height) ,(width,0),(0,255,0),10)

# for rectangle Pass Top left corner, bottom right corner, color , line thickness (-1 to fill, + int for boundary thickness ,(0 gives thin line boundary))
    img=cv2.rectangle(image,(100,100),(200,200),(213,132,314),5)

# for Circle Pass centre position, radius, color , thickness(-1 for fill, + int for boundary thickness(0 gives thin boundary))
    img=cv2.circle(img,(width//2,height//2),60,(0,0,255),-1)


    cv2.imshow('frameWindow',img)

    if cv2.waitKey(1)==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

#############################################################################

# Drawing Text on Screen
    # make font first
    # anti aliasing, location,color

import cv2

vidCap=cv2.VideoCapture(0)

while True:
    ret,frame=vidCap.read()

    width=int(vidCap.get(3))
    height=int(vidCap.get(4))

    image=cv2.line(image, (0,height) ,(width,0),(0,255,0),10)

    # setting font
    font=cv2.FONT_HERSHEY_SIMPLEX
    image=image.putText(frame,'Tim is Great!',(200,height-10),font,4,(131,234,156), 5, cv2.LINE_AA)
            # base image canvas{default frame or modified img},text, Bottom left corner location(center location) , font , fontScale(is relative magnification), color, line thickness, lineType cv2.LINE_AA    , optional argument for font 

    cv2.imshow('vidCapture',image)
    if cv2.waitKey(1)==ord('q'):
            # needs to be atleast 1 to capture live webcam , 0 gets only single image screenshot kinda
        break

vidCap.release()
cv2.destroyAllWindows()

#############################################################################
# using all concepts above Program 
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Tim is Great!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()