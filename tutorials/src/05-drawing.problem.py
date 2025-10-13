# Exercise #5
# -----------
#
# Create a white image and draw something on it.

import cv2
import numpy as np

width: int = 625
height: int = 512
image: cv2.UMat = np.ones((height, width, 3), np.uint8) * 255       # 3 stands for the RGB channels

## Drawing helper variables
# Thickness
thick: int = 10
thin: int = 3

# Colors in RGB
blue: tuple = (255, 0, 0)
red: tuple = (0, 0, 255)
darkgreen: tuple = (20, 200, 20)
black: tuple = (0, 0, 0)

# Fonts
font_size_large: int = 3
font_size_small: int = 1
font: int = cv2.FONT_HERSHEY_SIMPLEX


image = cv2.line(image, (0, 0), (width, height), darkgreen, thin)
image = cv2.line(image, (0, height), (width, 0), darkgreen, thin)

image = cv2.circle(image, (width // 2, height // 2), thick * thin, red, thick)

lorem_ipsum: str = "Lorem ipsum dolor sit amet."
image = cv2.putText(image, lorem_ipsum, (0, height - 10), font, font_size_small, black, thin)

image = cv2.arrowedLine(image, (30, 30), (30, 90), blue, thin)
image = cv2.arrowedLine(image, (30, 30), (90, 30), blue, thin)

image = cv2.putText(image, "X-Axis", (30, 25), font, font_size_small, blue, thin)
image = cv2.putText(image, "Y-Axis", (30, 120), font, font_size_small, blue, thin)

cv2.imshow("Drawing Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

