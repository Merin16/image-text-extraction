import keras_ocr
import os
import cv2
import numpy as np
from glob import glob
from tqdm import tqdm

# Function to rotate the image
def rotate_image(image, angle):
    center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

img_fns = glob(r'D:\github\image-text-extraction\images\*')
pipeline = keras_ocr.pipeline.Pipeline()

# Create a folder to save the rotated images
output_folder = r'D:\github\image-text-extraction\rotated_images'
os.makedirs(output_folder, exist_ok=True)

for img_fn in img_fns:
    results = pipeline.recognize([img_fn])
    result = results[0]

    # Extract recognized text from OCR results
    recognized_text = ""
    for detection in result:
        text = detection[0]
        recognized_text += text + " "

    # Print the complete recognized text for the current image
    print(f"Recognized text for '{img_fn}': {recognized_text}")

    # Read the image
    image = cv2.imread(img_fn)
    rotated_angle=151
    # Rotate the image 30 degrees
    rotated_image = rotate_image(image, rotated_angle)

    # Save the rotated image
    output_path = os.path.join(output_folder, os.path.basename(img_fn))
    cv2.imwrite(output_path, rotated_image)

img_fns = glob(r'D:\github\image-text-extraction\rotated_images\*')
pipeline = keras_ocr.pipeline.Pipeline()


for img_fn in img_fns:
    results = pipeline.recognize([img_fn])
    result = results[0]

    # Extract recognized text from OCR results
    recognized_text = ""
    for detection in result:
        text = detection[0]
        recognized_text += text + " "

    # Print the complete recognized text for the current image
    print(f"Recognized text for '{img_fn}' : {recognized_text}")
    print("The rotation angle needed to extract word",recognized_text.split(" ")[0],"is",rotated_angle,"degree")