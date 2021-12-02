#!/usr/bin/python3
import gpiozero
import time
import sys
button = gpiozero.Button(12)
b = gpiozero.TonalBuzzer(17)
tone = gpiozero.tones.Tone
def pachabel():
    b.play(tone("D5"))
    time.sleep(1)
    b.stop()

    b.play(tone("A4"))
    time.sleep(1)
    b.stop()

    b.play(tone("B4"))
    time.sleep(1)
    b.stop()

    b.play(tone("F#4"))
    time.sleep(1)
    b.stop()

    b.play(tone("G4"))
    time.sleep(1)
    b.stop()

    b.play(tone("D4"))
    time.sleep(1)
    b.stop()

    b.play(tone("G4"))
    time.sleep(1)
    b.stop()

    b.play(tone("A4"))
    time.sleep(1)
    b.stop()

while True:
    if button.is_active is True:
        pachabel()
