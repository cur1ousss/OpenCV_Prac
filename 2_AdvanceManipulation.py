import cv2

image1=cv2.imread('assets/heheCat.png',cv2.IMREAD_COLOR)

print(image1)
    # prints as numpy array of rgb vales 0 .. 255
    # openCV and numpy are closely related 
    # so when load an image using imread() it extracts into form of numpy array
print(type(image1))

# iamge1.shape attribute prints number of rows, number of columns, number of channels in my image1
#   [[137 169 175]
#   [139 171 177]
#   [143 172 179]
#   ...
#   [125  95  16]
#   [124  94  15]
#   [123  93  14]]

# rows is height of my image
# columns is width of my image
# channels is color space of my image - B G R in openCV unlike RGB
print(image1.shape)
    # (524, 500, 3)
    # height width B G R 

# used earlier cv2.rotate() can also manually implement it by rotating values in numpy array representation which happens under the hood

########################################################################
# Accessing Pixel Values
print(image1[230]) # row 230 
print(image1[230][45:400]) # 45 to 400 pixel inside the row
print(image1[230][400]) # looking at specific pixel

##############################################################################
# Changing Pixel Manually in image
import cv2
import random
image2=cv2.imread('assets/heheCat.png',cv2.IMREAD_COLOR)

for i in range(100):
    for j in range(image2.shape[1]): 
        # .shape() gives rows colums channels
                # #####    0   1    2  index
        image2[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        # random.randint(low,high) - gives random value between low high extremities

cv2.imshow('WindowNew',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#############################################################################
# Copying Pasting one part of image to Another

# numpy array slice - like regular slice in python except we can do it twice inside
import cv2
image2=cv2.imread('assets/heheCat.png',cv2.IMREAD_COLOR)

tag=image2[500:700,600:900]
# copy from 500 to 700 row , columns from 600: to 900
# not including 700
image2[100:300,650:950]=tag
# replace this part of image with = tag part
    # difference must be same example replacing 200 pixels with 200 pixels 700-500 = 300-100 part row and 900-600 = 950-650 part column of patch

cv2.imshow('popUpWindow',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# doubt- Multiple image window popUp from same code? after key hit all close or fall flat one by one