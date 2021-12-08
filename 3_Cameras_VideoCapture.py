# multiple window image open show at once, how do one after another? - order of .destroyAllWindows matters
import cv2

image1=cv2.imread('assets/heheCat.png',cv2.IMREAD_COLOR)
cv2.imshow('im 1',image1)


cv2.waitKey(0)

cv2.destroyAllWindows()
image2=cv2.imread('assets/rotatedCatuwu.jpg',cv2.IMREAD_COLOR)
cv2.imshow('im 2',image2)

cv2.waitKey(0)

cv2.destroyAllWindows()

#############################################################################
# displaying capture device
import numpy as np
import cv2

capture=cv2.VideoCapture(0)
    # 0 1 2 -> for if multiple webcam 0 for default 
# can also load video presaved
    # cap=cv2.VideoCapture('path/video.extension')
while True:
    ret,frame=capture.read()
        # getting a frame from video capture device
        # cap.read() returns frame{image itself which is a numpy array} and ret is if capture works properly

    cv2.imshow('capturedFrame',frame)

    if cv2.waitKey(1)==ord('q'):
        # waitkey(1) : 1 millisecond, its gonna wait 1 millisecond and if it gets to 1 millisecond we'll just move on after that , but if we press a key within that millisecond its gonna capture and return the ordinal/ascii value of key pressed
        # waitkey(1) : every 1 millisecond frame captured, can change time to affect performance and interval
            # increasing millisecond increases lag reduces overhead on host system but accuracy decreased as well
        # ord('q') ord is ordinal value{ascii value} of here 'q' since .waitKey(1) also captures which key pressed can compare if confirm to quit on 'q' pressed only and avoid if any other key pressed don't quit
        break

capture.release()
    # release capture device resource
cv2.destroyAllWindows()

#############################################################################

# create roatated mesh of 4 images of face captured from webcam
    # mirroring video multiple times
import numpy as np
import cv2

capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()

    # get width and height of captured image
    width=int(capture.get(3))
            # 3 is index of width 
            # use int to convert from default floating point value to integer
    height=int(capture.get(4))
            # 4 is index of height
            # use int to convert from default floating point value to integer
            # can also
                # widht,height=int(capture.get(3)),int(capture.get(4))
    # capture.get(1:17) has 17 different properties get them by using apt index

    image=np.zeros(frame.shape,dtype=np.uint8)
                # space/iterator to fill  , datatype of array values {uint8 unsigned int 8 bit} 
        # for creating a blank canvas use numpy.zeros() fills the shape{rows,columns,channel} with all zeroes{ 0 is black by default acts as a canvas}
        # also for frame bounds use captured frame.shape

    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    
    # copy portion in quadrants here
    image[:height//2,:width//2]=smaller_frame
        # starting : to height/2
        # top left
    # bottom left
    image[height//2:,:width//2]=smaller_frame

    # top right
    image[:height//2,width//2:]=smaller_frame
    # bottom right
    image[height//2:,width//2:]=smaller_frame

    cv2.imshow('canVas',image)
                # now show canvas image not frame


    if cv2.waitKey(1)==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

#############################################################################
# rotating and greyscaling individual quadrants
import numpy as np
import cv2

capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()

    # get width and height of captured image
    width=int(capture.get(3))
            # 3 is index of width 
            # use int to convert from default floating point value to integer
    height=int(capture.get(4))
            # 4 is index of height
            # use int to convert from default floating point value to integer
            # can also
                # widht,height=int(capture.get(3)),int(capture.get(4))
    # capture.get(1:17) has 17 different properties get them by using apt index

    image=np.zeros(frame.shape,dtype=np.uint8)
                # space/iterator to fill  , datatype of array values {uint8 unsigned int 8 bit} 
        # for creating a blank canvas use numpy.zeros() fills the shape{rows,columns,channel} with all zeroes{ 0 is black by default acts as a canvas}
        # also for frame bounds use captured frame.shape

    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    
    # copy portion in quadrants here
    image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180_CLOCKWISE)
        # starting : to height/2
        # top left
    # bottom left
    image[height//2:,:width//2]=smaller_frame

    # top right
    image[:height//2,width//2:]=cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180_CLOCKWISE)
    # bottom right
    image[height//2:,width//2:]=smaller_frame

    cv2.imshow('canVas',image)
                # now show canvas image not frame


    if cv2.waitKey(1)==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
#########################################################################
# we could have also used frame.shape[1] instead of cap.get(3) as well as for height

# Great video as always Tim. For anyone who is interested, here is a function to rotate the image to any chosen angle.
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]

    
#     # set rotation point as center of image if not specified
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)

#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width,height)

#     return cv.warpAffine(img, rotMat, dimensions)

#############################################################################

# Btw, you can still do it with the 4 different rotations if they are all squares.  It looks really trippy...
# Here's the code:

# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     h = frame.shape[0]
#     w = frame.shape[1]
#     strip = abs(w - h)//2
#     edge = min(w, h)

#     square = np.zeros((edge, edge, frame.shape[2]), np.uint8)
#     square = frame[:, strip:-strip]

#     small = cv2.resize(square, (0, 0), fx=0.5, fy=0.5)

#     square[:edge//2, :edge//2] = cv2.rotate(small, cv2.ROTATE_90_CLOCKWISE)
#     square[edge//2:, :edge//2] = cv2.rotate(small, cv2.ROTATE_180)
#     square[:edge//2, edge//2:] = cv2.rotate(small, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     square[edge//2:, edge//2:] = small

#     cv2.imshow('frame', square)

#     if cv2.waitKey(1) == ord('p'):
#         break

# cap.release()
# cv2.destroyAllWindows()