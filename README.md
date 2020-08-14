# Ant Project

## REQUISITOS
### PASOS PARA EJECUTAR LA APLICACION
```
sudo apt-get install python3-pyqt5
sudo apt-get install python3-rpi.gpio
sudo apt install python3-smbus
cd Adafruit_Python_DHT  
sudo python3 setup.py install 
```

### HABILITAR I2C
```
sudo raspi-config 
INTERFACE OPTIONS ---> SPI ---> yes
```


----------------------------------------------

## REQUISITOS PARA DESARROLLAR
### LIBRERIA ADAFRUIT
```
mkdir -p /home/pi/sources  
cd /home/pi/sources  
git clone https://github.com/adafruit/Adafruit_Python_DHT.git  
cd Adafruit_Python_DHT  
sudo python setup.py install 
```
