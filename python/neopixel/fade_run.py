from microbit import *
import neopixel

npix = neopixel.NeoPixel(pin0, 15)

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
       
while True:
    Fade()
    Run(blue)
    Run(green)
    Run(red)
    Run(yellow)
    Run(purple)
