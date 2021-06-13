from GY85 import GY85
import machine
import utime
sclPin = 1
sdaPin = 0
i2cid = 0
magnet = GY85(scl = sclPin, sda = sdaPin, i2cid = i2cid, acc = False, magnet = True) # Magnetometer only mode, magnetometer and accelerometer configuration skipped
try:
    while True:
        try:
            buffer = magnet.readMagnet()
            print("Magnet Value x = " + str(buffer[0])+", y = " + str(buffer[1])+", z = " + str(buffer[2]))
            utime.sleep(1)
        except:
            utime.sleep(10)
            pass
except KeyboardInterrupt:
    magnet.deinit()
        


