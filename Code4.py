from machine import Pin
import time

stepm1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

in1=Pin(14, Pin.OUT)
in2=Pin(25, Pin.OUT)
in3=Pin(26, Pin.OUT)
in4=Pin(27, Pin.OUT)
pushbutton1=Pin(4,Pin.IN, Pin.PULL_UP)
pushbutton2=Pin(19,Pin.IN, Pin.PULL_UP)
my_t=0.005

while True:
    val=pushbutton1.value()
    val2=pushbutton2.value()
    
    if val==0:
        for i in range(0,501):
            for i in stepm1:
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                    
                time.sleep(my_t)
    if val2==0:
        for i in range(500,1001):
            for i in reversed (stepm1):
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                    
                time.sleep(my_t)
