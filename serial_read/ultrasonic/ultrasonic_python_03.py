import serial
import time
var = 0

ser = serial.Serial('/dev/cu.usbmodem1412', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()

try:
  while True:
    data = ser.readline().rstrip()  
    data_s = data.split(":")
    x,y = data_s[0], data_s[1]
    y = int(y)
    if 20 <= y <= 40:
        print("Alert number: " + str(int(var)))
        print("Distance: " + str(int(y)) + "cm")
        print(" ")
 
        var = var + 1
    elif y < 10:
      print("Too close!")
      
finally:
    ser.close()
  
