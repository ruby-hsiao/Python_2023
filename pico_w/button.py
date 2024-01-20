from machine import Pin
import time

led = Pin(15, Pin.OUT)
#button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button = Pin(14, Pin.PULL_DOWN)
is_press = False
led_status = False

def btn_detect(btn):
    global is_press, led_status
    if btn.value():
        #發生彈跳的解法
        time.sleep_ms(50)
        if btn.value():
            is_press = True
    elif is_press:
        time.sleep_ms(50)
        if btn.value() == False:
            print('release')
            led_status = not led_status
            print(f'led_status={led_status}')
            led.value(led_status)
            is_press = False
            
while True:
    btn_detect(button)