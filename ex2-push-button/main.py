from machine import Pin
import time

button=Pin(2,Pin.IN)
led=Pin(16,Pin.OUT)
state=0

while True:
    time.sleep(0.5)
    led.value(state)
    state=button.value()