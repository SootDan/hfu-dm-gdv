# Exercise #3
# -----------
#
# Show camera video and mirror it.

import numpy as np
import cv2

cap: cv2.VideoCapture = cv2.VideoCapture(0)

width: float = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height: float = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
codec: float = cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT)
print(f"Width: {width}\nHeight: {height}\nCodec: {codec}")

cv2.namedWindow("Video image", cv2.WINDOW_GUI_NORMAL)
#cv2.imshow("Image", cap)
#cv2.waitKey(0)
# TODO Start a loop to continuously read frames from the camera using 'while True:'.
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
# TODO (In loop, if successful) (Skip this step for now and implement the display first in order 
# to see the camera image.)
# Create four flipped tiles of the image by first creating an empty image 
# with 'np.zeros'. Then resize the frame to half size using 'cv2.resize' with fx=0.5 and fy=0.5.
# Finally, fill in the four quadrants of the empty image with the original and flipped images
# using 'cv2.flip' with the appropriate flip codes (check the documentation).

# TODO (In loop, if successful) Display the image.

# TODO (In loop) Check if 'q' is pressed by comparing the return value of 'waitKey' with the 'ord'
# of the letter "q". Use simply 'break' to exit the loop.

# TODO Release the video capture object with 'release' and close the window with 'destroyAllWindows'.
