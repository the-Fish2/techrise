import time
import board
#the above should have already been imported. 
from adafruit_sps30.i2c import SPS30_I2C
import adafruit_bme688

i2c = board.I2C()
pmsensor = SPS30_I2C(i2c, 0x69)
aqsensor = adafruit_bme680.Adafruit_BME680_I2C(i2c, 0x77)

while curr_events == RISING:
    #pmsensor
    results = pmsensor.read()
    print(results)
    print("PM2.5: {:d}".format(results["pm25 standard"]))
   
    #aqi sensor
    print('Temperature: {} degrees C'.format(sensor.temperature))
    print('Gas: {} ohms'.format(sensor.gas))
    print('Humidity: {}%'.format(sensor.humidity))
    print('Pressure: {}hPa'.format(sensor.pressure))
    
    time.sleep(20)
    
#results should have values: 'particles 40um', 'particles 10um', 'pm10 standard', 'pm100 standard', 'pm25 standard', 'particles 25um', 'particles 100um', 'particles 05um', 'tps', 'pm40 standard'
# other sensors running
#remember - indentation necessary in python (ew)
