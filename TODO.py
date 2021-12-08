# make 4 quadrants 1 slower then slower and slower
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

                smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=1)
                

                image[:height,:width//2]=smaller_frame
                    # starting : to height/2
                    # top left
                # bottom left
                image[:height,width//2:]=smaller_frame

            
                cv2.imshow('canVas',image)
                            # now show canvas image not frame

                
                if cv2.waitKey(1)==ord('q'):
                    break
            



capture.release()
cv2.destroyAllWindows()

#############################################################################
# snapchat kinda filter left side normal speed right half fast or slow
    # use as an import so code run in background
    # use one below other while loop

import cv2 
import numpy as np

capture1=cv2.VideoCapture(0)
capture2=cv2.VideoCapture(0)

while True:
    ret,frame1=capture1.read()

    # get width and height of captured image
    width=int(capture1.get(3))
            # 3 is index of width 
            # use int to convert from default floating point value to integer
    height=int(capture1.get(4))
            # 4 is index of height
            # use int to convert from default floating point value to integer
            # can also
                # widht,height=int(capture.get(3)),int(capture.get(4))
    # capture.get(1:17) has 17 different properties get them by using apt index

    image=np.zeros(frame1.shape,dtype=np.uint8)
                # space/iterator to fill  , datatype of array values {uint8 unsigned int 8 bit} 
        # for creating a blank canvas use numpy.zeros() fills the shape{rows,columns,channel} with all zeroes{ 0 is black by default acts as a canvas}
        # also for frame1 bounds use captured frame1.shape

    smaller_frame1=cv2.resize(frame1,(0,0),fx=0.5,fy=1)
    
    # copy portion in quadrants here
    image[:height,:width//2]=smaller_frame1
        # starting : to height/2
        # top left
    # bottom left
    image[:height,width//2:]=smaller_frame1


    cv2.imshow('canVas',image)
                # now show canvas image not frame11

    if cv2.waitKey(500)==ord('x'):
        pass
    if cv2.waitKey(1)==ord('q'):
        break

capture1.release()
capture2.release()
cv2.destroyAllWindows()