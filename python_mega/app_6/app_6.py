import cv2
import time

video = cv2.VideoCapture(0)

a = 0
while True:
    a = a + 1
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)
    cv2.waitKey(1000)

    if key == ord('q'):
        break

print(f"Ran for {a} seconds!")

video.release()

cv2.destroyAllWindows()
