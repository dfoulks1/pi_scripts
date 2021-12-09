#!/usr/bin/python3
import gpiozero
import colorzero
import time
import sys
import threading

status_led = gpiozero.RGBLED(13, 19, 26)
is_open = False
open_btn = gpiozero.Button(21)
close_btn = gpiozero.Button(20)

def pressed(channel):
    global is_open
    if channel is open_btn:
        if not is_open:
            print("Opening the curtains")
            status_led.color = colorzero.Color("red")
            time.sleep(1)
            status_led.off()
            is_open = True
        else:
            print("Curtains are already open..")
    elif channel is close_btn:
        if is_open:
            print("Closing the curtains")
            status_led.color = colorzero.Color("red")
            time.sleep(1)
            status_led.off()
            is_open = False
        else:
            print("Curtains are already closed..")
    
def wait_for_signal():
    while True:
        time.sleep(0.1)

def curtain():
    while True:
       wait_for_signal()

def init():
    open_btn.when_pressed = pressed
    close_btn.when_pressed = pressed
    time.sleep(0.1)

def start():
    t = threading.Thread(target=curtain)
    t.daemon = True
    t.start()
    t.join()

def main():
    print("starting curtain controller")
    try:
        init()
        start()
    except:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
