import os
import sys
from glob import glob

import subprocess
from subprocess import check_output, CalledProcessError

import picamera
from picamera import PiCamera
import time
import datetime as dt
from datetime import datetime, date

import time
from time import sleep

import RPi.GPIO as GPIO

ErrorPin=13
RecLed=15

class Video():
    crop_bool=0
    modo_fullscreen=1
    modo_offscreen=0
    modo_comprimir=0
    windows_x=0
    windows_y=0
    resize=1
    crop_x=0
    crop_y=0
    crop_w=1
    crop_h=1
    windows_posx=0
    windows_posy=0
    name="test"
    duracion_grabacion=0

    f_actual="1/1/00"
    h_actual="12:12"
    tiempo_defecto="yes"
    h_inicio="13:13"
    duracion_grabacion=5
    cantidad_videos=1

    def cargar_default(self):
        print("Load configuration...")
        
        try:
            archivo = open("tiempo.txt")
            self.f_actual=archivo.readline().replace('\n', '')
            self.h_actual=archivo.readline().replace('\n', '')
            self.tiempo_defecto=archivo.readline().replace('\n', '')
            self.h_inicio=archivo.readline().replace('\n', '')
            self.duracion_grabacion=int(archivo.readline().replace('\n', ''))
            self.cantidad_videos=int(archivo.readline())
        except:
            print("ERROR AL LEER TIEMPO.txt")
            self.f_actual="1/1/00"
            self.h_actual="12:12"
            self.tiempo_defecto="yes"
            self.h_inicio="00:00"
            self.duracion_grabacion=5
            self.cantidad_videos=1

            #txt = self.f_actual.split("/")
            
            #inicio= datetime(int(txt[2]), int(txt[1]), int(txt[0]),int(txt2[0]),int(txt2[1]))


        try:
            archivo = open("video.txt")
            self.windows_x=archivo.readline()
            self.windows_y=archivo.readline()
            comprimir=archivo.readline()
            if(comprimir[0]=="y"): self.modo_comprimir=1
            print("Resolution: "+self.windows_x+self.windows_y)
            archivo.close()
        except:
            print("ERROR AL LEER GRABACION.txt")
            self.windows_x=640
            self.windows_y=480
            self.modo_comprimir=0

        try:
            archivoRES = open("resolucion.txt")
            txt_i=archivoRES.readline().replace('\n', '')

            if(txt_i[0]=="y"): self.modo_offscreen=1
            else:
                txt_f=archivoRES.readline().replace('\n', '')
                if(txt_f[0]=="y"): self.modo_fullscreen=1
                else:
                    self.modo_fullscreen=0
                    self.windows_posx=int(archivoRES.readline())
                    self.windows_posy=int(archivoRES.readline())
                    self.resize=int(archivoRES.readline()) 
            archivoRES.close()
        except:
            print("ERROR AL LEER RESOLUCION.txt")
            self.modo_offscreen=0
            self.modo_fullscreen=1

        try:
            archivo3=open("crop.txt")
            self.crop_x=float(archivo3.readline().replace('\n', ''))
            self.crop_y=float(archivo3.readline().replace('\n', ''))
            self.crop_w=float(archivo3.readline().replace('\n', ''))
            self.crop_h=float(archivo3.readline().replace('\n', ''))

            
            if(self.crop_x==0.0 and self.crop_y==0.0 and self.crop_h==1.0 and self.crop_w==1.0):
                self.crop_bool=0
            else:
                self.crop_bool=1
        except:
            print("problema lectura crop")
            self.crop_bool=0
        try:
            formato="%Y%m%d-%H%M%S"
            fecha=datetime.now()
            self.name=fecha.strftime(formato)
        except:
            print("ERROR AL ESTABLECER FECHA.txt")


# DISPOSITIVOS USB

def get_usb_devices():
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices
    if 'usb' in dev.split('/')[5])
    return dict((os.path.basename(dev), dev) for dev in usb_devices)

# DIRECCION DEL USB

def get_mount_points(devices=None):
    devices = devices or get_usb_devices() # if devices are None: get_usb_devices
    output = check_output(['mount']).splitlines()
    output = [tmp.decode('UTF-8') for tmp in output]

    def is_usb(path):
        return any(dev in path for dev in devices)
    usb_info=(line for line in output if is_usb(line.split()[0]))
    #result=[(info.split()[0],info.split()[2]) for info in usb_info]
    result=[(info.split()[2]) for info in usb_info]
    
    if len(result):
        return result.pop()
    else:
        print('CONECTE UN DISPOSITIVO USB PARA GRABAR!' )
        blink_error()

def setup():
    GPIO.setmode(GPIO.BOARD)            # Numbers GPIOs by physical location
    GPIO.setup(ErrorPin, GPIO.OUT)      # Set pin mode as output
    GPIO.output(ErrorPin, GPIO.LOW)    # Set pin low to turn on led
    GPIO.setup(RecLed, GPIO.OUT)      # Set pin mode as output
    GPIO.output(RecLed, GPIO.LOW)    # Set pin low to turn on led

def blink_error():
    while True:
        GPIO.output(ErrorPin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(ErrorPin, GPIO.LOW)
        time.sleep(0.3)

def blink_rec():
    GPIO.output(RecLed, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(RecLed, GPIO.LOW)
    time.sleep(0.2)

def main():
    setup()
    completed=0
    t_preview=2
    roiX=roiY=roiW=roiH=0.0
    #make destination direcory
    dstDir = get_mount_points()  + '/'
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)



    #CANTIDAD DE VIDEOS
    archivo = open("tiempo.txt")
    fecha_hoy=archivo.readline()
    hora_hoy=archivo.readline()
    buffer=archivo.readline()
    hora_inicio=archivo.readline()
    buffer=archivo.readline()
    cant=int(float(archivo.readline()))
    archivo.close()

    #hora_inicio="12:24"
    
    start=dt.datetime.now()
    
    txt2 = hora_inicio.split(":")
    inicio=dt.datetime.now()
    inicio=inicio.replace(hour=int(txt2[0]), minute=int(txt2[1]))

    sleep(3)
    while(dt.datetime.now()<inicio):
        sleep(1)
    
    for _ in range(cant):
        start=dt.datetime.now()
        try:
            newVideo=Video()
            newVideo.cargar_default()
            t_record=(newVideo.duracion_grabacion)*1
            thisVideoFile=dstDir + newVideo.name + '.h264'
            camera=PiCamera()
            
                #camera.sensor_mode = 1 
                #camera.framerate = 25
            if(newVideo.crop_bool==1):
                print("MODO CROP: "+str(newVideo.crop_x)+str(newVideo.crop_y)+str(newVideo.crop_w)+str(newVideo.crop_h))
                regionOfInterest = (float(newVideo.crop_x),float(newVideo.crop_y),float(newVideo.crop_w),float(newVideo.crop_h))
                (roiX, roiY, roiW, roiH) = regionOfInterest
                #(roiX2, roiY2, roiW2, roiH2)= regionOfInterest
                width  = int(newVideo.windows_x)*roiW                     #Desired width
                height = int(newVideo.windows_y)*roiH                    #Desired height
                        
                percentAspectRatio = roiW/roiH                #Ratio in percent of size 
                imageAspectRatio   = width/height             #Desired aspect ratio
                sensorAspectRatio  = int(newVideo.windows_x)/int(newVideo.windows_y) #Physical sensor aspect ratio       

                        #The sensor is automatically cropped to fit current aspect ratio 
                        #so we need to adjust zoom to take that into account
                #if (imageAspectRatio > sensorAspectRatio):    
                #    roiY = (roiY - 0.5) * percentAspectRatio + 0.5  
                #    roiH = roiW                                  
                
                #if (imageAspectRatio < sensorAspectRatio):   
                #    roiX = (roiX - 0.5) * percentAspectRatio + 0.5  
                #    roiW = roiH 
                
                camera.resolution=(int(newVideo.windows_x),int(newVideo.windows_y))
                        
                camera.zoom=(roiX,roiY,roiW,roiH)
                #camera.zoom=(roiX2/int(newVideo.windows_x),roiY2/int(newVideo.windows_y),roiW2/int(newVideo.windows_x),roiH2/int(newVideo.windows_y))
                #print("CROP DE ZOOM:"+str(roiX/())+"XXX"+str(roiY)+"XXX"+str(roiW)+"XXX"+str(roiH)+"XXX")
                camera.start_preview()
                camera.start_recording(thisVideoFile)
            else:
                if newVideo.modo_fullscreen==0:
                    print("MODO NO-FULL-SCREEN: "+str(newVideo.windows_x)+" "+str(newVideo.windows_y))
                    camera.resolution = (int(newVideo.windows_x),int(newVideo.windows_y))
                    camera.start_preview(fullscreen=False,window=(newVideo.windows_posx,newVideo.windows_posy,int(newVideo.windows_x/newVideo.resize),int(newVideo.windows_y/newVideo.resize)))
                    camera.start_recording(thisVideoFile)
                else:
                    print("MODO FULL-SCREEN: "+str(newVideo.windows_x)+" "+str(newVideo.windows_y))
                    camera.resolution = (int(newVideo.windows_x),int(newVideo.windows_y))
                    camera.start_preview(fullscreen=True)
                    camera.start_recording(thisVideoFile)
            while (dt.datetime.now() - start).seconds < t_record: 
                    camera.wait_recording(.5)
                    blink_rec()
            camera.stop_recording()
            camera.close()
            completed=1
                            
        except KeyboardInterrupt:
            print("terminando antes")
            camera.stop_preview()
            camera.stop_recording()
            camera.close()
            completed=1
            break

        if(completed==1):
            #print("GRABAR EN: "+get_mount_points())           
            completed_video= os.path.join(get_mount_points(), thisVideoFile)
            #print("Camera stop recording")
            if(newVideo.modo_comprimir==1):
                #print("Beginning Convertion")
                command = "MP4Box -add {} {}.mp4; rm {}".format(completed_video, os.path.splitext(thisVideoFile)[0],completed_video)
                try:
                    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
                except subprocess.CalledProcessError as e:
                    print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))
    GPIO.cleanup()

if __name__ == "__main__":
    main()



            
