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

cap = cv2.VideoCapture(0)

# ret, frame = cap.read()
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('y'):
        cv2.imwrite('C:/Users/AKASH/OneDrive/Desktop/Skin_recognition/test.jpg',frame)
        break

cap.release()
cv2.destroyAllWindows()

#n = input("Enter File Name : ")

img = Image.open("test.jpg")
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

# for oily

with open('oily.txt') as f:
    # content = f.readlines()
    l = []
    for i in f:
        l.append(int(i.strip('\n')))
l.sort()
print(l)
size = len(l)
# print(size)
# index = int(((size+1)/2)-1)
# print(l[index])
level = int(sum(l)/size)

print(level)

print("\n")

# for dry 

with open('dry.txt') as f:
    # content = f.readlines()
    l1 = []
    for j in f:
        l1.append(int(j.strip('\n')))
l1.sort()
print(l1)
size1 = len(l1)
# print(size)
# index1 = int(((size1+1)/2)-1)
# print(index)

level1 = int(sum(l1)/size1)

print(level1)

differ = level-level1
dif = (level-level1)/2 + 100
# print("The dif is",dif)


if(k>=level):
    name="Oily Skin"
elif(k<=level1):
    name="Dry Skin"
elif(k>dif):
    if(k<differ):
        name="Mixed"
elif(k<=dif):
    name="Dry Skin"

I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('FreeMono.ttf', 65)
I1.text((100, 100), name,font=myFont, fill=(255, 0, 0))   
img.show()
# im.show(name)
print(k,b)