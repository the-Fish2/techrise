# NASA Techrise Challenge Work
Nishka Kacheria

## Before Flight ##

### Hypothesis ###
Pollution is concentrated at lower altitudes, due to denser particles sinking. However, there is the possibility of environmental factors, such as thermal inversion, causing a different result. 

### Data ###
* Determining the percentage of air pollution
* Detailed quantification of air pollution resulting in improved targeting/ scoping of possible solutions
* Determination of the percentage of air pollution that is below cloud level contributing to getting recycled into the hydrologic cycle and thereby to water pollution. 
* Correlation between living at higher altitudes and prevalence of lung cancer and other similar health implications.
* Qualitative implication of air pollution. This can be used to raise awareness and rally efforts to address air pollution, similar to: endangered species photo archive, glacial melt photographs, library of lost sounds of animals.

### Fun Issues ###
* Working with computers
  * Video decoder issues
  * Memory issues - my computer can render videos stored on the hard disk drive, but not as reliably from an SD card
  * Writing Python programs, and subsequently, CircuitPy code that runs on the microprocessor
* Wiring up microprocessors and sensors
  * Including how MISO/MOSI ports and the I2C interface work
  * Handling multiple data streams with limited TX ports
  * Disassembling off the shelf products to extract individual components
  * Regulating circuits using pull-up resistors (more current is not always good!)
  * Soldering & heat shrink tubing
  * Wire stripping & tinning
  * Graduating from gobs of flux to clean connections
  * Painfully learning how not to burn myself again
  * Taking care of soldering implements
* 3-D printing
  * How to design 3-D models, accounting for printer limitations, supports and overhangs
  * 3-D printer issues such as print bed adhesion, extruder blockage, delamination
  * Sanding to make last minute adjustments to fit sharp 3-D printed corners in a rounded capsule
* Hardening for extreme pressures and temperatures
  * Most 3-D infill patterns can’t handle decreased atmospheric pressures
  * Epoxy works, tape residue melts
  * Popsicle sticks absorb humidity and skew readings

### Code ###
Clone the repository and save it to the metro, in addition to missing files. 
Certain files, ie TRSim Raven, require certain other physical parts (sent from NASA) to work.
The code itself works with a Dashcam (hacked), a SPS 30 particulate matter sensor, an SD Card breakout board, and a BME 680/688 AQI. 
Leave the .fseventsd and Trashes files on your Metro M4 Express, these are in addition. 
Lib files from Adafruit's documentation. 
The Dashcam does not have code, for formatting it to allow a 7 hr flight, format a 64GB card to Fat32 and it should work. 

### Specs ###
Weighs 527.3 g / 1.16 lb
Size: 40 x 40 x 80 inch / 101.6 x 101.6 x 203.2 cm box
5 V
0.27 A

Data Parameters collected:
* Vehicle_Time
* Vehicle_Altitude
* Temperature (C)
* Gas (ohms)
* Humidity (%)
* Pressure (hPa)
* 40um particles
* 10um particles
* pm10 standard
* pm100 standard
* pm25 standard
* 25um particles
* 100um particles
* particles 05um
* pm40 standard
* Image (color of sky)
