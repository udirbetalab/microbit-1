from microbit import *
import random

stein = Image("00000:"
              "09990:"
              "99999:"
              "09990:"
              "00000:")
saks = Image("99009:"
             "99090:"
             "00900:"
             "99090:"
             "99009:")
papir = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")

while True:
    if accelerometer.was_gesture("shake"):
        svar = random.randint(0, 2)
        if svar == 0:
            display.show(stein)
        elif svar == 1:
            display.show(saks)
        elif svar == 2:
            display.show(papir)
