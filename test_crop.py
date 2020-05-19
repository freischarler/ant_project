import os
import sys
from picamera import PiCamera
import time
from time import sleep



#sudo apt-get install gpac
sensorWidth=640
sensorHeight=480
tiempo_grabado=5
x=y=0.5
w=h=1.0
#x=0.0
#y=0.65
#w=0.1
#h=0.1


try:
    camera=PiCamera()
    regionOfInterest = (x,y,w,h)
    (roiX, roiY, roiW, roiH) = regionOfInterest
    
    width  = sensorWidth*roiW                     #Desired width
    height = sensorHeight*roiH                    #Desired height
    
    percentAspectRatio = roiW/roiH                #Ratio in percent of size 
    imageAspectRatio   = width/height             #Desired aspect ratio
    sensorAspectRatio  = sensorWidth/sensorHeight #Physical sensor aspect ratio       

    #The sensor is automatically cropped to fit current aspect ratio 
    #so we need to adjust zoom to take that into account
    if (imageAspectRatio > sensorAspectRatio):    
        roiY = (roiY - 0.5) * percentAspectRatio + 0.5  
        roiH = roiW                              
        
    if (imageAspectRatio < sensorAspectRatio):   
        roiX = (roiX - 0.5) * percentAspectRatio + 0.5  
        roiW = roiH 

    camera.resolution=(int(width),int(height))
    camera.zoom=(roiX,roiY,roiW,roiH)
    camera.start_preview()
    
    camera.start_recording("pythonVideo.h264")
    time.sleep(tiempo_grabado)
   	
except KeyboardInterrupt:
    print("interrumpiendo")
    camera.stop_preview()
    camera.close()




