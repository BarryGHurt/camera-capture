import cv2
import time

max_images = 3
interval_minutes = 1
filename_format = "timelapse_{}.png"
camera_index = 1


def main():
    video = cv2.VideoCapture(camera_index)
    index = 0

    while True:
        if video.grab():
            flag, frame = video.retrieve()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            index = index + 1
            filename = str.format(filename_format, index)
            print(filename)
            cv2.imwrite(filename, image)

        time.sleep(interval_minutes * 60)

        if index >= max_images:
            break

    video.release()


main()



