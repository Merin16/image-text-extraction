import keras_ocr
import os
import cv2
import numpy as np
from glob import glob
# "test"
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
    # Read the original image
    image = cv2.imread(img_fn)

    # Initialize the rotation angle to None
    rotation_angle = None

    # Try rotating the image at different angles
    for rotated_angle in range(0, 361):
        # Rotate the image
        rotated_image = rotate_image(image, rotated_angle)

        # Perform OCR on the rotated image
        rotated_results = pipeline.recognize([rotated_image])
        rotated_result = rotated_results[0]

        # Extract recognized text from OCR results
        recognized_text = ""
        for detection in rotated_result:
            text = detection[0]
            recognized_text += text + " "

        # Check if the word "psi" is successfully extracted
        if "psi" in recognized_text:
            rotation_angle = rotated_angle
            break

    if rotation_angle is not None:
        # Save the rotated image
        rotated_image = rotate_image(image, rotation_angle)
        output_path = os.path.join(output_folder, os.path.basename(img_fn))
        cv2.imwrite(output_path, rotated_image)
        print(f"Rotated image saved to: {output_path}")
        print(f"The rotation angle needed to extract the word 'psi' is {rotation_angle} degrees")
    else:
        print("The word 'psi' was not successfully extracted in rotated images.")

        # print
