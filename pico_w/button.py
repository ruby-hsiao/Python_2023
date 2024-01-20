from machine import Pin
import time

led = Pin(15, Pin.OUT)
#button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button = Pin(14, Pin.PULL_DOWN)

while True:
    #print(button.value())
    #time.sleep_ms(500)
  
    if button.value():
        led.value(1)
    else:
        led.value(0)
'''
        led.toggle()
        time.sleep(0.5)
'''        