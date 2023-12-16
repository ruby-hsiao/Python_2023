from machine import ADC, Timer
import time

def alert():
    print("On Fire!")
    
    
def doTimer(t:Timer):
    # define 全域變數
    global start
    # measure temperature
    sensor = ADC(4) # 4 for fifth channel 
    
    # measure vol
    vol = sensor.read_u16() * (3.3/65535) # read value, 0-65535 across voltage range 0.0v - 3.3v
    # Veb=0.706V at 27 degree C, with a slope偏移 -1.721mV(0.001721)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')
    
    #start = time.ticks_ms() - 60 * 1000
    #print(start)
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 23.3 and delta >= 10 - 60 * 1000:
        alert()
        start = time.ticks_ms()

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒

time1 = Timer()
time1.init(period=1000, callback=doTimer)