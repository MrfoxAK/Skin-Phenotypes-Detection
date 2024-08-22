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

     if cv2.waitKey(1) == ord('q'):
          break

cv2.release()
cv2.destroyAllWindows()