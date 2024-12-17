#Sobel edge detection
import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread("cross.png", 0)

# Check if the image loaded successfully
if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Create an empty output image for storing results
imgNew = np.zeros_like(img, dtype=np.float64)  # Use float64 for intermediate calculations

# Define Sobel kernels
sobelX = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
sobelY = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

# Convert kernels to NumPy arrays
sobelX = np.array(sobelX)
sobelY = np.array(sobelY)

# Get image dimensions
h, w = img.shape[:2]

# Perform convolution
for i in range(1, h - 1):
    for j in range(1, w - 1):
        Gx = 0
        Gy = 0
        # Convolution with Sobel kernels
        for m in range(3):
            for n in range(3):
                Gx += sobelX[m][n] * int(img[i - 1 + m][j - 1 + n])  # Convert to int
                Gy += sobelY[m][n] * int(img[i - 1 + m][j - 1 + n])  # Convert to int
        # Compute the gradient magnitude
        imgNew[i, j] = (Gx**2 + Gy**2)**0.5

# Normalize the output image to 0-255
imgNew = np.clip(imgNew, 0, 255).astype(np.uint8)

# Display the original and processed images side by side
show = np.hstack((img, imgNew))
cv2.imshow("Sobel Edge Detection", show)
cv2.waitKey(0)
cv2.destroyAllWindows()
