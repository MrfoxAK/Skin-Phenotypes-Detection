# import imghdr
import cv2
# import numpy as np
from PIL import Image, ImageOps
import glob

path = glob.glob("C:/Users/AKASH/OneDrive/Desktop/Skin_recognition/Oily/*.jpg")
path1 = glob.glob("C:/Users/AKASH/OneDrive/Desktop/Skin_recognition/Dry/*.jpg")

for i in path:
    # img = cv2.imread(i)
    # cv2.imshow("image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img = Image.open(i)
    im = ImageOps.grayscale(img)

    def output_image():
        im.show()

    pixels = img.load()
    height, width = img.size

    k = 00

    for x in range(height):
        for y in range(width):
            r, g, b = pixels[x, y]
            if(r >= 200 and g >= 200 and b >= 200):
                k = k+1

    area = height*width
    # input_image()
    print(k)
    ks = str(k)
    f = open("oily.txt", "a")
    val = ks
    a = f.write(f"{val}\n")
    output_image()
    cv2.waitKey(0)
print("after")
for j in path1:
    # img = cv2.imread(i)
    # cv2.imshow("image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img1 = Image.open(j)
    im1 = ImageOps.grayscale(img1)

    def output_image():
        im1.show()

    pixels1 = img1.load()
    height1, width1 = img1.size

    k1 = 00

    for x1 in range(height1):
        for y1 in range(width1):
            r1, g1, b1 = pixels1[x1, y1]
            if(r1 >= 200 and g1 >= 200 and b1 >= 200):
                k1 = k1+1

    area1 = height1*width1
    # input_image()
    print(k1)
    ks1 = str(k1)
    f = open("dry.txt", "a")
    val1 = ks1
    a1 = f.write(f"{val1}\n")
    output_image()
    cv2.waitKey(0)
