#!/usr/bin/python3

import gpiozero
import time
import threading
import sys

# Must be between 0-1!
motor_speed = 1

m1c = gpiozero.LED(21)
m1 = gpiozero.Motor(20, 16)

m2c = gpiozero.LED(13)
m2 = gpiozero.Motor(26, 19)

m1_open = gpiozero.Button(12)
m1_close = gpiozero.Button(7)

m2_open = gpiozero.Button(6)
m2_close = gpiozero.Button(5)

def pressed(channel):
    global m2, m1, m1c, m2c
    if channel is m1_open:
       m1.forward(speed=motor_speed)
       m1c.on()
       time.sleep(5)
       m1c.off()
    if channel is m1_close:
       m1.reverse(speed=motor_speed)
       m1c.on()
       time.sleep(5)
       m1c.off()
    if channel is m2_open:
       m2.forward(speed=motor_speed)
       m2c.on()
       time.sleep(5)
       m2c.off()
    if channel is m2_close:
       m2.reverse(speed=motor_speed)
       m2c.on()
       time.sleep(5)
       m2c.off()

def wait_for_signal():
    while True:
        time.sleep(0.1)

def curtain():
    while True:
       wait_for_signal()

def init():
    m1_open.when_pressed = pressed
    m2_open.when_pressed = pressed
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
