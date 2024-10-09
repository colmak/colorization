# Colorize Image Project

This project demonstrates how to automatically colorize black and white images using a pre-trained deep learning model with OpenCV. The project utilizes a convolutional neural network (CNN) trained on color images to predict and add color to grayscale images.

![image](https://github.com/user-attachments/assets/516007d7-883d-4edd-8177-ff9dd2b6703e)
![image](https://github.com/user-attachments/assets/e9bcb67f-589d-4e0a-9cc1-e82ee9f56a60)


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model and Resources](#model-and-resources)
- [Acknowledgements](#acknowledgements)

## Features

- Convert black and white images to color images using a pre-trained deep learning model.
- Automatically predicts the color channels (`ab`) based on the grayscale (`L`) channel of the input image.
- Uses OpenCV's deep neural network (`cv2.dnn`) module to load and run the colorization model.

## Installation

1. **Install OpenCV and NumPy**:
   Make sure you have Python installed on your machine. Install the necessary libraries with the following command:

   ```bash
   pip install opencv-python numpy
   ```

2. **Download the model files**:
   Download the following files needed for the colorization process:

   - `colorization_deploy_v2.prototxt`: The architecture file for the neural network.
   - `colorization_release_v2.caffemodel`: The pre-trained weights for the model.
   - `pts_in_hull.npy`: A NumPy array containing cluster centers required for color prediction.

   You can find these files in various repositories or from OpenCV's official model zoo.

3. **Project Setup**:
   Place the downloaded model files in the project directory where your script resides.

## Usage

To use the colorization script:

1. Ensure that you have a grayscale (black and white) image in your working directory.
   
2. Call the `colorize_image()` function, passing the input black and white image and the desired output file path.

   ```python
   input_path = "bw_image.jpg"
   output_path = "color_image.jpg"
   colorize_image(input_path, output_path)
   ```

This will load the grayscale image, colorize it, and save the colorized image to the specified output path.

## Model and Resources

- **Prototxt File**: This file contains the structure of the CNN used for colorization.
- **Caffemodel File**: The weights of the pre-trained model used to perform the task of colorization.
- **Cluster Centers (`pts_in_hull.npy`)**: These are essential to predict the color values for each pixel in the grayscale image.

The model was trained on millions of color images to predict the missing color channels (`ab`) from the grayscale `L` channel.

## Acknowledgements

This project leverages the colorization model developed by Richard Zhang et al. The original paper is titled ["Colorful Image Colorization"](https://richzhang.github.io/colorization/), and the implementation is based on their work. Special thanks to OpenCV for providing the pre-trained models and deep learning tools used in this project.

--- 

This README provides an overview of the project, instructions for setting it up, and how to use it effectively. If you have any questions or need further assistance, feel free to reach out!
