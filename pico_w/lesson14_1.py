from machine import Timer, Pin, ADC
import time

def fun10(t:Timer | None = None):    
    print('5秒')
    led.toggle() #turn on/off led
    
led = Pin(15, Pin.OUT)
light = ADC(Pin(28))
timer10 = Timer(period=5000, mode=Timer.PERIODIC, callback=fun10)
fun10() #trigger function first


while True:
    print(light.read_u16())
    time.sleep_ms(500)


