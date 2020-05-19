# Autor: Martin Omar Paz


#import picamera
#from picamera import PiCamera5
import time
from time import sleep
import datetime 

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QAction


	#-----------------------------
	#	VENTANA DE CONFIGURACION DE PANTALLA
	#-----------------------------
	
class Ui_ConfigurarPantalla(object):
    tiempo_finalizacion=0
    duracion_grabacion=0
    cantidad_videos=0
    resolucion_x=640
    resolucion_y=480
    comprimir="no"
    resize=1
    

    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 391)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 601, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 391, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.le_inicio = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.le_inicio.setObjectName("le_inicio")
        self.horizontalLayout_3.addWidget(self.le_inicio)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.le_duracion = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.le_duracion.setDecimals(0)
        self.le_duracion.setObjectName("le_duracion")
        self.horizontalLayout_5.addWidget(self.le_duracion)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.le_cantidad = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.le_cantidad.setDecimals(0)
        self.le_cantidad.setObjectName("le_cantidad")
        self.horizontalLayout.addWidget(self.le_cantidad)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.le_finalizacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.le_finalizacion.setObjectName("le_finalizacion")
        self.horizontalLayout_6.addWidget(self.le_finalizacion)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.qbox_resolucion = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.qbox_resolucion.setObjectName("qbox_resolucion")
        self.horizontalLayout_7.addWidget(self.qbox_resolucion)
        self.checkBox_convertir = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_convertir.setObjectName("checkBox_convertir")
        self.horizontalLayout_7.addWidget(self.checkBox_convertir)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setGeometry(QtCore.QRect(50, 80, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.check_fullscreen = QtWidgets.QCheckBox(self.tab_3)
        self.check_fullscreen.setGeometry(QtCore.QRect(120, 30, 161, 23))
        self.check_fullscreen.setObjectName("check_fullscreen")
        #self.check_fullscreen.setChecked(False)        
        self.le_wx = QtWidgets.QLineEdit(self.tab_3)
        self.le_wx.setGeometry(QtCore.QRect(140, 110, 113, 25))
        self.le_wx.setObjectName("le_wx")
        self.le_wx.setEnabled(True)
        self.le_wy = QtWidgets.QLineEdit(self.tab_3)
        self.le_wy.setGeometry(QtCore.QRect(140, 140, 113, 25))
        self.le_wy.setObjectName("le_wy")
        self.le_wy.setEnabled(True)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(120, 110, 16, 17))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(120, 140, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(280, 110, 61, 21))
        self.label_8.setObjectName("label_8")
        self.cbox_size = QtWidgets.QComboBox(self.tab_3)
        self.cbox_size.setGeometry(QtCore.QRect(350, 110, 101, 25))
        self.cbox_size.setObjectName("cbox_size")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(50, 180, 491, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lb_image = QtWidgets.QLabel(self.tab_2)
        self.lb_image.setEnabled(True)
        self.lb_image.setGeometry(QtCore.QRect(220, 30, 320, 240))
        self.lb_image.setStatusTip("")
        self.lb_image.setText("")
        self.lb_image.setTextFormat(QtCore.Qt.PlainText)
        self.lb_image.setObjectName("lb_image")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(40, 30, 21, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(40, 70, 21, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 51, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 150, 31, 17))
        self.label_13.setObjectName("label_13")
        self.crop_x = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.crop_x.setGeometry(QtCore.QRect(70, 30, 69, 26))
        self.crop_x.setDecimals(2)
        self.crop_x.setMaximum(1.0)
        self.crop_x.setSingleStep(0.1)
        self.crop_x.setObjectName("crop_x")
        self.crop_y = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.crop_y.setGeometry(QtCore.QRect(70, 70, 69, 26))
        self.crop_y.setDecimals(2)
        self.crop_y.setMaximum(1.0)
        self.crop_y.setSingleStep(0.1)
        self.crop_y.setObjectName("crop_y")
        self.crop_width = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.crop_width.setGeometry(QtCore.QRect(70, 110, 69, 26))
        self.crop_width.setDecimals(2)
        self.crop_width.setMaximum(1.0)
        self.crop_width.setSingleStep(0.1)
        self.crop_width.setProperty("value", 1.0)
        self.crop_width.setObjectName("crop_width")
        self.crop_height = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.crop_height.setGeometry(QtCore.QRect(70, 150, 69, 26))
        self.crop_height.setDecimals(2)
        self.crop_height.setMaximum(1.0)
        self.crop_height.setSingleStep(0.1)
        self.crop_height.setProperty("value", 1.0)
        self.crop_height.setObjectName("crop_height")
        self.button_preview = QtWidgets.QPushButton(self.tab_2)
        self.button_preview.setGeometry(QtCore.QRect(40, 210, 89, 25))
        self.button_preview.setObjectName("button_preview")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(163, 30, 20, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab_2, "")

        #------------------------------------------------------
        # AGREGADO DE RESOLUCION Y RESIZE
        #------------------------------------------------------

        self.cbox_size.addItem("1")
        self.cbox_size.addItem("2")
        self.cbox_size.addItem("3")
        self.qbox_resolucion.addItem("1920x1080")
        self.qbox_resolucion.addItem("1640x1232")
        self.qbox_resolucion.addItem("1280x720")
        self.qbox_resolucion.addItem("640x480")
        
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.cargar_default()
        
	#-----------------------------
	#	INICIO DE FUNCIONES
	#-----------------------------

        self.button_preview.clicked.connect(self.preview_image)
        self.crop_x.valueChanged.connect(self.mantener_cuadroX)
        self.crop_y.valueChanged.connect(self.mantener_cuadroY)
        self.check_fullscreen.toggled.connect(self.fullscreen)
        self.pushButton.clicked.connect(self.preview_video)
        self.le_duracion.valueChanged.connect(self.actualizar)
        self.le_cantidad.valueChanged.connect(self.actualizar)
        self.checkBox_convertir.toggled.connect(self.actualizar)
        self.le_wx.textChanged.connect(self.actualizar_2)
        self.le_wy.textChanged.connect(self.actualizar_2)
        self.cbox_size.currentIndexChanged.connect(self.actualizar_2)
        
	#-----------------------------
	#	PESTANIA de TIEMPO
	#   Permite configurar el inicio,fin y resolucion del video
	#-----------------------------
	
    def cargar_default(self):
        #CARGAMOS VALORES DE LA VENTANA DE TIEMPO
        try:
            archivo=open("grabacion.txt")
            self.duracion_grabacion=archivo.readline()
            self.cantidad_videos=archivo.readline()
            self.resolucion_x=archivo.readline()
            self.resolucion_y=archivo.readline()
            self.comprimir=archivo.readline()
            archivo.close()
        except:
            duracion_grabacion=5
            cantidad_videos=1
            resolucion_x=640
            resolucion_y=480
            comprimir="no"
            archivo=open("grabacion.txt", 'w')
            archivo.write(str(self.duracion_grabacion)+"\n") 
            archivo.write(str(self.cantidad_videos)+"\n")
            archivo.write(str(self.resolucion_x)+"\n")
            archivo.write(str(self.resolucion_y)+"\n")
            archivo.write(str(self.comprimir))
            archivo.close()
        if(self.comprimir[0]=="y"): 
            self.checkBox_convertir.setChecked(True)
        self.le_cantidad.setValue(float(self.cantidad_videos))
        self.le_duracion.setValue(float(self.duracion_grabacion))

                ######################################
                #NO FUNCIONA BUSCAR LA RESOLUCION
                ######################################

        if(self.resolucion_x[:2]=="19"): 
            self.qbox_resolucion.setCurrentIndex(self.qbox_resolucion.findText("1920x1080"))

        ######################################
        #CARGAMOS VALORES DE LA VENTANA VISUALIZACION
        ######################################

        try:
            archivo=open("resolucion.txt")
            txt_f=archivo.readline()
            if(txt_f[0]=="y"):
                self.check_fullscreen.setChecked(True)
                self.le_wx.setEnabled(False)
                self.le_wy.setEnabled(False)
                self.cbox_size.setEnabled(False)        
                archivo.close()
            else:
                txt_x=archivo.readline()
                txt_y=archivo.readline()
                txt_s=archivo.readline()
                self.check_fullscreen.setChecked(False)
                self.le_wx.setText(txt_x)
                self.le_wy.setText(txt_y)
                #self.cbox_size PENDIENTE CAMBIAR CBOX
                archivo.close()
        except:
            self.check_fullscreen.setChecked(True)



    def actualizar(self):
        f_inicio=self.le_inicio.text()
        self.duracion_grabacion=self.le_duracion.value()
        self.cantidad_videos=self.le_cantidad.value()     
        index = self.qbox_resolucion.currentIndex()
        if(index==0): 
            self.resolucion_x=1920 
            self.resolucion_y=1080
        if(index==1): 
            self.resolucion_x=1640 
            self.resolucion_y=1232
        if(index==2): 
            self.resolucion_x=1280 
            self.resolucion_y=720
        if(index==3): 
            self.resolucion_x=640 
            self.resolucion_y=480

        if(self.checkBox_convertir.isChecked()):
            self.comprimir="yes"
        else:
            self.comprimir="no"

        t_total=int(self.duracion_grabacion*self.cantidad_videos)
        
        t=datetime.time(int(f_inicio[:2]),int(f_inicio[3:]))
        if (int(t_total)+t.minute)>=60:
            if(t.hour+int(int(t_total+t.minute)/60)>23):
                 t=datetime.time(int(f_inicio[:2])+int(int(t_total+t.minute)/60)-24,int(f_inicio[3:])+int(int(t_total+t.minute)%60))
            else:
                t=datetime.time(int(f_inicio[:2])+int(int(t_total+t.minute)/60),int(f_inicio[3:])+int(int(t_total+t.minute)%60))
        else:
            t=datetime.time(int(f_inicio[:2]),int(f_inicio[3:])+int(t_total))
        tiempo_finalizacion=t

        self.le_finalizacion.setText(str(t.hour)+':'+str(t.minute))
        self.grabar_datos() #grabamos duracion y cantidad

    def grabar_datos(self):
        archivo = open("grabacion.txt",'w')
        archivo.write(str(self.duracion_grabacion)+"\n")
        archivo.write(str(self.cantidad_videos)+"\n")
        archivo.write(str(self.resolucion_x)+"\n")
        archivo.write(str(self.resolucion_y)+"\n")
        archivo.write(str(self.comprimir))
        archivo.close()

	#-----------------------------
	#	PESTANIA de PREVIEW_VIDEO
	#   Permite acomodar el video en la pantalla o fullscreen
	#-----------------------------

    def preview_video(self):
        camera=PiCamera()
        camera.resolution = (self.resolucion_x,self.resolucion_y)
        archivo = open("resolucion.txt")
        txt=archivo.readline()
        if(self.check_fullscreen.isChecked()):
            camera.start_preview(fullscreen=True)
            archivo = open("resolucion.txt",'w')
            archivo.write("yes"+"\n"+str(0)+"\n"+str(0))
            archivo.close()
        else:
            txt=self.le_wx.text()
            txt2=self.le_wy.text()
            resize=int(self.cbox_size.currentText())
            archivo = open("resolucion.txt",'w')
            wx=self.le_wx.text()
            wy=self.le_wy.text()
            archivo.write("no"+"\n"+wx+"\n"+wy+"\n"+str(resize))
            archivo.close()   
            camera.start_preview(fullscreen=False, window=(int(txt),int(txt2),int(640/resize),int(480/resize)))
        time.sleep(3)
        camera.stop_preview()
        camera.close()

    def actualizar_2(self):
        archivo = open("resolucion.txt",'w')
        wx=self.le_wx.text()
        wy=self.le_wy.text()
        size=self.cbox_size.currentIndex()
        print("BANDERAAAA")
        archivo.write("no"+"\n"+wx+"\n"+wy+"\n"+str(size))
        archivo.close()


    def fullscreen(self):
        if (self.check_fullscreen.isChecked()):
            self.le_wx.setEnabled(False)
            self.le_wy.setEnabled(False)
            self.cbox_size.setEnabled(False)        
        else:
            self.le_wx.setEnabled(True)
            self.le_wy.setEnabled(True)
            self.cbox_size.setEnabled(True)
        
        archivo = open("resolucion.txt",'w')
        self.resize=self.cbox_size.currentText()
        archivo.write("yes"+"\n"+"0"+"\n"+"0"+"\n"+str(self.resize))
        archivo.close()   

	#-----------------------------
	#	PESTANIA de Crop
	#   Mantiene el cuadrado dentro de los limites
	#-----------------------------

    def mantener_cuadroX(self):
        x=self.crop_x.value()
        w=self.crop_width.value()		
        if (x+w)>1:
            self.crop_width.setValue(1-x)

    def mantener_cuadroY(self):
        y=self.crop_y.value()
        w=self.crop_height.value()		
        if (y+w)>1:
            self.crop_height.setValue(1-y)  	

	#-----------------------------
	#	PESTANIA de CROP
	#   Vista previa del crop
	#-----------------------------

    def preview_image(self):
        camera=PiCamera()
        #camera.start_preview()
        #sleep(0)
        camera.resolution = (640,480)
        camera.capture('/home/pi/Desktop/ant_project/image.jpg')
        #camera.stop_preview()
        camera.close()
        #camera.stop_recording()
		
        filename = "image.jpg"
        # convert image file into pixmap
        self.pixmap_image = QtGui.QPixmap(filename)

        # create painter instance with pixmap
        self.painterInstance = QtGui.QPainter(self.pixmap_image)

        # set rectangle color and thickness
        self.penRectangle = QtGui.QPen(QtCore.Qt.red)
        self.penRectangle.setWidth(3)

        lbw=self.lb_image.width()
        lbh=self.lb_image.height()
        
		# draw rectangle on painter
        cx=self.crop_x.value()*lbw*2
        cy=self.crop_y.value()*lbh*2
        cw=self.crop_width.value()*lbw*2
        ch=self.crop_height.value()*lbh*2

        self.pixmap_image.scaled(lbw,lbh)

        self.lb_image.setScaledContents(True)
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(cx,cy,cw,ch)
        self.painterInstance.end()
        self.lb_image.setPixmap(self.pixmap_image)
        self.lb_image.show()
        archivo=open("crop.txt", 'w')
        #archivo.write(str(cx)+"\n"+str(cy)+"\n"+str(cw)+"\n"+str(ch))
        archivo.write(str(self.crop_x.value())+"\n"+str(self.crop_y.value())+"\n"+str(self.crop_width.value())+"\n"+str(self.crop_height.value()))
        archivo.close()

	#-----------------------------
	#	NOMBRE DE OBJETOS
	#-----------------------------


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Inicio (hora):"))
        self.label_2.setText(_translate("Dialog", "Duración (minutos):"))
        self.label_4.setText(_translate("Dialog", "Cantidad de videos:"))
        self.label_6.setText(_translate("Dialog", "Finalización(hora):"))
        self.le_finalizacion.setText(_translate("Dialog", "00:00"))
        self.label_7.setText(_translate("Dialog", "Resolución"))
        self.checkBox_convertir.setText(_translate("Dialog", "Convertir .mp4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tiempo"))
        self.check_fullscreen.setText(_translate("Dialog", "Fullscreen"))
        self.label.setText(_translate("Dialog", "x"))
        self.label_5.setText(_translate("Dialog", "y"))
        self.label_8.setText(_translate("Dialog", "Escala %"))
        self.pushButton.setText(_translate("Dialog", "Ver"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Visualizacion"))
        self.label_10.setText(_translate("Dialog", "X"))
        self.label_11.setText(_translate("Dialog", "Y"))
        self.label_12.setText(_translate("Dialog", "Ancho"))
        self.label_13.setText(_translate("Dialog", "Alto"))
        self.button_preview.setText(_translate("Dialog", "Ver"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Crop"))


class Ui_ConeccionWifi(object):
    def setupUi(self, ConeccionWifi):
        ConeccionWifi.setObjectName("ConeccionWifi")
        ConeccionWifi.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConeccionWifi)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.le_ssid = QtWidgets.QLineEdit(ConeccionWifi)
        self.le_ssid.setGeometry(QtCore.QRect(190, 40, 113, 25))
        self.le_ssid.setObjectName("le_ssid")
        self.le_pwd = QtWidgets.QLineEdit(ConeccionWifi)
        self.le_pwd.setGeometry(QtCore.QRect(190, 80, 113, 25))
        self.le_pwd.setObjectName("le_pwd")
        self.label = QtWidgets.QLabel(ConeccionWifi)
        self.label.setGeometry(QtCore.QRect(110, 40, 31, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ConeccionWifi)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton_conectar = QtWidgets.QPushButton(ConeccionWifi)
        self.pushButton_conectar.setGeometry(QtCore.QRect(150, 120, 89, 25))
        self.pushButton_conectar.setObjectName("pushButton_conectar")
        self.label_3 = QtWidgets.QLabel(ConeccionWifi)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lb_estadoWifi = QtWidgets.QLabel(ConeccionWifi)
        self.lb_estadoWifi.setGeometry(QtCore.QRect(180, 160, 131, 21))
        self.lb_estadoWifi.setObjectName("lb_estadoWifi")

        self.retranslateUi(ConeccionWifi)
        self.buttonBox.accepted.connect(ConeccionWifi.accept)
        self.buttonBox.rejected.connect(ConeccionWifi.reject)
        QtCore.QMetaObject.connectSlotsByName(ConeccionWifi)

        self.pushButton_conectar.clicked.connect(self.conectar_Wifi)

    def conectar_Wifi(self):
        ssid = self.le_ssid.text()
        passw = self.le_pwd.text()
        try:
            command1 = "echo 'network={' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
            command2 = "echo '        ssid=\"" + ssid + "\"' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
            command3 = "echo '        psk=\""  + passw + "\"' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
            command4 = "echo '        key_mgmt=WPA-PSK' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
            command5 = "echo '}' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
            self.lb_estadoWifi.setText("Conectado")
            self.lb_estadoWifi.setStyleSheet("color: rgb(78, 154, 6);")
        except:
            self.lb_estadoWifi.setText("Desconectado")
            self.lb_estadoWifi.setStyleSheet("color: rgb(239, 41, 41);")
        self.lb_estadoWifi.setFont(QtGui.QFont("Ubuntu",weight=QtGui.QFont.Bold))

    def retranslateUi(self, ConeccionWifi):
        _translate = QtCore.QCoreApplication.translate
        ConeccionWifi.setWindowTitle(_translate("Dialog", "Configuración de Conexion"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>SSID</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.pushButton_conectar.setText(_translate("Dialog", "Conectar"))
        self.label_3.setText(_translate("Dialog", "Estado:"))
        self.lb_estadoWifi.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ef2929;\">Desconectado</span></p></body></html>"))

class ConeccionWifi(QDialog):
                                   # <===
    def __init__(self, *args, **kwargs):
        super(ConeccionWifi, self).__init__(*args, **kwargs)
        self.setWindowTitle("Configuracion de Wifi")

class ConfigurarPantalla(QDialog):
                                   # <===
    def __init__(self, *args, **kwargs):
        super(ConfigurarPantalla, self).__init__(*args, **kwargs)
        self.setWindowTitle("Configuracion de Wifi")


class Ui_MainWindow(QMainWindow):
    
    modo_fullscreen="yes"
    windows_x=0
    windows_y=0
    resize=1
    crop_x=0
    crop_y=0
    crop_w=1
    crop_h=1
    sensorWidth=640
    sensorHeight=480

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(39, 20, 571, 103))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.t_temperatura = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.t_temperatura.setObjectName("t_temperatura")
        self.horizontalLayout_2.addWidget(self.t_temperatura)
        self.lb_temperatura = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lb_temperatura.setObjectName("lb_temperatura")
        self.horizontalLayout_2.addWidget(self.lb_temperatura)
        self.t_humedad = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.t_humedad.setObjectName("t_humedad")
        self.horizontalLayout_2.addWidget(self.t_humedad)
        self.lb_humedad = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lb_humedad.setObjectName("lb_humedad")
        self.horizontalLayout_2.addWidget(self.lb_humedad)
        self.t_luz = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.t_luz.setObjectName("t_luz")
        self.horizontalLayout_2.addWidget(self.t_luz)
        self.lb_luz = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lb_luz.setObjectName("lb_luz")
        self.horizontalLayout_2.addWidget(self.lb_luz)
        self.status_mainBar = QtWidgets.QLabel(self.centralwidget)
        self.status_mainBar.setEnabled(True)
        self.status_mainBar.setGeometry(QtCore.QRect(170, 130, 421, 39))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)    
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        self.status_mainBar.setPalette(palette)


        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.status_mainBar.setFont(font)
        self.status_mainBar.setObjectName("status_mainBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 140, 67, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuSistema = QtWidgets.QMenu(self.menubar)
        self.menuSistema.setObjectName("menuSistema")
        self.menuBase_de_Datox = QtWidgets.QMenu(self.menubar)
        self.menuBase_de_Datox.setObjectName("menuBase_de_Datox")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuConfiguraci_on = QtWidgets.QMenu(self.menubar)
        self.menuConfiguraci_on.setObjectName("menuConfiguraci_on")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionGrabar = QtWidgets.QAction(MainWindow)
        self.actionGrabar.setObjectName("actionGrabar")
        self.actionConexion = QtWidgets.QAction(MainWindow)
        self.actionConexion.setObjectName("actionConexion")
        self.actionConexion_configuracion = QtWidgets.QAction(MainWindow)
        self.actionConexion_configuracion.setObjectName("actionConexion_configuracion")
        self.actionRecord = QtWidgets.QAction(QIcon("play.png"), "Your button", self)
        self.actionRecord.setObjectName("actionRecord")
        self.actionactionStop = QtWidgets.QAction(QIcon("stop.png"), "Your button", self)
        self.actionactionStop.setObjectName("actionactionStop")
        self.actionConection = QtWidgets.QAction(QIcon("wifi.png"), "Your button", self)
        self.actionConection.setObjectName("actionConection")
        button_action = QAction(QIcon("bug.png"), "Your button", self)
        self.actionCargar_configuracion = QtWidgets.QAction(MainWindow)
        self.actionCargar_configuracion.setObjectName("actionCargar_configuracion")
        self.actionConsultarBD = QtWidgets.QAction(MainWindow)
        self.actionConsultarBD.setObjectName("actionConsultarBD")
        self.actionCargarBD = QtWidgets.QAction(MainWindow)
        self.actionCargarBD.setObjectName("actionCargarBD")
        self.actionGuardarBD = QtWidgets.QAction(MainWindow)
        self.actionGuardarBD.setObjectName("actionGuardarBD")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAcerca_de_Ant_Project = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de_Ant_Project.setObjectName("actionAcerca_de_Ant_Project")
        self.actionConfigurar = QtWidgets.QAction(QIcon("cfg.png"), "Your button", self)
        self.actionConfigurar.setObjectName("actionConfigurar")
        self.actionGuardar_configuracion = QtWidgets.QAction(MainWindow)
        self.actionGuardar_configuracion.setObjectName("actionGuardar_configuracion")
        self.actionPantalla_configuracion = QtWidgets.QAction(MainWindow)
        self.actionPantalla_configuracion.setObjectName("actionPantalla_configuracion")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionImprimir = QtWidgets.QAction(MainWindow)
        self.actionImprimir.setObjectName("actionImprimir")
        self.menuSistema.addSeparator()
        self.menuSistema.addSeparator()
        self.menuSistema.addAction(self.actionImprimir)
        self.menuSistema.addAction(self.actionSalir)
        self.menuBase_de_Datox.addSeparator()
        self.menuBase_de_Datox.addAction(self.actionConsultarBD)
        self.menuBase_de_Datox.addSeparator()
        self.menuBase_de_Datox.addAction(self.actionCargarBD)
        self.menuBase_de_Datox.addAction(self.actionGuardarBD)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionManual)
        self.menuAyuda.addAction(self.actionAcerca_de_Ant_Project)
        self.menuConfiguraci_on.addSeparator()
        self.menuConfiguraci_on.addAction(self.actionConexion_configuracion)
        self.menuConfiguraci_on.addAction(self.actionPantalla_configuracion)
        self.menuConfiguraci_on.addSeparator()
        self.menuConfiguraci_on.addAction(self.actionCargar_configuracion)
        self.menuConfiguraci_on.addAction(self.actionGuardar_configuracion)
        self.menubar.addAction(self.menuSistema.menuAction())
        self.menubar.addAction(self.menuConfiguraci_on.menuAction())
        self.menubar.addAction(self.menuBase_de_Datox.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionRecord)
        self.toolBar.addAction(self.actionactionStop)
        self.toolBar.addAction(self.actionConection)
        self.toolBar.addAction(self.actionConfigurar)
        #self.toolBar.addAction(self.actionConfiguration)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #----------------------------------------------------------
        #FUNCIONES DEL MENU
        #----------------------------------------------------------

        self.actionConexion_configuracion.triggered.connect(self.show_coneccion)
        self.actionConection.triggered.connect(self.show_coneccion)
        self.actionPantalla_configuracion.triggered.connect(self.show_pantalla)
        self.actionConfigurar.triggered.connect(self.show_pantalla)
        self.actionactionStop.triggered.connect(self.detener_grabacion)
        self.actionRecord.triggered.connect(self.grabar_video)
        self.actionGuardar_configuracion.triggered.connect(self.grabar_video)
        #self.actionConfiguration.triggered.connect(self.show_config)   
        #self.actionRecord.triggered.connect(self.grabar_video)    
        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.actionc_on.setText("Esperando orden...")

    def detener_grabacion(self):
        camera.stop_preview()
        camera.close()

    def grabar_video(self):
        self.cargar_default()
        try:
            camera=PiCamera()
            #print("BANDERA"+str(self.crop_x)+str(self.crop_y)+str(self.crop_w)+str(self.crop_h))
            regionOfInterest = (float(self.crop_x),float(self.crop_y),float(self.crop_h),float(self.crop_w))
            (roiX, roiY, roiW, roiH) = regionOfInterest

            width  = self.sensorWidth*roiW                     #Desired width
            height = self.sensorHeight*roiH                    #Desired height
    
            percentAspectRatio = roiW/roiH                #Ratio in percent of size 
            imageAspectRatio   = width/height             #Desired aspect ratio
            sensorAspectRatio  = self.sensorWidth/self.sensorHeight #Physical sensor aspect ratio       

    #The sensor is automatically cropped to fit current aspect ratio 
    #so we need to adjust zoom to take that into account
            if (imageAspectRatio > sensorAspectRatio):    
                roiY = (roiY - 0.5) * percentAspectRatio + 0.5  
                roiH = roiW                              
        
            if (imageAspectRatio < sensorAspectRatio):   
                roiX = (roiX - 0.5) * percentAspectRatio + 0.5  
                roiW = roiH 

            self.actionactionStop.setEnabled(True)
            camera.resolution=(int(width),int(height))
            camera.zoom=(roiX,roiY,roiW,roiH)
            camera.start_preview()
            camera.start_recording("pythonVideo.h264")
            time.sleep(5)
            camera.stop_preview()
            camera.close()
        except KeyboardInterrupt:
            print("interrumpiendo")
            camera.stop_preview()
            camera.close()

            
    def cargar_default(self):
        try:
            archivo3=open("crop.txt")
            self.crop_x=archivo3.readline()
            self.crop_y=archivo3.readline()
            self.crop_h=archivo3.readline()
            self.crop_w=archivo3.readline()
            archivo3.close()
            #print("LEE EL CROP")
            archivoRES = open("resolucion.txt")
            self.modo_fullscreen=archivoRES.readline()
            self.windows_x=int(archivoRES.readline())
            self.windows_y=int(archivoRES.readline())
            self.resize=int(archivoRES.readline())
            archivoRES.close()

            archivo = open("registros.txt")
            self.duracion_grabacion=archivo.readline()
            self.cantidad_videos=archivo.readline()
            archivo.close()
        except:
            self.duracion_grabacion=5
            self.cantidad_videos=1


    def show_pantalla(self):
        dialog = ConfigurarPantalla(self)  # self hace referencia al padre
        dialog.ui=Ui_ConfigurarPantalla()
        dialog.ui.setupUi(dialog)
        dialog.show()        

    def show_coneccion(self):                                             # <===
        dialog = ConeccionWifi(self)  # self hace referencia al padre
        dialog.ui=Ui_ConeccionWifi()
        dialog.ui.setupUi(dialog)
        dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.t_temperatura.setText(_translate("MainWindow", "Temperatura:"))
        self.lb_temperatura.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">15°</span></p></body></html>"))
        self.t_humedad.setText(_translate("MainWindow", "Humedad:"))
        self.lb_humedad.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">69%</span></p></body></html>"))
        self.t_luz.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Luz:</p></body></html>"))
        self.lb_luz.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">600 lux</span></p></body></html>"))
        self.status_mainBar.setText(_translate("MainWindow", "<html><head/><body><p>description</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Estado:"))
        self.menuSistema.setTitle(_translate("MainWindow", "Sistema"))
        self.menuBase_de_Datox.setTitle(_translate("MainWindow", "Base de Datos"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuConfiguraci_on.setTitle(_translate("MainWindow", "Configuracion"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionGrabar.setText(_translate("MainWindow", "Grabar"))
        self.actionConexion.setText(_translate("MainWindow", "Conexion"))
        self.actionConexion_configuracion.setText(_translate("MainWindow", "Conectar"))
        self.actionRecord.setText(_translate("MainWindow", "Grabar"))
        self.actionactionStop.setText(_translate("MainWindow", "Parar"))
        self.actionactionStop.setEnabled(False)
        self.actionConection.setText(_translate("MainWindow", "Conectar"))
        self.actionCargar_configuracion.setText(_translate("MainWindow", "Cargar configuracion"))
        self.actionConsultarBD.setText(_translate("MainWindow", "Consultar"))
        self.actionCargarBD.setText(_translate("MainWindow", "Cargar"))
        self.actionGuardarBD.setText(_translate("MainWindow", "Guardar"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAcerca_de_Ant_Project.setText(_translate("MainWindow", "Acerca de Ant Project"))
        self.actionConfigurar.setText(_translate("MainWindow", "Configurar"))
        self.actionGuardar_configuracion.setText(_translate("MainWindow", "Guardar configuracion"))
        self.actionPantalla_configuracion.setText(_translate("MainWindow", "Configurar pantalla"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
