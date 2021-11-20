#!/usr/bin/python3
import gpiozero
import threading
import time
import random
import subprocess

# Red, Green, Blue, Yellow
LIGHTS = [5, 6, 13, 19]
NOTES = [ "E3", "A4", "E4", "C#4"]

simon = {
  "buzzer": gpiozero.TonalBuzzer(23),
  "blue": {
    "button": gpiozero.Button(26),
    "note": "E3",
    "light_pin": False,
    }
}

print(simon["blue"]["button"])
