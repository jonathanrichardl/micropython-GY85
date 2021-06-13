from GY85 import GY85
import machine
import utime
sclPin = 1
sdaPin = 0
i2cid = 0
gyro = GY85(scl = sclPin, sda = sdaPin, i2cid = i2cid, acc = False, gyro = True) # Gyro only mode, magnetometer and accelerometer configuration skipped
try:
    while True:
        buffer = gyro.readGyro()
        print("Temperature : " + str(buffer[0]))
        print("Gyroscope Value x = " + str(buffer[1])+", y = " + str(buffer[2])+", z = " + str(buffer[3]))
        utime.sleep(1)
except KeyboardInterrupt:
    acc.deinit()
        

