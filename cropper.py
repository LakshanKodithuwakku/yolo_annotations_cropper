import cv2
import numpy as np
import os

# Function to display an image using OpenCV
def show_image(image, title='Image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Get the directory path of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the paths for the input and output directories
input_dir = os.path.join(current_dir, 'input_dir')
output_dir = os.path.join(current_dir, "cropped_dir")

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        # Load the image
        image_file = os.path.join(input_dir, filename)
        image = cv2.imread(image_file)

        # Load the corresponding annotation file
        annotation_file = os.path.join(input_dir, os.path.splitext(filename)[0] + '.txt')
        annotations = np.loadtxt(annotation_file, delimiter=" ")

        # Convert the YOLO annotations to pixel coordinates
        image_height, image_width, _ = image.shape
        x_center = annotations[1]
        y_center = annotations[2]
        width = annotations[3]
        height = annotations[4]
        x_min = int((x_center - width / 2) * image_width)
        y_min = int((y_center - height / 2) * image_height)
        x_max = int((x_center + width / 2) * image_width)
        y_max = int((y_center + height / 2) * image_height)

        # Crop the image
        cropped_image = image[y_min:y_max, x_min:x_max]

        # Save the cropped image
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '_cropped.jpg')
        cv2.imwrite(output_file, cropped_image)

