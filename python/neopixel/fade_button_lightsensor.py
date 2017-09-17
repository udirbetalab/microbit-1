from microbit import *
import neopixel
from random import randint

npix = neopixel.NeoPixel(pin0, 15)
np = neopixel.NeoPixel(pin0, 15)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
yellow = (255,255,0)

def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()
    return
    
def Fade():
   for i in range(0,255,5):
       LightAll((i,0,0))
       sleep(20)
   for i in range(255,-1,-5):
       LightAll((i,0,0))
       sleep(20)
       
def Run(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
        npix[pix-1] = (0, 0, 0)
        npix.show()
        sleep(100)

def Runcol():
    Run(blue)
    Run(green)

def Runcol2():
#    Run(red)
    Run(yellow)
    Run(purple)

def Randomcol():
    for j in range(0,4):
        for pixel_id in range(0, len(np)):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)
            np[pixel_id] = (red, green, blue)
            np.show()
            sleep(50)

while True:
    lightSensor = pin2.read_analog()
    print(lightSensor)
    if lightSensor < 512:
        Runcol2()
    if lightSensor > 512:
        Runcol()
    if button_a.was_pressed():
        Fade()
    if pin1.is_touched():
        Randomcol()
 #   else:
 #       Runcol()
