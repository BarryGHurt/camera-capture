import cv2
from timeit import default_timer as timer
import time

video = cv2.VideoCapture(0)

start = timer()
print(start)

a = 0

while True:
    now = timer()
    print(now)

    if video.grab():
        flag, frame = video.retrieve()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        a = a + 1
        filename = str.format("timelapse_{}.png", a)
        print(filename)
        cv2.imwrite(filename, gray)

    time.sleep(1 * 60)

    #cv2.imshow("capture", gray)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()
