from microbit import *

REFRESH = 100

def get_data():
    a, b, p = button_a.was_pressed(), button_b.was_pressed(), pin0.is_touched()
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    print(a, b, p, x, y, z)

def run():
 while True:
  sleep(REFRESH)
  get_data()

#display.show('M')
run()
