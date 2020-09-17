import cv2

webcamset = '/dev/video1'

# TODO: fix this one
webcamset2 = 'v4l2src device=/dev/video1 ! video/x-raw, width=800, height=600, framerate=24/1 ! videoconvert ! appsink'

picamset = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=0 ! video/x-raw, width=1920, height=1200, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'


camera = cv2.VideoCapture(picamset)

while True:
    flag, frame = camera.read()
    cv2.imshow('thecam', frame)
    cv2.moveWindow('thecam',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()