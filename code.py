import time
import board
import busio
import sdcardio
import storage
from adafruit_sps30.i2c import SPS30_I2C
import adafruit_bme688

#do not rearrange code; SD card must come first
spi = board.SPI()
# if this doesn't work; spi = busio.SPI(board.SD_SCK, MOSI=board.SD_MOSI, MISO=board.SD_MISO)
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

i2c = board.I2C()
pmsensor = SPS30_I2C(i2c, 0x69)
aqsensor = adafruit_bme688.Adafruit_BME680_I2C(i2c, 0x77) #if this doesn't work try 0x76

aqsensor.sea_level_pressure = 1013
temperature_offset = -5 
#needs to be calibrated

while curr_events == RISING:
    
    pmsensor.wakeup();
    pmsensor.start();
    start = time.monotonic();  
    
    with open("/sd/readings.txt", "a") as f:
        #balloon
        f.write('ALTITUDE', '%.3f' % TRsim.altitude)
        
        #aqi
        temp = aqsensor.temperature();
        f.write('Temperature: {} degrees C'.format(temp))
        f.write('Gas: {} ohms'.format(aqsensor.gas))
        f.write('Humidity: {}%'.format(aqsensor.humidity))
        f.write('Pressure: {}hPa'.format(aqsensor.pressure))
        
        #cleaning the fan of the pm sensor - code found on https://github.com/kevinjwalters/Adafruit_CircuitPython_SPS30/blob/master/examples/sps30_test.py
        sps30_fp.clean(wait=4)
        for i in range(2 * (10 - 4 + 15)):
            cleaning = bool(sps30_fp.read_status_register() & sps30_fp.STATUS_FAN_CLEANING)
            print("c" if cleaning else ".", end="")
            if not cleaning:
                break
            time.sleep(0.5)
        
        #pm sensor
        #declare an array of values and then avg all of them basically
        if (temp > -10 and temp < 60):
            now = time.monotonic()
            time.sleep(30 - (now - start))
            
            results = pmsensor.read()
            for i in range 15: 
                results2 = pmsensor.read()
                for i in range results.len:
                    results[i] += results2[i]
                time.sleep(1)
            
            for x in results:
                x = x/15;
                f.write(x + " ");
        
    pmsensor.stop();
    pmsensor.sleep();
    
    time.sleep(20)
    
#results should have values: 'particles 40um', 'particles 10um', 'pm10 standard', 'pm100 standard', 'pm25 standard', 'particles 25um', 'particles 100um', 'particles 05um', 'tps', 'pm40 standard'
#note that pm100 standard and pm40 standard ARE GUESSES BASED ON SURROUNDINGS, only exact data is 25 and 10
# other sensors running
#remember - indentation necessary in python (ew)
