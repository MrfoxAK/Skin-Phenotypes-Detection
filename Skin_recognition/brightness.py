from audioop import avg
from mimetypes import init
import cv2
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont

class bright():
    def brightness():
        av=0
        im=cv2.imread("opencv0.png")
        hsv=cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        im_pil=Image.fromarray(hsv)
        pixels = im_pil.load()
        h,w=im_pil.size
        im_pil.show()
        for x in range(h):
            for y in range(w):
                h,s,v=pixels[x,y]
                av=v+av
        av=av/(h*w)
        print(av)
        return av
    # brightness()
if __name__ == '__main__':
    bright.brightness()