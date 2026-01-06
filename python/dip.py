'''
1. Read the image at the saved image path
2. Display that image
3. Prints its different attributes of the image
4. print the type of image saved and changed its type to another type.
'''

# cv2 opencv module for digital image processing
import cv2
import os
from google.colab.patches import cv2_imshow

# Image path - i.e image path where the image is saved!
img_path = "/content/img.jpg"

# Read image
img = cv2.imread(img_path)

# Check if image loaded properly
if img is None:
    print("Image is not visible properly!")
else:
    # Display image
    cv2_imshow(img)

    # Print image attributes
    print("Image size:", img.size)
    print("Image dimensions (ndim):", img.ndim)
    print("Image shape:", img.shape)
    print("Image data type:", img.dtype)
    print(type(img))


# Get the original image type
file_name, file_extension = os.path.splitext(img_path)
print(f"Original image type: {file_extension}")

# Convert and save the image as PNG
output_png_path = "/content/img.png"
cv2.imwrite(output_png_path, img)
print(f"Image successfully converted and saved as PNG at: {output_png_path}")

# Converting to jpeg type

output_jpeg_path = "/content/img.jpeg"
cv2.imwrite(output_jpeg_path, img)
print(f"Image successfully converted and saved as JPEG at: {output_jpeg_path}")


# This shows the difference between lossy and lossless compression of the image using different formats
# Another way to optain the format of the image
from PIL import Image
img = Image.open(img_path)
format = img.format

import matplotlib.pyplot as plt
plt.imshow(img)

if format in ["JPG","JPEG"]:
  compression = "Lossy Compression"

elif format in ["PNG","TIFF","BMP"]:
  compression = "LossLess compression"

else:
  compression = "Unkownn compression"

print(f"Format of the image: {format}")
print(f"compression of the image: {compression}")
