# Refer: https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html
from gpiozero import Button

proxy = Button(4)

if proxy.is_pressed:
    print("button is pressed")