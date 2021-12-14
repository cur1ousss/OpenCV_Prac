# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
# https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html

# shi tomasi corner detection used below

import numpy as np
import cv2

img=cv2.imread('assets/chessboard.png')
        # # if you are using webcam for this tutorial use the code below to convert BGR2GRAY
        # ret,frame = cap.read()
        # img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('frame',img)

img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)

# corner detection algorithms work better on gray scale images hence convert input bgr rbg image to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # will detect corner location on grayscale image but later draw on colored image for end user , also since location(of corners), size pixel(of image) remains same end result not affected

corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)
        # pass source image{image you want to detect corners from}, best N corners count you want to return, quality of corner(0,1 floating point range){aka degree of confidence}, minimum eucledian distance between corners that are returned {since if round corner points maybe 500 on same round curve false corners}
# by default value of corners returned is in floating point so convert to int
# since .goodFeaturesToTrack() returns np.array()
corners=np.int0(corners)
        # converting numpy array floating point to numpy array integer

for corner in corners:
        x,y=corner.ravel()
                # ravel() method of numpy helps flatten an array
                        # meaning since returned array is of form [[[1,2]],[[11,13].....]
                        # flattend output will assign x 1 y 2  x 11 y 13
# now to draw the corner
        cv2.circle(img,(x,y), 5 , (255,0,0),-1)
                # image, centre, radius , bgr , fill

# drawing randomly colored lines between corners
for i in range(len(corners)):
        for j in range(i+1,len(corners)):
                corner1=tuple(corners[i][0])
                corner2=tuple(corners[j][0]) # since corners if of list form convert to tuple

                color=tuple(map(lambda x: int(x),np.random.randint(0,255,size=3)))
                           # lowerBound, higherBound , number of random samples to pick
                        # numpy has 32,64 bit integers but python uses 8 bit integer need to convert to python compatabile, also randint() returns list convert that
                        # 2.Instead of the map(lambda... for the np.random.randint you can also tuple a comprehension for the function.
                                #  color = tuple(int(x) for x in np.random.randint())
                        # 3. Just in case you're not a fan of the map function, try:
                                # color = [int(x) for x in np.random.randint(0, 255, size=3)]
                cv2.line(img,corner1,corner2,color,1)
                        # indenting this line separately to make 1 point to many etc...

cv2.imshow('windowPopup',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

        # some border extreme black region may fail to detect corner

#############################################################################
# Corner detection in live webCam

import numpy as np
import cv2

capture=cv2.VideoCapture(0)

while True:

    ret,frame=capture.read()
    img=frame
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)
    corners=np.int0(corners)

    for corner in corners:
            x,y=corner.ravel()
            cv2.circle(img,(x,y), 5 , (255,0,0),-1)

    for i in range(len(corners)):
            for j in range(i+1,len(corners)):
                    corner1=tuple(corners[i][0])
                    corner2=tuple(corners[j][0]) # since corners if of list form convert to tuple

                    color=tuple(map(lambda x: int(x),np.random.randint(0,255,size=3)))
            cv2.line(img,corner1,corner2,color,1)
    cv2.imshow('windowPopup',img)

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()