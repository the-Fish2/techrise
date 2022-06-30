import time
import board
#the above should have already been imported. 
from adafruit_sps30.i2c import SPS30_I2C

# printing should work first
i2c = board.I2C()
sps = SPS30_I2C(i2c)

while curr_events == RISING:
    results = sps.read()
    print(results)
    print("PM2.5: {:d}".format(results["pm25 standard"]))
    time.sleep(20)
#aqdata should have values: 'particles 40um', 'particles 10um', 'pm10 standard', 'pm100 standard', 'pm25 standard', 'particles 25um', 'particles 100um', 'particles 05um', 'tps', 'pm40 standard'
# other sensors running
#remember - indentation necessary in python (ew)
