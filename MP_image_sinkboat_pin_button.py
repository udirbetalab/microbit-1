from microbit import *

boat1 = Image("07070:06060:05050:99999:09990")
boat2 = Image("00000:07070:06060:05050:99999")
boat3 = Image("00000:00000:07070:06060:05050")
boat4 = Image("00000:00000:00000:07070:06060")
boat5 = Image("00000:00000:00000:00000:07070")
boat6 = Image("00000:00000:00000:00000:00000")

all_boats1 = [boat1, boat2, boat3, boat4, boat5, boat6]

while True:
    if button_a.is_pressed():
        display.show(boat1)
        sleep(1000)
        display.show(all_boats1, delay=200)
        sleep(2000)
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
    elif pin0.is_touched():
        display.show(Image.DUCK)
    elif pin1.is_touched():
        display.show(Image.HOUSE)
    elif pin2.is_touched():
        display.show(Image.SWORD)
    else:
        display.show(Image.SAD)