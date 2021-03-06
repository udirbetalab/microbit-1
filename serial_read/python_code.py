import serial

#the port will depend on your computer
#for a raspberry pi it will probably be /dev/ttyACM0
#PORT = "/dev/ttyACM0"
#for windows it will be COM(something)
PORT = "/dev/tty.usbmodem40132"

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        #read a line from the microbit, decode it and
        # strip the whitespace at the end
        data = s.readline().rstrip()

        #split the accelerometer data into x, y, z
        data_s = data.split(" ")
        a, b, p = data_s[0], data_s[1], data_s[2]
        x, y, z = data_s[3], data_s[4], data_s[5]
#        twitter = data_s[0]

        print(a,b,p,x,y,z)
#        print(data_s[0])

 
finally:
    s.close()
