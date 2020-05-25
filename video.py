import os
import sys
from glob import glob

import subprocess
from subprocess import check_output, CalledProcessError
#asd

import picamera
from picamera import PiCamera
import time
#from time import sleep
import datetime 


class Video():
    crop_bool=0
    modo_fullscreen=1
    windows_x=0
    windows_y=0
    resize=1
    crop_x=0
    crop_y=0
    crop_w=1
    crop_h=1
    windows_posx=0
    windows_posy=0
    num_video=0
    duracion_grabacion=0


    def cargar_default(self):
        
        print("LEYENDO VALORES DE LOS TXT")
        try:
            archivo = open("grabacion.txt")
            self.duracion_grabacion=int(float(archivo.readline()
))
            self.cantidad_videos=int(float(archivo.readline()))
            self.windows_x=archivo.readline()
            self.windows_y=archivo.readline()
            print("SETEO DE RESOLUCION: "+self.windows_x+self.windows_y)
            archivo.close()
            print("VALORES CARGADOS")
        except:
            print("ERROR AL LEER GRABACION.txt")
            self.duracion_grabacion=5
            self.cantidad_videos=1    

        try:
            print("LEE RESOLUCION")
            archivoRES = open("resolucion.txt")
            txt_f=archivoRES.readline()
            if(txt_f[0]=="y"): self.modo_fullscreen=1
            else:
                self.modo_fullscreen=0
                self.windows_posx=int(archivoRES.readline())
                self.windows_posy=int(archivoRES.readline())
                self.resize=int(archivoRES.readline())      
            archivoRES.close()
        except:
            print("ERROR AL LEER RESOLUCION.txt")

        try:
            archivo3=open("crop.txt")
            self.crop_x=float(archivo3.readline().replace('\n', ''))
            self.crop_y=float(archivo3.readline().replace('\n', ''))
            self.crop_w=float(archivo3.readline().replace('\n', ''))
            self.crop_h=float(archivo3.readline().replace('\n', ''))
            print("LECTURA CROP")
            
            if(str(self.crop_x)=="0.0" and str(self.crop_y)=="0.0" and str(self.crop_h)=="1.0" and str(self.crop_w)=="1.0"):
                self.crop_bool=0
            else:
                self.crop_bool=1
            print("VALOR BOOL CROP: "+str(crop_bool))

        except:
            print("problema lectura crop")
            self.crop_bool=0


        try:
            archi_acum=open("num.txt")
            self.num_video=archi_acum.readline().replace('\n', '')
            archi_acum.close()
            self.num_video=int(self.num_video)+1   
            archi_acum2=open("num.txt", 'w')
            archi_acum2.write(str(self.num_video))
            archi_acum2.close()
            print("VIDEO N~: "+str(self.num_video))
        except:
            print("ERROR AL LEER NUM.txt")



def get_usb_devices():
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices
    if 'usb' in dev.split('/')[5])
    return dict((os.path.basename(dev), dev) for dev in usb_devices)

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
        print('No USB Drive' )
        blink_error()


def main():
    completed=0
    t_preview=2

    #make destination direcory
    dstDir = get_mount_points()  + '/'
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)

    
    newVideo= Video()
    newVideo.cargar_default()
    t_record=newVideo.duracion_grabacion
    thisVideoFile=dstDir + str(newVideo.num_video) + '.h264'
    try:
        camera=PiCamera()
            #camera.sensor_mode = 1 
            #camera.framerate = 25
        if(newVideo.crop_bool==1):
            print(str(newVideo.crop_x)+str(newVideo.crop_y)+str(newVideo.crop_w)+str(newVideo.crop_h))
            regionOfInterest = (float(newVideo.crop_x),float(newVideo.crop_y),float(newVideo.crop_w),float(newVideo.crop_h))
            (roiX, roiY, roiW, roiH) = regionOfInterest
                    
            width  = int(newVideo.windows_x)*roiW                     #Desired width
            height = int(newVideo.windows_y)*roiH                    #Desired height
                    
            percentAspectRatio = roiW/roiH                #Ratio in percent of size 
            imageAspectRatio   = width/height             #Desired aspect ratio
            sensorAspectRatio  = int(newVideo.windows_x)/int(newVideo.windows_y) #Physical sensor aspect ratio       

                    #The sensor is automatically cropped to fit current aspect ratio 
                    #so we need to adjust zoom to take that into account
            if (imageAspectRatio > sensorAspectRatio):    
                roiY = (roiY - 0.5) * percentAspectRatio + 0.5  
                roiH = roiW                                  
            
            if (imageAspectRatio < sensorAspectRatio):   
                roiX = (roiX - 0.5) * percentAspectRatio + 0.5  
                roiW = roiH 
            
            camera.resolution=(int(newVideo.windows_x),int(newVideo.windows_y))
                    
            camera.zoom=(roiX,roiY,roiW,roiH)
            camera.start_preview()
            camera.stop_preview()


            camera.start_recording(thisVideoFile)
            #time.sleep(1)
            camera.wait_recording(t_preview)

            camera.wait_recording(t_record)
            camera.stop_recording()
            camera.close()
            completed=1
        else:
            if newVideo.modo_fullscreen==0:
                print("MODO NO-FULL-SCREEN: "+str(newVideo.windows_x)+" "+str(newVideo.windows_y))
                camera.resolution = (int(newVideo.windows_x),int(newVideo.windows_y))
                camera.start_preview(fullscreen=False,window=(newVideo.windows_posx,newVideo.windows_posy,int(640/newVideo.resize),int(480/newVideo.resize)))
                camera.start_recording(thisVideoFile)
                #time.sleep(1)
                camera.wait_recording(t_record)
                camera.stop_preview()
                camera.close()  
                completed=1   
            else:
                print("MODO FULL-SCREEN: "+str(newVideo.windows_x)+" "+str(newVideo.windows_y))
                camera.resolution = (int(newVideo.windows_x),int(newVideo.windows_y))
                camera.start_preview(fullscreen=True)
                camera.start_recording(thisVideoFile)
                #time.sleep(1)
                camera.wait_recording(t_record)
                camera.stop_preview()
                camera.close()
                completed=1     
                        
    except KeyboardInterrupt:
                print("terminando antes")
                camera.stop_preview()
                camera.stop_recording()
                camera.close()
    completed=1
    if(completed==1):
        print("GRABAR EN: "+get_mount_points())
        
        completed_video= os.path.join(get_mount_points(), thisVideoFile)
        print("Camera finished recording... Beginning Convertion")

        from subprocess import CalledProcessError
        command = "MP4Box -add {} {}.mp4; rm {}".format(completed_video, os.path.splitext(thisVideoFile)[0],completed_video)
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))

if __name__ == "__main__":
    main()



            
