from importlib.resources import path
import cv2
import numpy as np
from cgitb import text
import glob
import mean as m

path=glob.glob("C:/Users/debsp/OneDrive/Desktop/Face/non_skin/*.jpg")

for i in path:
    image=cv2.imread(i)
    im=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    h,w = image.shape[0], image.shape[1]

    avg_s=im[::1].mean()
    max_s=im[::1].min()
    print(avg_s)


f = open("non_skin.txt","a")
val = avg_s
a = f.write(f"{val}\n")
f.close()



m.mean("non_skin.txt")