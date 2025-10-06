# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

import cv2

print(cv2.version.opencv_version)

image: cv2.UMat = cv2.imread("./tutorials/data/images/logo.png", cv2.IMREAD_COLOR)

if image is None:
    raise FileNotFoundError
image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_CUBIC)
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("output.jpg", image)
cv2.namedWindow("My Image", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Image", image)
cv2.waitKey(0)