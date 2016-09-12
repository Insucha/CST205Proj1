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

#Secondly, we define functions:

def bwFilter (img):
    img = img.convert('L')
    img.show()

def secFilter (img):
    img = img.convert('1')
    img.show()




theImages = []

#Next, showing the path to my .py project

imagePath = "/Users/Darya/Desktop/CST205Project1/ProjectImages/"

#I assign the range from 1 to 9:

for myImage in range(1,10):

    theImages.append(Image.open(imagePath + str(myImage) + ".png"))

"""
    I create a if-else statement that will make my odd photos black and white
    and all my even photos Edgy through Functions.
"""

#Beginning with the first image, we create an if-else statement:

myCounter = 0
for aImage in theImages:
    if (myCounter%2 == 1):
        
        bwFilter(theImages[myCounter])
    else:
        secFilter(theImages[myCounter])

    myCounter = myCounter + 1
