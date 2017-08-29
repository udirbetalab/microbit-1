from microbit import *
import random

stein = Image("00000:"
              "09990:"
              "99999:"
              "09990:"
              "00000")

saks = Image("99009:"
             "99090:"
             "00900:"
             "99090:"
             "99009")

papir = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")

stein_saks_papir = [stein, saks, papir]

while True:
    if accelerometer.is_gesture("shake"):
        display.show(random.choice(stein_saks_papir))
    if button_a.was_pressed():
        display.show(random.choice(stein_saks_papir))
    if button_b.is_pressed():
        display.show(random.choice(stein_saks_papir))
