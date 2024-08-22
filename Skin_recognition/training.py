# import imghdr
from cgitb import text
import cv2
# import numpy as np
from PIL import Image,ImageOps
import glob
# from elevate import elevate
import train_test as ts

# elevate()
# name=input("Enter path")
# text=input("enter text file name")
path = glob.glob("C:/Users/debsp/Downloads/Skin_recognition/Oily/*.jpg")

for i in path:
    # img = cv2.imread(i)
    # cv2.imshow("image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img = Image.open(i)
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
    lim=(avg)+((255-avg)*70/100)
    for x in range (height):
        for y in range (width):
            r,g,b = pixels[x,y]
            if(r>=lim and g>=lim and b>=lim):
                k=k+1


    
    # input_image()
    print(k ,"area=",area)
    ks=str(k)
    f = open("oily.txt","a")
    val = k
    a = f.write(f"{val}\n")
    f.close()
    output_image()
    cv2.waitKey(0)

ts.mean("oily.txt")
