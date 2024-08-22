from PIL import Image, ImageChops

img1 = Image.open("C:\\Users\\AKASH\\OneDrive\\Desktop\\Skin_recognition_deb\\opencv1.png")
img2 = Image.open("C:\\Users\\AKASH\\OneDrive\\Desktop\\Skin_recognition_deb\\opencv2.png")



dif = ImageChops.difference(img1,img2)
print(dif)

dif.show()















