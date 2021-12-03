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
X = gpiozero.tones.Tone("A4")
V = gpiozero.tones.Tone("B4")
I = gpiozero.tones.Tone("F#4")

def winchester():
    q1_tones = ["G#4", "E4", "F#4", "B3"]
    q2_tones = ["B3", "F#4", "G#4", "E4"]
    for tone in q1_tones:
        b.play(gpiozero.tones.Tone(tone))
        time.sleep(0.3)
        b.stop()
    time.sleep(0.5)
    for tone in q2_tones:
        b.play(gpiozero.tones.Tone(tone))
        time.sleep(0.3)
        b.stop()


def chime(r):
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
    if button.is_active is True:
        winchester()
    minute = int(time.strftime("%M", time.localtime()))
    second = int(time.strftime("%S", time.localtime()))
    hour = int(time.strftime(fmt, time.localtime()))
    if minute == 00 and second == 00:
        chime(hour)
        time.sleep(1)
    elif minute == 30 and second == 00:
        chime(1)
    else:
        time.sleep(1)
