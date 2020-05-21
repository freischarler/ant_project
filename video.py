

self.cargar_default()
        #print(str(self.crop_bool))
        try:
            camera=PiCamera()
            #print("CROP BOOL RECIBIDO"+str(self.crop_bool))
            if(self.crop_bool==1):
                print(str(self.crop_x)+str(self.crop_y)+str(self.crop_w)+str(self.crop_h))
                regionOfInterest = (float(self.crop_x),float(self.crop_y),float(self.crop_w),float(self.crop_h))
                (roiX, roiY, roiW, roiH) = regionOfInterest
                
                width  = int(self.windows_x)*roiW                     #Desired width
                height = int(self.windows_y)*roiH                    #Desired height
                
                percentAspectRatio = roiW/roiH                #Ratio in percent of size 
                imageAspectRatio   = width/height             #Desired aspect ratio
                sensorAspectRatio  = int(self.windows_x)/int(self.windows_y) #Physical sensor aspect ratio       

                #The sensor is automatically cropped to fit current aspect ratio 
                #so we need to adjust zoom to take that into account
                if (imageAspectRatio > sensorAspectRatio):    
                    roiY = (roiY - 0.5) * percentAspectRatio + 0.5  
                    roiH = roiW                              
        
                if (imageAspectRatio < sensorAspectRatio):   
                    roiX = (roiX - 0.5) * percentAspectRatio + 0.5  
                    roiW = roiH 
                self.actionactionStop.setEnabled(True)
                camera.resolution=(int(self.windows_x),int(self.windows_y))
                
                camera.zoom=(roiX,roiY,roiW,roiH)
                camera.start_preview()
                #camera.start_recording("pythonVideo.h264")
                time.sleep(5)
                camera.stop_preview()
                camera.close()
            else:
                if self.modo_fullscreen==0:
                    print("MODO NO-FULL-SCREEN: "+str(self.windows_x)+" "+str(self.windows_y))
                    camera.resolution = (int(self.windows_x),int(self.windows_y))
                    camera.start_preview(fullscreen=False,window=(self.windows_posx,self.windows_posy,int(640/self.resize),int(480/self.resize)))
                    time.sleep(5)
                    camera.stop_preview()
                    camera.close()
                else:
                    print("MODO FULL-SCREEN: "+str(self.windows_x)+" "+str(self.windows_y))
                    camera.resolution = (int(self.windows_x),int(self.windows_y))
                    camera.start_preview(fullscreen=True)
                    time.sleep(5)
                    camera.stop_preview()
                    camera.close()
                    
        except KeyboardInterrupt:
            print("interrumpiendo")
            camera.stop_preview()
            camera.close()

            
def cargar_default(self):
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