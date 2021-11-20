import gpiozero
import threading
import time
import random
import os
from subprocess import call

# green, red, blue, yellow
LIGHTS = [33, 37, 35, 31]
BUTTONS = [11, 15, 13, 7]
NOTES = ["E3", "A4", "E4", "Cs4"]

def led_on(led):
    led.on()

def led_off(led):
    led.off()
    
simon = {
    "blue": {
        "button": gpiozero.Button(12),
        "led": gpiozero.LED(6)
        },
    "red": {
        "button": gpiozero.Button(16),
        "led": gpiozero.LED(13)
        },
    "green": {
        "button": gpiozero.Button(20),
        "led": gpiozero.LED(19)
        },
    "yellow": {
        "button": gpiozero.Button(21),
        "led": gpiozero.LED(26)
        },
    }

simon["blue"]["button"].when_pressed = led_on(simon["blue"]["led"])
simon["blue"]["button"].when_released = led_off(simon["blue"]["led"])
        