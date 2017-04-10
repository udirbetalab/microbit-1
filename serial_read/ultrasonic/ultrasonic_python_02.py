import serial
import time

ser = serial.Serial('/dev/cu.usbmodem1412', 115200)

#ser.flushInput()
#ser.flushOutput()

try:
  while True:
    data = ser.readline().rstrip()  
    data_s = data.split(":")
    x,y = data_s[0], data_s[1]
    print(x,y)


finally:
    ser.close()
