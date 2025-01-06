import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to resize images to fit the screen
def resize_image(image, max_width=800, max_height=600):
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height)
    new_width = int(width * scale)
    new_height = int(height * scale)
    return cv2.resize(image, (new_width, new_height))

# Load the image
image2 = cv2.imread("images/tiger.jpg")  # Update the path to your image

# Check if the image is loaded successfully
if image2 is None:
    print("Error: Image not found. Please check the file path.")
else:
    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(image2, (5, 5), 1.4)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred_image, 50, 150)

    # Resize both the original and edge-detected images for display
    resized_image2 = resize_image(image2)
    resized_edges = resize_image(edges)

    # Display the original and edge-detected images using Matplotlib
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(resized_image2, cv2.COLOR_BGR2RGB))  # Convert to RGB for proper color display

    # Canny Edge Detection Image
    plt.subplot(1, 2, 2)
    plt.title('Canny Edge Detection')
    plt.imshow(resized_edges, cmap='gray')

    # Show the images
    plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to resize images to fit the screen
def resize_image(image, max_width=800, max_height=600):
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height)
    new_width = int(width * scale)
    new_height = int(height * scale)
    return cv2.resize(image, (new_width, new_height))

# Load the image
image2 = cv2.imread("path_to_your_image.jpg")  # Update the path to your image

# Check if the image is loaded successfully
if image2 is None:
    print("Error: Image not found. Please check the file path.")
else:
    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(image2, (5, 5), 1.4)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred_image, 50, 150)

    # Resize both the original and edge-detected images for display
    resized_image2 = resize_image(image2)
    resized_edges = resize_image(edges)

    # Display the original and edge-detected images using Matplotlib
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(resized_image2, cv2.COLOR_BGR2RGB))  # Convert to RGB for proper color display

    # Canny Edge Detection Image
    plt.subplot(1, 2, 2)
    plt.title('Canny Edge Detection')
    plt.imshow(resized_edges, cmap='gray')

    # Show the images
    plt.show()
