# Exercise #4
# -----------
#
# Loading a video file and mirror it.

import numpy as np
import cv2

cap: cv2.VideoCapture = cv2.VideoCapture("tutorials/data/videos/hello_UH.m4v")

width: float = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height: float = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
codec: float = cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT)
print(f"Width: {width}\nHeight: {height}\nCodec: {codec}")

cv2.namedWindow("Video image", cv2.WINDOW_GUI_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    key = cv2.waitKey(20)

    img = np.zeros_like(frame)
    tile = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    img[:tile.shape[0], :tile.shape[1]] = tile
    img[tile.shape[0]:, :tile.shape[1]] = cv2.flip(tile, 0)
    img[:tile.shape[0], tile.shape[1]:] = cv2.flip(tile, 1)
    img[tile.shape[0]:, tile.shape[1]:] = cv2.flip(tile, -1)
    cv2.imshow("Video image", img)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()