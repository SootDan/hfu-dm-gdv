# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of 
# the image to some other place, count the used colors in the image

import cv2
import numpy as np

def make_window(image: cv2.UMat, destroy_windows: bool = False):
    """
    Creates a window. Waits for user input before closing.
    """
    cv2.namedWindow("My Image", cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    if destroy_windows:
        cv2.destroyAllWindows()


file_path: str = "./tutorials/data/images/logo.png"
img_color: cv2.UMat = cv2.imread(file_path, cv2.IMREAD_COLOR)
img_gray: cv2.UMat = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

if img_color is None or img_gray is None:
    raise FileNotFoundError

## Image data access
print(type(img_gray))
print(img_gray.dtype)
print(img_gray.shape)

img: cv2.UMat = img_gray.copy()
width: int = img.shape[0]
height: int = img.shape[1]

## This is how you can access the height and width of an image stored as a numpy ndarray. 
## In all following exercises you should use this way to access the height and width of an image.
## Then, you can use the variables 'height' and 'width' in your code instead of hardcoding values. 
## This makes your code flexible and independent from the actual image size.
width = 7
height = 5
img = cv2.resize(img, (width, height))
print(img[0])
print(img[:, 0])

img = img_color.copy()

for x in range(width):
    for y in range(height):
        img[x][y] = [0, 0, 0]
make_window(img)

rgb = img.reshape(-1, img.shape[-1])
unique = np.unique(rgb, axis=0, return_counts=False)
print(unique)

part = img[3:3+width, 3:3+height]
img[30:30+width, 30:30+height] = part
make_window(img)

cv2.imwrite("image.jpg", img)

file_path = "./image.jpg"
img_edited: cv2.UMat = cv2.imread(file_path, cv2.IMREAD_COLOR)
make_window(img_edited)
make_window(img_color, destroy_windows=True)