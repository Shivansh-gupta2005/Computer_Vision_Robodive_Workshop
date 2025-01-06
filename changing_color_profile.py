import cv2

# Load the image
image = cv2.imread("images/color.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found. Please check the file path.")
else:
    # Print the original shape of the image
    print("Original Image Shape:", image.shape)

    # Function to resize images to fit the screen
    def resize_image(image, max_width=800, max_height=600):
        height, width = image.shape[:2]
        scale = min(max_width / width, max_height / height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        return cv2.resize(image, (new_width, new_height))

    # Resize and display the original image
    resized_image = resize_image(image)
    cv2.imshow("Original Image", resized_image)

    # Convert the image to grayscale and resize it
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_gray = resize_image(gray)
    print("Grayscale Image Shape:", gray.shape)

    # Display the grayscale image
    cv2.imshow("Grayscale Image", resized_gray)

    # Convert the image to HSV and resize it
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    resized_hsv = resize_image(hsv)
    print("HSV Image Shape:", hsv.shape)

    # Display the HSV image
    cv2.imshow("HSV Image", resized_hsv)

    # Save the processed images for verification
    cv2.imwrite("resized_grayscale_output.jpg", resized_gray)
    cv2.imwrite("resized_hsv_output.jpg", resized_hsv)

    # Wait for a key press indefinitely and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
