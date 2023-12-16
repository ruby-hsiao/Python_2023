from machine import Timer

def doTimer(t:Timer):
    #print(type(t))
    print(1)
    
def doTimer2(t):
    print(2)
    
def doTimer3(t:Timer):    
    print(3)
    t.deinit()#delete timer instance
    
time1 = Timer()
time1.init(freq=1, callback=doTimer)

time2 = Timer()
time2.init(period=2000, callback=doTimer2)

time3 = Timer()
time3.init(period=3000, callback=doTimer3)