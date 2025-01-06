import cv2

# Function to resize images to fit the screen
def resize_image(image, max_width=800, max_height=600):
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height)
    new_width = int(width * scale)
    new_height = int(height * scale)
    return cv2.resize(image, (new_width, new_height))

# Load the image
image2 = cv2.imread("images/tiger.jpeg")

# Check if the image is loaded successfully
if image2 is None:
    print("Error: Image not found. Please check the file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # Apply normal blur
    image_blur = cv2.blur(image2, (5, 5))
    
    # Apply Canny edge detection
    canny_image = cv2.Canny(image_blur, 23, 50)

    # Resize all images for display
    resized_image2 = resize_image(image2)
    resized_canny_image = resize_image(canny_image)
    resized_image_blur = resize_image(image_blur)

    # Display the resized images using cv2.imshow()
    cv2.imshow("Original Image (Resized)", resized_image2)
    cv2.imshow("Canny Edge Detected Image (Resized)", resized_canny_image)
    cv2.imshow("Blurred Image (Resized)", resized_image_blur)

    # Wait for a key press indefinitely and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the resized images for further use
    cv2.imwrite("resized_original_image.jpg", resized_image2)
    cv2.imwrite("resized_canny_image.jpg", resized_canny_image)
    cv2.imwrite("resized_blurred_image.jpg", resized_image_blur)
