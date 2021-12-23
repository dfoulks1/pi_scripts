#!/usr/bin/python3

import gpiozero
import time
import threading
import sys

# Must be between 0-1!
motor_speed = 1
motor_duration = 2

m1c = gpiozero.LED(16)
m1 = gpiozero.Motor(20, 21)

m2c = gpiozero.LED(13)
m2 = gpiozero.Motor(26, 19)

m1_open = gpiozero.Button(12)
m1_close = gpiozero.Button(7)

m2_open = gpiozero.Button(6)
m2_close = gpiozero.Button(5)

m1_isOpen = False
m2_isOpen = False

def pressed(channel):
    global m2, m1, m1c, m2c, m2_isOpen, m1_isOpen
    if channel is m1_open:
        if not m1_isOpen:
            print("Opening Curtains...")
            m1.forward(speed=motor_speed)
            m1c.on()
            time.sleep(motor_duration)
            m1c.off()
            m1_isOpen = True
        else:
            print("Curtains are already open!")

    if channel is m1_close:
        if m1_isOpen:
            print("Closing Curtains...")
            m1.backward(speed=motor_speed)
            m1c.on()
            time.sleep(motor_duration)
            m1c.off()
            m1_isOpen = False
        else:
            print("Curtains are already closed!")

    if channel is m2_open:
        if not m2_isOpen:
            print("Opening Shades...")
            m2.forward(speed=motor_speed)
            m2c.on()
            time.sleep(motor_duration)
            m2c.off()
            m2_isOpen = True

        else:
            print("Shades are already open!")
    if channel is m2_close:
        if m2_isOpen:
            print("Closing Shades...")
            m2.backward(speed=motor_speed)
            m2c.on()
            time.sleep(motor_duration)
            m2c.off()
            m2_isOpen = False
        else:
            print("Shades are already closed!")

def wait_for_signal():
    while True:
        time.sleep(0.1)

def curtain():
    while True:
       wait_for_signal()

def init():
    m1_open.when_pressed = pressed
    m1_close.when_pressed = pressed
    m2_open.when_pressed = pressed
    m2_close.when_pressed = pressed
    time.sleep(0.1)

def start_curtain():
    t = threading.Thread(target=curtain)
    t.daemon = True
    t.start()
    t.join()

def main():
    print("starting curtain")
    try:
        init()
        start_curtain()
    except:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
