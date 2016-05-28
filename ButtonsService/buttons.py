#!/usr/bin/python

# Original idea from http://forum.kodi.tv/showthread.php?tid=260817

import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')

import RPi.GPIO as GPIO
import xbmc

# Decorator for some sugar
callbacks = []

def listen(pin):
    def decorator(func):
        callbacks.append({ "func": func, "pin": pin })
    
    return decorator

# Pin listeners
@listen(12)
def next_callback(channel):
    xbmc.executebuiltin("PlayerControl(Next)")

@listen(16)
def playPause_callback(channel):
    xbmc.executebuiltin("Action(PlayPause)")

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for c in callbacks:
        GPIO.setup(c["pin"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(c["pin"], GPIO.FALLING, callback=c["func"], bouncetime=300)

    while not xbmc.abortRequested:
        xbmc.sleep(5)

    # Clean up
    pins = [x["pin"] for x in callbacks]
    for pin in pins:
        GPIO.remove_event_detect(pin)

    GPIO.cleanup(pins)
