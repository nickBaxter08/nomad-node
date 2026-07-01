from machine import Pin
from time import sleep


led = Pin("LED", Pin.OUT)


def led_on():
    led.value(1)


def led_off():
    led.value(0)


def blink(times, delay=0.5):
    for i in range(times):
        led_on()
        sleep(delay)

        led_off()
        sleep(delay)