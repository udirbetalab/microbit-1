from microbit import *
import random

gutt = """William,Oskar,Lucas,Mathias,Filip,Oliver,Jakob,Emil,Noah,Aksel"""
jente = """Nora,Emma,Sara,Sofie,Sofia,Maja,Olivia,Ella,Ingrid,Emilie"""
dyr = """Kanin,Hund,Katt,Rotte,Fisk,Hest,Sau,Ku"""
            
gutt_split = gutt.split(",")
jente_split = jente.split(",")
dyr_split = dyr.split(",")

while True:
    if button_a.is_pressed():
        display.scroll(random.choice(gutt_split))
    if button_b.is_pressed():
        display.scroll(random.choice(jente_split))
    if pin0.is_touched():
        display.scroll(random.choice(gutt_split + jente_split))
    if pin1.is_touched():
        display.scroll(random.choice(dyr_split))
    if pin2.is_touched():
        display.scroll(random.choice(gutt_split + jente_split) + " : " + random.choice(dyr_split))
    else:
        display.show(Image.HEART)
