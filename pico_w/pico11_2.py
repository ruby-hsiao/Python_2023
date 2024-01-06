import network
import time
import urequests as requests
from machine import WDT, Timer, ADC, RTC


ssid = 'RHS'
pwd = '1526314a'

# enable station interface and connect to WiFi access point
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect()#反覆測試才加上這個斷線
wlan.connect(ssid, pwd)

#連線等待10秒
def connect():
    max_wait = 10

    #處理正在連線
    while max_wait > 0:
        max_wait -= 1
        status = wlan.status()
        if status < 0 or status >=3:
            break
        print("等待連線")
        time.sleep(1)


        
    #沒有wifi的處理
    if wlan.status() != 3:
        #連線失敗,重新開機
        #wdt = WDT(timeout=2000)
        #wdt.feed()
        raise RuntimeError("連線失敗")
        
    else:
        print("成功連線")
        print(wlan.ifconfig())

def reconnect():
    if wlan.status() == 3: #還在連線, 只是傳送的server無回應
        print(f"無法連線({wlan.status()})")
        return
    else:
        print("嘗試重新連線")
        wlan.disconnect()
        wlan.connect(ssid, password)
        connect()

def alert(t:float):
    rtc = RTC()
    date_tuple = rtc.datetime()
    year = date_tuple[0]
    month = date_tuple[1]
    date = date_tuple[2]
    hour = date_tuple[4]
    minute = date_tuple[5]
    second = date_tuple[6]
    date_str = f'{year}-{month}-{date} {hour}:{minute}:{second}'
    
    print('要爆炸了!')
    
    try:
        response = requests.get(f'https://hook.eu2.make.com/ij57vtw5jvkaj1p5asl6j1fv3835nu4e?name=我的家電2&date={date_str}&temperature={t}')
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("server 有錯誤訊息")
            print(f'status_code:{response.status_code}')
        response.close()    
        
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
        alert(temperature)
        start = time.ticks_ms()#重新設定計時的時間
        

connect()       

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒    
time1 = Timer()
time1.init(period=1000,callback=doTimer)

