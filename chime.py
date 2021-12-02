#!/usr/bin/python3
import gpiozero
import time
import sys

FORMAT24 = False

if FORMAT24:
    fmt = "%H"
else:
    fmt = "%I"

button = gpiozero.Button(12)
b = gpiozero.TonalBuzzer(17)
X = gpiozero.tones.Tone("A5")
V = gpiozero.tones.Tone("B5")
I = gpiozero.tones.Tone("F#5")

def chime(r):
    print(r)
    if r > 10:
        ring(X)
        r = r - 10
        chime(r)

    elif 10 > r > 4:
        ring(V)
        r = r - 5
        chime(r)

    elif r > 0:
        ring(I)
        r = r - 1
        chime(r)

def ring(note):
    b.play(note)
    time.sleep(0.25)
    b.stop()
    time.sleep(0.01)

while True:
#    if button.is_active is True:
    minute = int(time.strftime("%M", time.localtime()))
    second = int(time.strftime("%S", time.localtime()))
    hour = int(time.strftime(fmt, time.localtime()))
    if minute == 19 and second == 00:
        chime(hour)
        time.sleep(1)
    else:
        print("%i:%i:%i" %(hour, minute, second))
        time.sleep(1)
