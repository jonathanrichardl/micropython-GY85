Written By Jonathan Richard
Department Of Electrical Engineering, UI 
# micropython-GY85
Complete library for GY-85 compatible with all micropython board. Supports reading from ADXl345, HMC5883L, and ITG3200 in the GY85 board or its own standalone board. Examples are tested in Raspberry Pi Pico.
# Features
1. Selectable modes from Acceleration reading only, Gyroscope and Temperature reading only, Magnetometer reading only, or configurable multiple reading modes. 
2. Standard Micropython syntax, no special library used. 
3. Feature to detect counterfeit GY-85. 

# Usage 
## Acceleration only mode
```
from GY85 import GY85
sclPin = 1 # change the pins to your desired ones
sdaPin = 0 
i2cid = 0 
acc = GY85(scl = sclPin, sda = sdaPin, i2cid = i2cid) # default mode / accelerometer only, magnetometer and gyroscope configuration skipped
buffer = acc.readAcc()
print("Acceleration Value x = " + str(buffer[0])+", y = " + str(buffer[1])+", z = " + str(buffer[2]))
buffer = acc.calculateRP()
print("Roll Value = " + str(buffer[0])+", Pitch Value = " + str(buffer[1]))
utime.sleep(1)
```
Output: 
```
Acceleration Value x = 0.0351, y = 0.0195, z = -1.0764
Roll Value = -1.037929, Pitch Value = -1.867509
```
## Magnet only mode 
        


