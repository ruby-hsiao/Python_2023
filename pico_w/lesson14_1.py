from machine import Timer, Pin, ADC
import time

def fun10(t:Timer | None = None):    
    print('5秒')
    led.toggle() #turn on/off led

def fun10ms(t:Timer):
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')

led = Pin(15, Pin.OUT)
light = ADC(Pin(28)) #光敏電阻接Pin28
vr = ADC(Pin(27)) #可變電阻接Pin27
timer10 = Timer(period=5000, mode=Timer.PERIODIC, callback=fun10)
timer10ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun10ms)
fun10() #trigger function first






