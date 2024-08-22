from turtle import width
import cv2
import numpy as np

vd = cv2.VideoCapture(0)

while True:
     ret,frame = vd.read()
     width = int(vd.get(3))
     height = int(vd.get(4))

     # img = cv2.ellipse(frame,(320,250),100,0,30,360,(0,0,255),2)
     # center_coordinates = (120, 100)
     center_coordinates = (320, 250)

     axesLength = (100, 75)

     angle = 90

     startAngle = 0

     endAngle = 360

     # Blue color in BGR
     color = (255, 0, 0)

     # Line thickness of -1 px
     thickness = 5
     upper_left = (280,175)
     bottom_right = (360,205)  # Using cv2.ellipse() method
     # Draw a ellipse with blue line borders of thickness of -1 px
     img = cv2.ellipse(frame, center_coordinates, axesLength, angle,
                          startAngle, endAngle, color, thickness)
     img = cv2.rectangle(frame,upper_left,bottom_right,(255, 0, 0),1)

     cv2.imshow('frame', img)

     img_counter = 0

     k = cv2.waitKey(1)
     if k%256 == 27:
          # ESC pressed
          print("Escape hit, closing...")
          break
     elif k%256 == 32:
          # SPACE pressed
          img_name = "opencv_frame_{}.png".format(img_counter)
          cv2.imwrite(img_name, frame)
          print("{} written!".format(img_name))
          img_counter += 1

imgnormal=cv2.imread("opencv_frame_0.png")

imgCropped=imgnormal[175:205,280:360]
# print(imgCropped.shape)
imgResize = cv2.resize(imgCropped,(400,400))


cv2.imshow("frame_ss",imgCropped)
cv2.imshow("resized_ss",imgResize)
cv2.waitKey(0)

cv2.release()
cv2.destroyAllWindows()
