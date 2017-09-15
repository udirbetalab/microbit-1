from microbit import *


# Start calibrating
compass.calibrate()

# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)
    needle = compass.heading()
    if needle < 45:
        display.clear()
        display.set_pixel(2,0,9)
    elif needle < 135:
        display.clear()
        display.set_pixel(4,2,9)
    elif needle < 225:
        display.clear()
        display.set_pixel(2,4,9)
    elif needle < 315:
        display.clear()
        display.set_pixel(0,2,9)
