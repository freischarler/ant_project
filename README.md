# ant_project
# main.py 60% - INTERFAZ GRAFICA PRINCIPAL
# s.py: 90% - CONFIGURACION DE LA INTERFASE PARA MANEJAR LA VENTANA Y REALIZAR CROP

#instalar:
sudo apt-get install python3-rpi.gpio


mkdir -p /home/pi/sources  
cd /home/pi/sources  
git clone https://github.com/adafruit/Adafruit_Python_DHT.git  
cd Adafruit_Python_DHT  
sudo python setup.py install 

#para i2C
sudo apt install python3-smbus