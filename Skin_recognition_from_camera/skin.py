from tkinter import image_names
import numpy as np
import cv2
import sys
from PIL import Image
import os
import PIL
import glob

class crop:
    def main():
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_capture = cv2.VideoCapture(0)
        img_counter = 0

        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)

            # for (x, y, w, h) in faces:
            #     t = cv2.rectangle(frame, (x+92, y-20), (x+w, y+h), (0, 200, 0), 2)
            y=0
            x=0
            h=50
            w=120
            for (x, y, w, h) in faces:
                t = cv2.rectangle(frame, (x+100, y+40), (x+20, y+10), (0, 250, 0), 2)

            crop_image = frame[y+13:y+40, x+20:x+100]

            cv2.imshow('Video', frame)

            k = cv2.waitKey(1)
            if k & 0xFF == ord('q'):
                break
            elif k%256 == 27:
                break
            elif k%256 == 32:
                img_name = "opencv{}.png".format(img_counter)
                cv2.imwrite(img_name, crop_image)
                print("{} written!".format(img_name))
                img_counter += 1

                fixed_height = 480
                image = Image.open('opencv0.png')
                height_percent = (fixed_height / float(image.size[1]))
                width_size = 640
                image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
                image.save('opencv0.png')

                image = cv2.imread('opencv0.png')
                sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                sharpen = cv2.filter2D(image, -1, sharpen_kernel)

                cv2.imshow('sharpen', sharpen)

        # cv2.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    crop.main()
