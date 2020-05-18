from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap

from picamera import PiCamera
import time
from time import sleep
import datetime 

class Ui_Dialog(object):
    tiempo_finalizacion=0
    duracion_grabacion=0
    cantidad_videos=0

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
        self.check_fullscreen.setChecked(False)        
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
        self.cbox_size.addItem("1")
        self.cbox_size.addItem("2")
        self.cbox_size.addItem("3")
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

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
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
	
    def grabar_datos(self):
        archivo = open("grabacion.txt",'w')
        archivo.write(str(self.duracion_grabacion)+"\n")
        archivo.write(str(self.cantidad_videos))
        archivo.close()
        
	#-----------------------------
	#	PESTANIA de TIEMPO
	#   Permite configurar el inicio,fin y resolucion del video
	#-----------------------------
	
    def actualizar(self):
        f_inicio=self.le_inicio.text()
        self.duracion_grabacion=self.le_duracion.value()
        self.cantidad_videos=self.le_cantidad.value()
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

	#-----------------------------
	#	PESTANIA de PREVIEW_VIDEO
	#   Permite acomodar el video en la pantalla o fullscreen
	#-----------------------------

    def preview_video(self):
        camera=PiCamera()
        camera.resolution = (640,480)
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
            archivo.write("no"+"\n"+wx+"\n"+wy)
            archivo.close()   
            camera.start_preview(fullscreen=False, window=(int(txt),int(txt2),int(640/resize),int(480/resize)))
        time.sleep(3)
        camera.stop_preview()
        camera.close()


    def fullscreen(self):
        if (self.check_fullscreen.isChecked()):
            self.le_wx.setEnabled(False)
            self.le_wy.setEnabled(False)
            self.cbox_size.setEnabled(False)        
        else:
            self.le_wx.setEnabled(True)
            self.le_wy.setEnabled(True)
            self.cbox_size.setEnabled(True) 

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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
