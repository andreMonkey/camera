#!/usr/bin/python

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(1)
camera.capture('/agile-node-red-nodes/camera/pictures/image.jpg')
camera.stop_preview()
