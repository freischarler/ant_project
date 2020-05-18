import os
import sys
from picamera import PiCamera
import time
from time import sleep

resize=2

#sudo apt-get install gpac

try:
    camera=PiCamera()
    camera.resolution = (640,480)
    camera.start_preview(fullscreen=False,window=(100,20,int(640/resize),int(480/resize)))
    time.sleep(5)
   	
except KeyboardInterrupt:
    print("interrumpiendo")
    camera.stop_preview()
    camera.close()
