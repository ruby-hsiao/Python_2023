from machine import Pin
import time

led = Pin(15, Pin.OUT)
#button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
is_press = False
led_status = False

while True:
    #print(button.value())
    #time.sleep_ms(500)
  
    #if button.value():
    #    led.value(1)
    #else:
    #    led.value(0)
    
    #解決彈跳電容的錢
    #switch button
    if button.value():
        is_press = True
    elif is_press:
        print('release')
        led_status = not led_status
        print(f'led_status={led_status}')
        led.value(led_status)
        is_press = False
 
    time.sleep_ms(200)
        
    
'''
        led.toggle()
        time.sleep(0.5)
'''        