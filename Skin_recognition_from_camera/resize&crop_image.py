# import cv2

# img = cv2.imread("face_ak.png")
# print(img.shape)

# width,height=400,400
# imgResize = cv2.resize(img,(width,height))
# print(imgResize.shape)

# imgCropped = img[0:900,300:540]

# cv2.imshow("ak",img)
# cv2.imshow("resized_ak",imgResize)
# cv2.imshow("cropped_ak",imgCropped)

# cv2.waitKey(0)


import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

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

cam.release()

cv2.destroyAllWindows()