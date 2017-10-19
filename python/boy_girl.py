# 10 most popular boy and girl name in Norway 2016 picker - gutt=boy and jente=girl

from microbit import *
import random

gutt = """William,Oskar,Lucas,Mathias,Filip,Oliver,Jakob,Emil,Noah,Aksel"""
jente = """Nora,Emma,Sara,Sofie,Sofia,Maja,Olivia,Ella,Ingrid,Emilie"""
            
gutt_split = gutt.split(",", )
jente_split = jente.split(",", )

while True:
    if button_a.is_pressed():
        display.scroll(random.choice(gutt_split))
    if button_b.is_pressed():
        display.scroll(random.choice(jente_split))
    if pin0.is_touched():
         display.scroll(random.choice(gutt_split + jente_split))
    else:
        display.show(Image.HEART)
