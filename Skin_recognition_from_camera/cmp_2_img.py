from skimage.metrics import strcuctural_similarity
import cv2


def orb_sim(img1,img2):
     orb = cv2.ORB_create()

     k_a,des_a = orb.detectAndCompute(img1,None)
     k_b,des_b = orb.detectAndCompute(img2,None)


     bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

     matches = bf.match(des_a,des_b)

     similar_reg = [i for i in matches if i.distance < 50]
     if len(matches)==0:
          return 0
     return len(similar_reg)/len(matches)

def strctural_sim(img1,img2):

     sim,diff = strcuctural_similarity(img1,img2,full = True)
     return sim

img01 = cv2.imread('C:/Users/AKASH/OneDrive/Desktop/Skin_recognition_deb/opencv1.png',0)
img02 = cv2.imread('C:/Users/AKASH/OneDrive/Desktop/Skin_recognition_deb/opencv2.png',0)

orb_similarity = orb_sim(img01,img02)

print("Similarity using ORB is : ",orb_similarity)

ssim = strctural_sim(img01,img02)

print("Similarity using SSIM is : ",ssim)






















