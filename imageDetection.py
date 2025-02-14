import cv2
import numpy as np

def detect_edges(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Error: Unable to read the image.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Display the original image and edges
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detection", edges)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    print("Edge Detection Program")
    # Sample image path (update the path as per your environment)
    image_path = "sample_image.jpg"
    print(f"Using sample image path: {image_path}")
    detect_edges(image_path)

if __name__ == "__main__":
    main()