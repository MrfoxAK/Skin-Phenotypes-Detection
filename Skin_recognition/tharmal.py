# import cv2
# import numpy as np


# # initialize the video stream
#         print("[INFO] starting video stream...")
#         vs = VideoStream(src=1)  # call inside WebcamVideoStream class: self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        
#         print("CAP_PROP_FRAME_WIDTH")
#         vs.stream.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#         print("CAP_PROP_FRAME_HEIGHT")
#         vs.stream.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#         print("CAP_PROP_FPS")
#         vs.stream.stream.set(cv2.CAP_PROP_FPS, 25)

#         vs.start()

#         # loop over the frames from the video stream
#         while True:
#             # grab the frame from the threaded video stream
#             frame = vs.read()

#         ...
#        # not relevant frame processing snipped

#             cv2.imshow("webcam_tf", frame)
#             if cv2.waitKey(20) == 27:
#                 break






# import sys
# import os
# import time
# import colorsys
# import numpy as np
# import cv2
# import datetime

# from PIL import Image

# sys.path.insert(0, "./build/lib.linux-armv7l-3.5")

# import MLX90640 as mlx

# img = Image.new( 'L', (24,32), "black")

# def irCounter():   


#     mlx.setup(8) #set frame rate of MLX90640

#     f = mlx.get_frame()

#     mlx.cleanup()

#     # get max and min temps from sensor
#     v_min = min(f)
#     v_max = max(f)

#     # Console output for testing
#     textTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # get timestamp
#     print(textTime)
#     print(min(f))
#     print(max(f))
#     print("")

#     for x in range(24):
#         row = []
#         for y in range(32):
#             val = f[32 * (23-x) + y]
#             row.append(val)
#             img.putpixel((x, y), (int(val)))

#     # convert raw temp data to numpy array
#     imgIR = np.array(img)

#     ## Threshold the -40C to 300 C temps to a more human range
#     # Sensor seems to read a bit cold, calibrate in final setting
#     rangeMin = 6 # low threshold temp in C
#     rangeMax = 20 # high threshold temp in C


#     # Apply thresholds based on min and max ranges
#     depth_scale_factor = 255.0 / (rangeMax-rangeMin)
#     depth_scale_beta_factor = -rangeMin*255.0/(rangeMax-rangeMin)

#     depth_uint8 = imgIR*depth_scale_factor+depth_scale_beta_factor
#     depth_uint8[depth_uint8>255] = 255
#     depth_uint8[depth_uint8<0] = 0
#     depth_uint8 = depth_uint8.astype('uint8')

#     # increase the 24x32 px image to 240x320px for ease of seeing
#     bigIR = cv2.resize(depth_uint8, dsize=(240,320), interpolation=cv2.INTER_CUBIC)

#     # Normalize the image
#     normIR = cv2.normalize(bigIR, bigIR, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

#     # Apply a color heat map
#     colorIR = cv2.applyColorMap(normIR, cv2.COLORMAP_JET)

#     # Use a bilateral filter to blur while hopefully retaining edges
#     brightBlurIR = cv2.bilateralFilter(normIR,9,150,150)

#     # Threshold the image to black and white 
#     retval, threshIR = cv2.threshold(brightBlurIR, 210, 255, cv2.THRESH_BINARY)

#     # Define kernal for erosion and dilation and closing operations
#     kernel = np.ones((5,5),np.uint8)

#     erosionIR = cv2.erode(threshIR,kernel,iterations = 1)

#     dilationIR = cv2.dilate(erosionIR,kernel,iterations = 1)

#     closingIR = cv2.morphologyEx(dilationIR, cv2.MORPH_CLOSE, kernel)

#     # Detect edges with Canny detection, currently only for visual testing not counting
#     edgesIR = cv2.Canny(closingIR,50,70, L2gradient=True)

#     # Detect countours
#     contours, hierarchy = cv2.findContours(closingIR, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#     # Get the number of contours ( contours count ...






