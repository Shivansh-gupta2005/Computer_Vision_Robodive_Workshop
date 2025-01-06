import cv2
import numpy as np

# Function to resize images to fit the screen
def resize_image(image, max_width=800, max_height=600):
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height)
    new_width = int(width * scale)
    new_height = int(height * scale)
    return cv2.resize(image, (new_width, new_height))

# Load the image
image = cv2.imread("images/color.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found. Please check the file path.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    canny_image = cv2.Canny(gray, 150, 200)

    # Erosion and Dilation
    kernel = np.ones((5, 5), np.uint8)

    # Dilation
    dilate_image = cv2.dilate(canny_image, kernel, iterations=1)

    # Erosion
    erode_image = cv2.erode(canny_image, kernel, iterations=1)

    # Resize all images for display
    resized_canny_image = resize_image(canny_image)
    resized_dilate_image = resize_image(dilate_image)
    resized_erode_image = resize_image(erode_image)

    # Combine all images horizontally
    display = np.hstack((resized_canny_image, resized_dilate_image, resized_erode_image))

    # Display the combined image using OpenCV
    cv2.imshow("Canny, Dilated, and Eroded Images", display)

    # Wait for a key press indefinitely and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
