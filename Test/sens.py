import Adafruit_DHT
from time import sleep

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11

temp_gpio=17
print("BANDERA 1")
while True:
        temp, hum = Adafruit_DHT.read_retry(sensor, temp_gpio)
        print("BANDERA 2")
        print(temp)
        sleep(3)