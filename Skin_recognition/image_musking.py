import numpy as np
import cv2


# low_green = np.array([25,52,72])
# high_green = np.array([102,255,255])
low_orange = np.array([5,50,50])
high_orange = np.array([15,255,255])


cap = cv2.VideoCapture(0)


while True:
     ret, frame = cap.read()
     cv2.imshow('o_f',frame)

     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


     mask = cv2.inRange(hsv,low_orange,high_orange)
     cv2.imshow("mask",mask)

     if cv2.waitKey(1) == ord('q'):
          break
cap.relase()
cap.destroyAllWindows()









