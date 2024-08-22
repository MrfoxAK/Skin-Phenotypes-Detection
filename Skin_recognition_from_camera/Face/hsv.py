import cv2
import numpy as np

count =0
def cal(count):
    print()
    if(count==0):
        print("Non-Skin")
    else:
        print("Skin")



def detect():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    while(True):
        ret, frame = cap.read()
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('y'):
            cv2.imwrite('C:\\Users\\AKASH\\OneDrive\\Desktop\\Skin_recognition_deb\\Face\\test.jpg',frame)
            break

    cap.release()
    cv2.destroyAllWindows()

    image=cv2.imread("test.jpg")
    im=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    h,w = image.shape[0], image.shape[1]

    avg_v=im[::1].mean()
# max_s=im[::1].min()

    with open("C:\\Users\\AKASH\\OneDrive\\Desktop\\Skin_recognition_deb\\Face\\skin.txt") as f1:
        l1 = []
        for i in f1:
            l1.append(float(i.strip('\n')))

    with open("C:\\Users\\AKASH\\OneDrive\\Desktop\\Skin_recognition_deb\\Face\\skin.txt") as f2:
        l2 = []
        for i in f2:
            l2.append(float(i.strip('\n')))
        
    dif=l2[0]-l1[0]
    sig_lev=l1[0]+(dif/2)

    if (avg_v<=sig_lev):
        count=1 
        cal(count)       #   SKIN

    else:
        count=0 
        cal(count)      #   NON-SKIN

detect()

# if (x==0):

#     print("skin")           #   SKIN

# else:

#     print("non-skin")          #   NON-SKIN