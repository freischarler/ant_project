# ant_project

## REQUISITOS
### PASOS PARA EJECUTAR LA APLICACION:
sudo apt-get install python3-pyqt5
sudo apt-get install python3-rpi.gpio
cd Adafruit_Python_DHT  
sudo python3 setup.py install 

### HABILITAR I2C
sudo apt install python3-smbus
sudo raspi-config 
INTERFACE OPTIONS ---> SPI ---> yes


----------------------------------------------

#LIBRERIA ADAFRUIT
mkdir -p /home/pi/sources  
cd /home/pi/sources  
git clone https://github.com/adafruit/Adafruit_Python_DHT.git  
cd Adafruit_Python_DHT  
sudo python setup.py install 
