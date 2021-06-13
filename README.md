Written By Jonathan Richard

Department Of Electrical Engineering, UI 
# micropython-GY85
Complete library for GY-85 compatible with all micropython board. Supports reading from ADXl345, HMC5883L, and ITG3200 in the GY85 board or its own standalone board. Examples are tested in Raspberry Pi Pico.
# Features
1. Selectable modes from Acceleration reading only, Gyroscope and Temperature reading only, Magnetometer reading only, or configurable multiple reading modes. 
2. Standard Micropython syntax, no special library used. 
3. Feature to detect counterfeit GY-85. 

# Usage 
```
from GY85 import GY85
import machine
import utime
sclPin = 1
sdaPin = 0
i2cid = 0
gy85 = GY85(scl = sclPin, sda = sdaPin, i2cid = i2cid, magnet = True, gyro = True) # enable all measurements
try:
    while True:
        buffer = gy85.readAcc()
        print("Acceleration Value x = " + str(buffer[0])+", y = " + str(buffer[1])+", z = " + str(buffer[2]))
        buffer = gy85.calculateRP()
        print("Roll Value = " + str(buffer[0])+", Pitch Value = " + str(buffer[1]))
        buffer = gy85.readGyro()
        print("Temperature : " + str(buffer[0]))
        print("Gyroscope Value x = " + str(buffer[1])+", y = " + str(buffer[2])+", z = " + str(buffer[3]))
        try:
            buffer = gy85.readMagnet()
            print("Magnet Value x = " + str(buffer[0])+", y = " + str(buffer[1])+", z = " + str(buffer[2]))
        except:
            pass
        utime.sleep(1)
except KeyboardInterrupt:
    acc.deinit()
        

```
Output: 
```
Magnet Value x = 0.xxxx, y = 0.xxxx, z = -1.xxxx
Acceleration Value x = 0.0234, y = 0.0468, z = -1.0764
Roll Value = -2.489737, Pitch Value = -1.244281
Temperature : 34.73214
```
## Magnet only mode 
        


