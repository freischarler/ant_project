import Adafruit_DHT
from time import sleep
import smbus #para i2c

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT22

temp_gpio=20
uv_gpio=0

bus = smbus.SMBus(1)
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
    return convertToNumber(data)


# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x20

print("BANDERA 1")
while True:
        s_Luz=str(format(readLight(),'.2f'))
        s_Humedad, s_Temperatura = Adafruit_DHT.read_retry(sensor, temp_gpio)
        s_Temperatura=format(s_Temperatura, '.2f')
        s_Humedad=format(s_Humedad, '.2f')
                
        print("BANDERA 2")
        print(s_Humedad)
        print(s_Temperatura)
        print(s_Luz)
        sleep(5)
