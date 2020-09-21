
# GStreamer Settings

A collection of gstreamer settings for my reference

---

## IMX219-160 8-Megapixel Camera (from Waveshare)

gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=3264,height=2464,framerate=21/1' ! nvvidconv flip-method=0 ! video/x-raw,width=1920,height=1200 ! ximagesink

## Logitech C270
gst-launch-1.0 v4l2src device=/dev/video1 ! 'video/x-raw,format=YUY2,width=1280,height=960,pixel-aspect-ratio=1/1,framerate=15/2' ! videoconvert ! ximagesink

## HLSSINK (wip)
gst-launch-1.0 videotestsrc ! videoconvert ! x264enc tune=zerolatency ! mpegtsmux ! hlssink playlist-root=192.168.86.22:8080
