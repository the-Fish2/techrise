import trsim_raven
import board
import busio
import sdcardio
import storage
import time
import adafruit_vc0706
import adafruit_bme680
from adafruit_sps30.i2c import SPS30_I2C

i2c = board.I2C()
pmsensor = SPS30_I2C(i2c, 0x69)
aqsensor = adafruit_bme680.Adafruit_BME680_I2C(i2c, 0x77)

spi = board.SPI()
cs = board.D7
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/temps.txt", "w") as f:
    f.write("Altitude, Temperature (C), Gas (ohms), Humidity (%), Pressure (hPa), 40um particles, 10um particles, pm10 standard, pm100 standard, pm25 standard, 25um particles, 100um particles, particles 05um, tps, pm40 standard")
    f.write("\n")
    f.close()

# uart = busio.UART(board.TX, board.RX, baudrate=38400)
# vc0706 = adafruit_vc0706.VC0706(uart)
# vc0706.image_size = adafruit_vc0706.IMAGE_SIZE_320x240

TRsim = trsim_raven.Simulator(pbf_pin=board.D2, go_pin=board.D3)

LAND = 0
RISING = 1
FLOATING = 2
DESCENDING = 3
curr_events = LAND
prev_events = curr_events

num_packets = 0

RISE_TH = -2
FLOAT_TH = 4
DSCND_TH = 5

asleep = False

while True:
    TRsim.update()
    if (TRsim.streaming):
        if TRsim.new_data:
            num_packets += 1
            data=TRsim.data

            curr_vd = TRsim.velocity_down

            if curr_vd < RISE_TH:
                curr_events = RISING
            elif curr_vd >= RISE_TH and curr_vd < DSCND_TH and curr_events != LAND:
                curr_events = FLOATING
            elif curr_vd >= DSCND_TH:
                curr_events = DESCENDING
            else:
                curr_events = LAND

            if curr_events != prev_events:
                prev_events = curr_events


            if (num_packets % 500 == 1):
                altitude = TRsim.altitude
                if curr_events == RISING:
#                     print("taking pic!")
#                     vc0706.take_picture()
#                     frame_length = vc0706.frame_length
#                     print(frame_length)


#                     s = "/sd/image" + str(altitude) + ".jpg"

#                     with open(s, "wb") as f:
#                         wcount = 0
#                         while frame_length > 0:
#                             to_read = min(frame_length, 32)
#                             copy_buffer = bytearray(to_read)
#                             if (vc0706.read_picture_into(copy_buffer) == 0):
#                                 raise RuntimeError("oof l+ratio")
#                             f.write(copy_buffer)
#                             frame_length -= 32
#                             wcount += 1
#                             if (wcount >= 64):
#                                 print(".", end=" ")
#                                 wcount = 0

#                         f.close()
                    if (aqsensor.temperature < -30):
                        asleep = True
                        pmsensor.stop();
                        pmsensor.sleep();
                    else:
                        pmsensor.wakeup();
                        pmsensor.start();
                        asleep = False

                    with open("/sd/temps.txt", "a") as f:
                        f.write(str(altitude) + ", ")
                        print(altitude)
                        f.write("{}, {}, {}, {}, ".format(aqsensor.temperature, aqsensor.gas, aqsensor.humidity, aqsensor.pressure))
                        if (not asleep):
                            results = pmsensor.read()
                            for key in results:
                                f.write(str(results[key]) + ", ")
                        f.write("\n")
                        f.close()
                        
# altitude = 0
# with open("/sd/temps.txt", "a") as f:
#     f.write(str(altitude))
#     results = pmsensor.read()
#     f.write('Temperature: {} degrees C'.format(aqsensor.temperature))
#     f.write('Gas: {} ohms'.format(aqsensor.gas))
#     f.write('Humidity: {}%'.format(aqsensor.humidity))
#     f.write('Pressure: {}hPa'.format(aqsensor.pressure))
#     f.write('\n')
#     results = pmsensor.read()
#     for key in results:
#         f.write(str(key) + " " + str(results[key]) + "\n")

#     f.close()

