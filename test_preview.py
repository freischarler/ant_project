import os
import sys
from picamera import PiCamera
import time
from time import sleep



#sudo apt-get install gpac

try:
    camera=PiCamera()
    camera.resolution = (640,480)

    	#camera.crop =(0.0,0.0,0.5,0.2) #crop

    camera.zoom =(0.0,0.0,0.5,0.2) #default(x, y, w, h)
    	#cant pix / 640 = 0.078
    	#cant pix / 480 = 0.104

    #camera.start_preview(fullscreen=False,window=(100,20,640,480))
    camera.start_preview(fullscreen=True)

    #camera.start_recording("pythonVideo.h264")
    #sleep(0)
    #camera.stop_recording()
    time.sleep(10)
   	
except KeyboardInterrupt:
    print("interrumpiendo")
    #print "interrumpiendo"
    camera.stop_preview()
    camera.close()
    #sys.exit()






