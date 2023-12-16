import network
import time

ssid = 'RHS'
pwd = '1526314a'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect()#反覆測試才加上這個斷線
wlan.connect(ssid, pwd)

#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#<0,>3失敗的連線

#10秒內確認連線與否
max_wait = 10
while max_wait > 0:
    status = wlan.status()
    if status < 0 or status >=3:
        break;
    max_wait -= 1
    print("等待連線...")
    time.sleep(1)
    
#檢查目前連線狀態
if wlan.status() != 3:
    print(wlan.status())
    raise RuntimeError("連線失敗")
else:
    print("連線成功")
    config = wlan.ifconfig()
    print(f'client ip={config[0]}')