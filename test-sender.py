from ast import In
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, In)

while 1:
    sensor = GPIO.input(27)

    if sensor == 1:
        print("Kontakt")
        sleep(0.5)
    elif sensor == 0:
        print("Kein Konatk")
        sleep(0.5)
