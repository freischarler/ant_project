
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


    def cargar_default():
        print("LEYENDO VALORES DE LOS TXT")
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

            print("LEE GRABACION")

            archivo = open("grabacion.txt")
            self.duracion_grabacion=archivo.readline()
            self.cantidad_videos=archivo.readline()
            self.windows_x=archivo.readline()
            self.windows_y=archivo.readline()
            print("SETEO DE RESOLUCION: "+self.windows_x+self.windows_y)
            archivo.close()
            print("VALORES CARGADOS")
        except:
            self.duracion_grabacion=5
            self.cantidad_videos=1    
    
def main():
    newVideo= Video()
    newVideo.cargar_default

    try:
        camera=PiCamera()
            #print("CROP BOOL RECIBIDO"+str(self.crop_bool))
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
            
            newVideo.actionactionStop.setEnabled(True)
            camera.resolution=(int(newVideo.windows_x),int(newVideo.windows_y))
                    
            camera.zoom=(roiX,roiY,roiW,roiH)
            camera.start_preview()
                    #camera.start_recording("pythonVideo.h264")
            time.sleep(5)
            camera.stop_preview()
            camera.close()                
        else:
            if newVideo.modo_fullscreen==0:
                print("MODO NO-FULL-SCREEN: "+str(newVideo.windows_x)+" "+str(newVideo.windows_y))
                camera.resolution = (int(newVideo.windows_x),int(newVideo.windows_y))
                camera.start_preview(fullscreen=False,window=(newVideo.windows_posx,newVideo.windows_posy,int(640/newVideo.resize),int(480/newVideo.resize)))
                time.sleep(5)
                camera.stop_preview()
                camera.close()        
            else:
                print("MODO FULL-SCREEN: "+str(newVideo.windows_x)+" "+str(newVideo.windows_y))
                camera.resolution = (int(newVideo.windows_x),int(newVideo.windows_y))
                camera.start_preview(fullscreen=True)
                time.sleep(5)
                camera.stop_preview()
                camera.close()        
                        
    except KeyboardInterrupt:
                print("interrumpiendo")
                camera.stop_preview()
                camera.close()                

if __name__ == "__main__":
    main()



            
