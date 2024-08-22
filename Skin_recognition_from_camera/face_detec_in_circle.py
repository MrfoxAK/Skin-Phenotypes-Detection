import cv2,sys
from matplotlib import image
from pyparsing import col, restOfLine

def detect_face(image):
     # detect face from an image and returns faces
     image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     face_d = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
     faces = face_d.detectMultiScale(image,scaleFactor=1.3,minNeighbors=5)
     return faces

def check_inside(point,center,radius):
     equation = (point[0]-center[0])**2 + (point[1]-center[1]**2) - radius**2
     if equation>0:
          return False

     return True

if __name__ == "__main__":
          
     # reading an iamge
     img = cv2.imread("face_ak.png", cv2.IMREAD_UNCHANGED)

     #convert BGR to BGRA,A-alpha channel
     img_transparent = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)

     # make the whole image transfarent
     for rows in range(img.shape[0]):
          for cols in range(img.shape[1]):
               img_transparent[rows][cols][3] = 0
          
     cv2.imwrite("output.png",img_transparent)

     faces = detect_face(img)
     if len(faces)==0:
          print("You got no faces in the iamge,please recheck")
     print(faces)
     # get a face
     face = faces[0]

     # crop a circle

     tlx = face[0]
     tly = face[1]
     w = face[2]
     h = face[3]

     center = [tlx + int(w/2), tly + int(h/2)]
     radius = max(int(w/2), int(h/2))

     for rows in range(img_transparent.shape[0]):
          for cols in range(img_transparent.shape[1]):
               if check_inside([cols,rows],center,radius):
                    img_transparent[rows][cols][3] = 255

     cv2.imwrite("output_cropped.png",img_transparent)


