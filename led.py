import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def on():
    GPIO.output(4, True)
def off():
    GPIO.output(4, False)