import machine
import time

led2= machine.Pin(27,machine.Pin.OUT)
led1 = machine.Pin(14, machine.Pin.OUT)

while True: 
    led2.value(1)
    time.sleep(0.5)
    led2.value(0)
    time.sleep(0.5)
    led1.value(1)
    time.sleep(0.9)
    led1.value(0)
    time.sleep(0.9)
