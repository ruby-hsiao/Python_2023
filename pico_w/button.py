from machine import Pin
import time
import urequests as requests
from tools import connect,reconnect

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
            
            try:
                if led_status == True:
                    get_url = 'https://blynk.cloud/external/api/update?token=Mcr1vSCkqhfcoFpDr5aMN92mDNWKD0EC&v0=1'
                else:
                    get_url = 'https://blynk.cloud/external/api/update?token=Mcr1vSCkqhfcoFpDr5aMN92mDNWKD0EC&v0=0'  
                response = requests.get(get_url)
            except:
                reconnect()
            else:
                if response.status_code == 200:
                    print("傳送成功")
                else:
                    print("server有錯誤訊息")
                    print(f'status_code:{response.status_code}')
                response.close()

connect()
while True:
    btn_detect(button)