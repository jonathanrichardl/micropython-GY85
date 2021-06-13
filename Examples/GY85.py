from sys import exit
import utime
from machine import Pin,I2C
import math

class GY85:
    adxl345 = const(0x53)
    itg3200 = const(0x68)
    hmc5883l = const(30) 
    accDataRegister = const(0x32)
    gyroDataRegister = const(0x1b)
    magnetDataRegister = const(0x03)
    def __init__(self, scl, sda, i2cid = 0, acc = True, gyro = False, magnet = False):
        sdaPin = machine.Pin(sda)
        sclPin = machine.Pin(scl)
        self.gy85 = machine.I2C(i2cid,scl = sclPin, sda = sdaPin, freq = 100000) #configure frequency here
        ### SETUP
        ## ADXL 345
        if acc:
            self.gy85.writeto(GY85.adxl345, bytes([0x2d]),False) # Power Register of ADXL345, no Stop condition
            print(self.gy85.writeto(GY85.adxl345,bytes([0])),False)
            self.gy85.writeto(GY85.adxl345, bytes([0x2d]),False)
            self.gy85.writeto(GY85.adxl345,bytes([24]),False) # Set the Power Register to 0001 1000
            utime.sleep(0.1)
        ## ITG3200
        if gyro:
            self.gy85.writeto(GY85.itg3200, bytes([0x16]), False) # DLPF Register of HMC5883L, no Stop condition
            self.gy85.writeto(GY85.itg3200,bytes([26])) # Default Setting of DLPF Register : 0001 1010 
            utime.sleep(0.1)
        ## HMC5883L
        ## added error handling to avoid confusion because theres so many fake GY-85 distributed on the market which doesnt include the genuine HMC5883L
        ## (and has a different i2c address and registers) There shouldnt be any problem for ADXL345 and ITG3200 for the counterfeit boards.
        if magnet:  
            try:
                self.gy85.writeto(GY85.hmc5883l, bytes([0x00]),False)   #Configuration A Register of HMC5883l
                self.gy85.writeto(GY85.hmc5883l, bytes([0x10])) # Default Setting of Configutation A Register, 00010000
                utime.sleep(0.1)

                self.gy85.writeto(GY85.hmc5883l, bytes([0x01]), False) # Configuration B Register of HMC5883l
                self.gy85.writeto(GY85.hmc5833l, bytes([32])) # Default Setting of Configutation B Register, 00100000
                utime.sleep(0.1)
            
                self.gy85.writeto(GY85.hmc5883l, bytes([0x02]), False) # Mode Select Register of HMC5883l
                self.gy85.writeto(GY85.hmc5883l, bytes([0x00])) # Default Setting of Mode Select Register, 00000001
                utime.sleep(0.1)
            except:
                print("Fake GY-85 Detected, Invalid address for Magnetometer. Please buy a genuine one.")
    
    def readAcc(self):
        try:
            buff = self.gy85.readfrom_mem(GY85.adxl345,GY85.accDataRegister,6)
            x = (int(buff[1]) << 8) | buff[0]
            if x > 32767:
                x -= 65536
            y = (int(buff[3]) << 8) | buff[2]
            if y > 32767:
                y -= 65536
            z = (int(buff[5]) << 8) | buff[4]
            if z > 32767:
                z -= 65536
            return x *0.0039 ,y * 0.0039,z * 0.0039
        except:
            print("Acceleration Measurement is not enabled, make sure you enable first by adding acc = True")
    
    def calculateRPY(self):
        x,y,z = self.readAcc()
        roll = math.atan(y/z) * 57.3
        pitch = math.atan((- x) / math.sqrt(y * y + z * z)) * 57.3
        return roll,pitch
        
    def readGyro(self):
        buff = self.gy85.readfrom_mem(GY85.itg3200, GY85.gyroDataRegister,8)
        temp = (int(buff[0]) << 8) | buff[1]
        if temp>32767:
            temp-= 65536
        temp =35 + (temp + 13200)/280;
        x = (int(buff[2] << 8) | buff[3])
        if x>32767:
            x-= 65535
        y = (int(buff[4] << 8) | buff[5])
        if y>32767:
            y-= 65535
        z = (int(buff[6] << 8) | buff[7])
        if z>32767:
            z-= 65535
        return temp, x/14.375, y/14.375, z/14.375
    
    def readMagnet(self):
        try:
            buff = self.gy85.readfrom_mem(GY85.hmc5883l, GY85.magnetDataRegister,6)
            x = (int(buff[0]) << 8) | buff[1]
            if x > 32767:
                x -= 65536
            y = (int(buff[2]) << 8) | buff[3]
            if y > 32767:
                y -= 65536
            z = (int(buff[4]) << 8) | buff[5]
            if z > 32767:
                z -= 65536
            return x *0.92,y * 0.92,z * 0.92
        except:
            print("Magnet Measurement is not enabled, make sure you enable first by adding magnet = True OR get a genuine GY85 Board")
    
    def calculateHeading(self, x = None, y = None):
        if x is None | y is None:
            x,y = self.readMagnet()
        heading = math.atan(y/x)
        return heading
    
    def deinit(self):
        #self.gy85.deinit() ##uncomment for WiPy Boards 
        print("exiting")
        
