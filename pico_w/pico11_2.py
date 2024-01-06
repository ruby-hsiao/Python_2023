import network
import time
import urequests as requests
from machine import WDT, Timer, ADC


#連線等待10秒
def connect():
    # enable station interface and connect to WiFi access point
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect('RHS', '1526314a')

    max_wait = 10

    #處理正在連線
    while max_wait > 0:
        max_wait -= 1
        status = nic.status()
        if status < 0 or status >=3:
            break
        print("等待連線")
        time.sleep(1)


        
    #沒有wifi的處理
    if nic.status() != 3:
        #連線失敗,重新開機
        #wdt = WDT(timeout=2000)
        #wdt.feed()
        raise RuntimeError("連線失敗")
        
    else:
        print("成功連線")
        print(nic.ifconfig())


def alert():
    print('要爆炸了!')
    response = requests.get('https://hook.eu2.make.com/ij57vtw5jvkaj1p5asl6j1fv3835nu4e?name=pico&date=202401061405&temperature=28.5')
    print(help(response))
    response.close()
    
def doTimer(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 27 and delta >= 60 * 1000:        
        alert()
        start = time.ticks_ms()#重新設定計時的時間
        

connect()       

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒    
time1 = Timer()
time1.init(period=1000,callback=doTimer)

