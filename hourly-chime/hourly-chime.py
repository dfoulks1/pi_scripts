#!/usr/bin/python3

import time
import sys

USE_GPIO = False
FORMAT24 = False


if FORMAT24:
    fmt = "%H"
else:
    fmt = "%I"


def winchester():
    tones = [["G#4", "E4", "F#4", "B3"], ["B3", "F#4", "G#4", "E4"]]
    for q in tones:
        for tone in q:
            if USE_GPIO:
                b.play(gpiozero.tones.Tone(tone))
                time.sleep(0.3)
                b.stop()
            else:
                print(tone)
        time.sleep(0.5)


def chime(r):
    chime_overrides = {
            4: [I, V],
            8: [I, I, X],
            9: [I, X],
            }
    chime_seq = []
   
    def set_chime(r):
        if r >= 10:
            chime_seq.append(X)
            r = r - 10
            set_chime(r)
        elif r >= 5:
            chime_seq.append(V)
            r = r - 5
            set_chime(r)
        elif r >= 1:
            chime_seq.append(I)
            r = r - 1
            set_chime(r)

    # Build the chime sequence if it's not defined
    if r in chime_overrides:
        chime_seq = chime_overrides[r]
    else:
        chime_seq = set_chime(r)

    # Set output
    if USE_GPIO:
        for tone in chime_seq:
            ring(tone)
    else:
        print(chime_seq)

def ring(note):
    b.play(note)
    time.sleep(0.25)
    b.stop()
    time.sleep(0.01)

def chime_listener():
    print("Starting hourly chime")
    while True:
        minute = int(time.strftime("%M", time.localtime()))
        second = int(time.strftime("%S", time.localtime()))
        hour = int(time.strftime(fmt, time.localtime()))
        if minute == 00 and second == 00:
            chime(hour)
            time.sleep(1)
        elif minute == 30 and second == 00:
            ring(HALF)
        else:
            time.sleep(1)

if __name__ == "__main__":
        if USE_GPIO:
            import gpiozero
            b = gpiozero.TonalBuzzer(17)
            I = gpiozero.tones.Tone("A4")
            V = gpiozero.tones.Tone("B4")
            X = gpiozero.tones.Tone("F#4")
            HALF = gpiozero.tones.Tone("A5")
        else:
            I = "I"
            V = "V"
            X = "X"

        chime_listener()
