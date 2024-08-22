# import imghdr
from ast import If
from email.mime import image
from tkinter import Frame
from cv2 import *
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont
from asyncore import write
from cgitb import text
import cv2
from numpy import size

import hsv

cap = cv2.VideoCapture(0)

# ret, frame = cap.read()
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('y'):
        cv2.imwrite('C:/Users/debsp/OneDrive/Desktop/FACE/test.jpg',frame)
        break

cap.release()
cv2.destroyAllWindows()
img = Image.open("test.jpg")
x=hsv.detect()

#n = input("Enter File Name : ")
if(x==0):
    
# img1=cv2.imread('test.jpg')
    im = ImageOps.grayscale(img)

    def output_image() :
        im.show()

    pixels = img.load()
    height, width=img.size

    k=0

    for x in range (height):
        for y in range (width):
            r,g,b = pixels[x,y]
            if(r>=160 and g>=160 and b>=160):
                k=k+1

    area=height*width



    with open("dry.txt") as f1:
        l1 = []
        for i in f1:
                l1.append(i.strip('\n'))

    with open("oily.txt") as f2:
        l2 = []
        for i in f2:
                l2.append(i.strip('\n'))

    dif=int(l2[0])-int(l1[0])
    sig_lev=int(l2[0])-(dif/2)
    per=100-((int(l2[0])-k)/dif)

    print(k,sig_lev)
    name=0

    if(k>=sig_lev):
        name="Oily Skin"
    else:
        name="Dry Skin"

    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('FreeMono.ttf', 65)
    I1.text((100, 100), name,font=myFont, fill=(255, 0, 0))   
    img.show()
    # im.show(name)
    #print(k,b)
else:
    name="Skin Can't be recognised"
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('FreeMono.ttf', 35)
    I1.text((100, 100), name,font=myFont, fill=(0, 0, 255))   
    img.show()
    # im.show(name)