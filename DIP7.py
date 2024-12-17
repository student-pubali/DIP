#Diagonal edges +45,-45
import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread("cross.png", 0)

# Check if the image loaded successfully
if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Create a copy of the image for output
imgNew = img.copy()

# Define the kernels for +45 and -45 edge detection
plus45 = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]
neg45 = [[-1, -1, 2], [-1, 2, -1], [2, -1, -1]]

# Convert kernels to NumPy arrays for easier manipulation
plus45 = np.array(plus45)
neg45 = np.array(neg45)

# Get image dimensions
h, w = img.shape[:2]

# Process the image
for i in range(1, h - 1):
    for j in range(1, w - 1):
        Gx = 0
        Gy = 0
        # Perform convolution manually
        for m in range(3):
            for n in range(3):
                Gx += (plus45[m][n] * int(img[i - 1 + m][j - 1 + n]))  # Cast to int
                Gy += (neg45[m][n] * int(img[i - 1 + m][j - 1 + n]))  # Cast to int
        # Compute the gradient magnitude and clip the result to 0-255
        imgNew[i, j] = min(255, max(0, int((Gx**2 + Gy**2)**0.5)))

# Display the original and processed images side by side
show = np.hstack((img, imgNew))
cv2.imshow("Edge Detection (+45 and -45)", show)
cv2.waitKey(0)
cv2.destroyAllWindows()
