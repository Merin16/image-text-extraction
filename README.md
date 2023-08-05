# image-text-extraction

This project aims to extract the word "psi" or "WIKAI" from images and determine the rotation angle required to make the text straight as "psi". The image is then rotated by that angle to make the text appear perfectly straight.

The sample result is shown here:
-------------------------------
Recognized text for 'D:\github\image-text-extraction\images\image_1.png': tin st
Recognized text for 'D:\github\image-text-extraction\rotated_images\image_1.png' : psi cila
The rotation angle needed to extract word psi is 151 degree


**Run the following command on terminal/command prompt inside the root folder where the files reside:
---------------------------------------------------------------------------------------------------
```bash
python main.py
---------------------------------------------------------------------------------------------------

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Installation

1. Clone this repository to your local machine using `git clone`.
2. Navigate to the project directory: `cd image-text-extraction`.
3. Install the required dependencies using `pip install -r requirements.txt`.

## Usage

1. Place the images from which you want to extract the text in the `images` folder.
2. Run the main script `main.py` to extract the text and determine the rotation angle.
3. The rotated images will be saved in the `rotated_images` folder.

## Troubleshooting

If you encounter any issues while running the program, please follow these steps:

Make sure you have installed all the required dependencies mentioned in requirements.txt.
Check that the image file paths are correct and located in the images folder.





