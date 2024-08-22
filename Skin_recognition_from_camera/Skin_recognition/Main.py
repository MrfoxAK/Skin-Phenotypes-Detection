# import imghdr
from ast import If
from asyncio.windows_events import NULL
from email.mime import image
from tkinter import Frame
from cv2 import *
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont
from asyncore import write
from cgitb import text
import cv2
from numpy import size

cap = cv2.VideoCapture(0)         #Runtime cam start

# ret, frame = cap.read()
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('y'):
        cv2.imwrite('C:/Users/AKASH/OneDrive/Desktop/Skin_recognition_deb/Skin_recognition/test.jpg',frame)
        break

cap.release()
cv2.destroyAllWindows()           #runtime cam ends

#n = input("Enter File Name : ")

img = Image.open("C:/Users/AKASH/OneDrive/Desktop/Skin_recognition_deb/Skin_recognition/test.jpg")
# img1=cv2.imread('test.jpg')
im = ImageOps.grayscale(img)

def output_image() :
    im.show()

pixels = img.load()
height, width=img.size

k=0
avg=0
for x in range (height):
        for y in range (width):
            r,g,b = pixels[x,y]
            avg=avg+r
area=height*width
avg=avg/area
lim=avg+((255-avg)*70/100)
for x in range (height):
    for y in range (width):
        r,g,b = pixels[x,y]
        if(r>=lim and g>=lim and b>=lim):
            k=k+1


# for oily

with open('oily.txt') as f:
    # content = f.readlines()
    l = []
    for i in f:
        l.append(i.strip('\n'))
# l.sort()
# print(l)
# size = len(l)
# print(size)
# index = int(((size+1)/2)-1)
# print(l[index])
# level = int(sum(l)/size)

# print(level)

# print("\n")

# # for dry 

with open('dry.txt') as f:
    # content = f.readlines()
    l1 = []
    for j in f:
        l1.append(j.strip('\n'))
# l1.sort()
# print(l1)
# size1 = len(l1)
# print(size)
# index1 = int(((size1+1)/2)-1)
# print(index)

#level1 = int(sum(l1)/size1)

# print(level1)

dif=float(l[0])-float(l1[0])
sig_lev_1 = float(l[0])-(dif/2)
# print("The dif is",dif)
sig_lev_2 = float(l[0])-(dif/2) - (dif*38/100)
per = (k-sig_lev_1) / (dif*50/100) *100
if(k>=sig_lev_1):
#     if(k<float(l[0])):
    name="Oily Skin "
elif(k<=sig_lev_2):
    name="Dry Skin"
elif(k>sig_lev_2 and k<sig_lev_1):
    name="Mixed"

I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('FreeMono.ttf', 65)
I1.text((100, 100), name,font=myFont, fill=(0, 255, 0))   
if(k<float(l[0]) and k>=sig_lev_1):
    I1.text((150, 150), str(per)+"%",font=myFont, fill=(0, 255, 0))  
img.show()
# im.show(name)
print(k,avg,sig_lev_1,sig_lev_2,lim)