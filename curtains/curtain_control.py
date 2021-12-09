#!/usr/bin/python3
import gpiozero
import colorzero
import time
import sys
import threading

status_led = gpiozero.LED(13)
is_open = False
open_btn = gpiozero.Button(26)
close_btn = gpiozero.Button(19)
f_switch_1 = gpiozero.LED(20)
f_switch_2 = gpiozero.LED(21)
c_switch_1 = gpiozero.LED(16)
c_switch_2 = gpiozero.LED(12)

def pressed(channel):
    global is_open
    if channel is open_btn:
        if not is_open:
            open()
        else:
            print("Curtains are already open..")
    elif channel is close_btn:
        if is_open:
            close()
        else:
            print("Curtains are already closed..")

def close():
    global status_led, is_open
    print("Closing the curtains")
    status_led.on()
    c_switch_1.on()
    c_switch_2.on()
    time.sleep(1)
    c_switch_1.off()
    c_switch_2.off()
    status_led.off()
    is_open = False

def open():
    global status_led, is_open
    print("Opening the curtains")
    status_led.on()
    f_switch_1.on()
    f_switch_2.on()
    time.sleep(1)
    f_switch_1.off()
    f_switch_2.off()
    status_led.off()
    is_open = True

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
