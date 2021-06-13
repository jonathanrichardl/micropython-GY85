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
        

