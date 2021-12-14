# template matching
    # detecting template/image in another image

# template image should be of the same size/close to same size we need to locate in source image

# example locating football in soccer match
import numpy as np
import cv2

img=cv2.resize(cv2.imread('assets/soccer_practice.jpg',0),(0,0),fx=0.5,fy=0.5) # loading in grayscale since most algorithms in openCV for object detection work best in gray scale
template=cv2.resize(cv2.imread('assets/ball.png',0),(0,0),fx=0.5,fy=0.5)
    # template and base image should be resized by close or same factor otherwise wrong detection

img2=img.copy()
    # not img2=img since in that case refer to same memory location if one changed other also changes

height,width=template.shape
    # directly can load since shape of template here is an tuple unlike when earlier loaded a color image with shape of height,width,channels  since this here is grayScale image no Channels exist

# METHODS for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# diff methods may give different efficiency for different image hence try all
for method in methods:
    img3=img.copy()

    result=cv2.matchTemplate(img3,template,method)
        # matchTemplate() method performs convolution on image {basically slide template to match through image returning 2D array}
            # (W - w + 1, H - h +1) -> shows how many times slide in x axis,y axis // size of result Array
    minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(result)
        # as slider goes value changes and assigns 

    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
            # since for these methods minLoc works as result for others max works
        location=minLoc
    else:
        location=maxLoc

    bottomRight=(location[0]+width,location[1]+height)
    cv2.rectangle(img3,location,bottomRight,255,5)

    cv2.imshow('Match',img3) # line 23 Tim
        # At the end of the video, you don't need to resize the image at every step. Just resize where you are showing the image at line 23 as
            # cv2.imshow("Match", cv2.resize(img2, (0,0), fx=0.8, fy=0.8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()