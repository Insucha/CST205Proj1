"""
Darya Yanouskaya
CST205
Project requires application of black-and-white filter to every odd-numbered
Image out of 9 possible. Every even-numbered image should have any other
filter apart from the black-and-white applied.
"""

#First we import images, import libraries from Pillow
from __future__ import print_function
from PIL import Image
from PIL import ImageFilter

theImages = []


#I am showing the path to my .py project
imagePath = "/Users/Darya/Desktop/CST205Project1/ProjectImages/"

#I assign the range from 1 to 9:
for myImage in range(1,10):

    theImages.append(Image.open(imagePath + str(myImage) + ".png"))

"""
I create a loop that will make my odd photos black and white
and all my even photos Blurred and Edgy
"""

#Beginning with the first image, we create an if-else statement:

myCounter = 0
for aImage in theImages:
    if (myCounter%2 == 1):
        aImage= aImage.convert('L')
        aImage.show()
    else:
        aImage = aImage.filter(ImageFilter.FIND_EDGES)
        aImage = aImage.filter(ImageFilter.BLUR)
        aImage.show()

    myCounter = myCounter + 1
