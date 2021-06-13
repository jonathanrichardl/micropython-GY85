from GY85 import GY85
import machine
import utime
sclPin = 1
sdaPin = 0
i2cid = 0

acc = GY85(scl = sclPin, sda = sdaPin, i2cid = i2cid) # default mode / accelerometer only, magnetometer and gyroscope configuration skipped
try:
    while True:
        buffer = acc.readAcc()
        print("Acceleration Value x = " + str(buffer[0])+", y = " + str(buffer[1])+", z = " + str(buffer[2]))
        buffer = acc.calculateRP()
        print("Roll Value = " + str(buffer[0])+", Pitch Value = " + str(buffer[1]))
        utime.sleep(1)
except KeyboardInterrupt:
    acc.deinit()
        
