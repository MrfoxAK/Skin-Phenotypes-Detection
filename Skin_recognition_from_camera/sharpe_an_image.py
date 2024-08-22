from PIL import Image
from PIL import ImageFilter

# Open an already existing image
imageObject = Image.open("C:/Users/AKASH/OneDrive/Desktop/Skin_recognition_deb/opencv0.png");
imageObject.show();

# Apply sharp filter
sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);

# Show the sharpened images
sharpened1.show();
sharpened2.show();