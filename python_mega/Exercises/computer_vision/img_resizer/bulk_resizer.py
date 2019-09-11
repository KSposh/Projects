import cv2
import os

def resizer(image, x, y, color=1):
    img = cv2.imread(image, color)
    return cv2.resize(img, (x, y))

for image in os.listdir('imgs'):
    if image.endswith('jpg'):
        resized_i = resizer(f"imgs/{image}", 100, 100)
        cv2.imwrite(f"resized/resized_{image}", resized_i)
