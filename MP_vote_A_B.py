from microbit import *

votea = 0
voteb = 0
startup = 0

while True:
    if startup == 0:
        display.scroll("Vote A or B")
        startup = 1
        display.clear()
    else:
        if button_a.is_pressed():
            votea = votea + 1
            display.show(str(votea))
            sleep(500)
            display.clear()
        elif button_b.is_pressed():
            voteb = voteb + 1
            display.show(str(voteb))
            sleep(500)
            display.clear()
        elif accelerometer.was_gesture("shake"):
            display.scroll("A:" + str(votea) + " B:" + str(voteb) + " ")
            display.clear()