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

    # Apply normal blur
    blur = cv2.blur(image, (15, 15))  # Kernel size (15, 15)
    resized_blur = resize_image(blur)
    print("Blurred Image Shape:", blur.shape)

    # Display the blurred image
    cv2.imshow("Blurred Image", resized_blur)

    # Apply Gaussian blur
    gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)  # Kernel size (15, 15) and sigmaX=0
    resized_gaussian_blur = resize_image(gaussian_blur)
    print("Gaussian Blurred Image Shape:", gaussian_blur.shape)

    # Display the Gaussian blurred image
    cv2.imshow("Gaussian Blurred Image", resized_gaussian_blur)

    # Save the processed images for verification
    cv2.imwrite("blur_output.jpg", blur)
    cv2.imwrite("gaussian_blur_output.jpg", gaussian_blur)

    # Wait for a key press indefinitely and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
