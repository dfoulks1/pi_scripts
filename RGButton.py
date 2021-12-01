#!/usr/bin/python3
import gpiozero
import colorzero
import time
import sys
import threading

led = gpiozero.RGBLED(13, 19, 26)
last_color = None

r_btn = gpiozero.Button(21)
g_btn = gpiozero.Button(20)
b_btn = gpiozero.Button(16)
stop_btn = gpiozero.Button(12)

def pressed(channel):
    global last_color, state
    if channel is r_btn:
        last_color = "red"
        led.color = colorzero.Color("red")
    if channel is g_btn:
        last_color = "green"
        led.color = colorzero.Color("green")
    if channel is b_btn:
        last_color = "blue"
        led.color = colorzero.Color("blue")
    if channel is stop_btn:
        if led.is_active:
            led.off()
        else:
            led.color = colorzero.Color(last_color)
        
def wait_for_signal():
    while True:
        time.sleep(0.1)

def rgbutton():
    while True:
       wait_for_signal()

def init():
    r_btn.when_pressed = pressed
    g_btn.when_pressed = pressed
    b_btn.when_pressed = pressed
    stop_btn.when_pressed = pressed
    time.sleep(1)

def start_rgbutton():
    t = threading.Thread(target=rgbutton)
    t.daemon = True
    t.start()
    t.join()

def main():
    print("starting rgbutton")
    try:
        init()
        start_rgbutton()
    except:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
