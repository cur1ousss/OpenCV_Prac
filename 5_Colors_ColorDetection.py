    # RGB red green blue {red significant area occupies}
    # BGR blue green red {blue significant area occupies}
    # HSV hue saturation and lightness/brightness

# goal - to show only specific colored objects in live webcam image
##############################################################################

# converting normal frame into HSV color scheme
    # reason we need to convert to HSV is because the method we are going to use to extract the color from the image requires an HSV image , so all colors need to be HSV hence need to convert image to HSV
import numpy as np
import cv2

capture=cv2.VideoCapture(0)

while True:
    ret,frame=capture.read()
    width=int(capture.get(3))
    height=int(capture.get(4))

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    cv2.imshow('frame',hsv)     # displays by default in bgr format , but we inputted here hsv hence output colors strange since interpreting hsv as bgr , pixels being read in a weird fashion

    if cv2.waitKey(1)==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


#############################################################################
# converting normal frame into HSV color scheme {using masking {mask}}

import numpy as np
import cv2

# convertin BGR to HSV , use that hsv image to extract separate colors

capture=cv2.VideoCapture(0)

while True:
    ret,frame=capture.read()
    width=int(capture.get(3))
    height=int(capture.get(4))

        # converting frame bgr to hsv color scheme
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # now we need to define colors that we want to extract from the image above converted to HSV image from BGR 
        # pick lower_bound {lower_blue} and upper_bound{upper_blue} for the color/pixel we want to extract {colors between this range will be picked/extracted}
   
# selecting lower and upper bound to display color 2 ways:
        # lowerBlue=np.array(['HSV color code']) 
                # pick hsv color code using picker wheel from net { There's a better way to get ur hsv range values. There's some program where u can use sliders to set hsv ranges to get a proper masking of the image. It's a hsv color thresholder. I got this from stack overflow :  https://stackoverflow.com/a/59906154 
    # OR 2nd approach below
        # work pixel by pixel {selecting lower bound blue for HSV -> convert lower bound blue of BGR to HSV using cvtColor method}
            # BGR_color = np.array([[[255,0,0]]])
            # x = cv2.cvtColor(BGR_color,cv2.COLOR_BGR2HSV) # returns array of hsv format [[[]]] stored to x
            # accessing one color/pixel of x 
                # x[0][0]
                            # misc. in background -> cv2.cvtColor([[[255,0,134]]],cv2.COLOR_BGR2HSV)
                                    # cvtColor expects image not single pixel hence convert single pixel to image format using three '[]'  brackets [[[]]]

    lower_blue=np.array([90,50,50]) # light blue
    upper_blue=np.array([130,255,255]) # dark blue
            # these might be RGB values upper and lower bound
                    # crosscheck https://alloyui.com/examples/color-picker/hsv.html more ref needed

    # now creating a mask
        # mask is part/portion of an image {tells which area to keep (example in editing software)}
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
                # pass image, lowerBound, upperBound
        # returns/ tells us what pixels are in range bound and what not later can convert not in range to blackout 

    # using above returned mask that has only colors between lower and upper color bound; rest are blacked out 0,0,0 since bitwise and {mask is used as a function mapping frame <-> frame and'ing}
    result=cv2.bitwise_and(frame,frame,mask=mask)
            # if pixel blue 1  &&  1  = 1
            #               0 && 0 =  0
            # blending image together using mask {since single image img1=img2 {src1=src2} }
    # OBSERVATIONS (bitwise_and(arguments)):
        # hsv hsv  idnty yes color orangish
        # hsv frame idnty yes color greenish
        # frame hsv idnty yes color greenish
        # frame frame idnty yes prefecto blue

    cv2.imshow('frame',result)    # result image after mask
    cv2.imshow('Mask',mask)     # mask is array of 0 and 1 , above declration if inRange() then 1 otherwise value 0 of that pixel {so mask window appears black and white}
    cv2.imshow('Original',frame)
    
    if cv2.waitKey(1)==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()