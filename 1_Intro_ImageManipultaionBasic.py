import cv2
# name used to install using pip is openCV but in code used import cv2

# loading an image
image1=cv2.imread('assets/heheCat.png',cv2.IMREAD_COLOR)
                    # path              # mode

# by default cv2 loads image in BGR blue green red , NOT RGB red green blue

# mode has 3 options
    # grayscale
    # normal as it is
    # without transparency {without considering alpha value of pixels} - example if want to remove transparent background load in this mode

        # cv2.IMREAD_COLOR / 1 : It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
            # in fedora 35 KDE IMREAD_COLOR also gives x,y coordinates and RGB value in bottom left per pixel

        # cv2.IMREAD_GRAYSCALE / 0 : It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
             # in fedora 35 KDE IMREAD_COLOR also gives x,y coordinates and RGB value in bottom left per pixel

        # cv2.IMREAD_UNCHANGED / -1 : It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag. Keeps Preserves transparency of image

 # better to use flag literal constant Values than integer value since vague for tutorials

# displaying image after loading
cv2.imshow('WindowLabelCustomXd',image1)
            # window label x     # image

cv2.waitKey(0)
    # waitKey(0) waits an infinite amount of time until key is pressed,means wait infinitely so will not go past this line of the program until we press a key
    # waitKey(5) would mean wait 5 seconds, if not press key within 5 seconds automatically gonna get skipped
cv2.destroyAllWindows()    
    # destroy opened windows so don't keep running in the background

#############################################################################

import cv2
image1=cv2.imread('assets/heheCat.png',cv2.IMREAD_COLOR)

# Resize and Rotatin Image
image1=cv2.resize(image1,(100,124))
                        # pixel X pixel 
    # resize in relative terms to original
image1=cv2.resize(image1,(0,0),fx=0.5,fy=0.5)
                            # fx=fy=0.5 for half height
                            # fx=fy=2 for double height

# Rotate image
image1=cv2.rotate(image1,cv2.ROTATE_90_CLOCKWISE)
image1=cv2.rotate(image1,cv2.cv2.ROTATE_90_CLOCKWISE)   # previous rotation also accounted for this rotation appends to previous rotation
    # also here used cv2.cv2.ROTATE_90_CLOCKWISE , earlier used cv2.ROTATE_90_CLOCKWISE
    # also available attributes ROTATE_180_CLOCKWISE , 180 ,270 etc


# Writing image
cv2.imwrite('assets/rotatedCatuwu.jpg',image1)
            # path/FileName.extension , manipulated_imagetoWrite
        # can cross code save png to jpg , png to png etc.


cv2.imshow('WindowLabelCustomXd',image1)
cv2.waitKey(0)
cv2.destroyAllWindows()    