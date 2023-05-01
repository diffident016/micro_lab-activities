from machine import Pin, PWM, ADC, TouchPad
from time import sleep

frequency = 5000
threshold = 150

led_pins = [22, 19 , 18]
touch_pins = [12, 4, 15]

led = []
touch = [500, 500, 500]
touch_pin = []

for i in range(3):
    led.append(PWM(Pin(led_pins[i]), frequency))
    touch_pin.append(TouchPad(Pin(touch_pins[i], mode=Pin.IN)))
    
    led[i].duty(0)
    
pot = ADC(Pin(13))
pot.atten(ADC.ATTN_11DB)   

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    dim = convert(pot.read(), 0, 4095, 0, 1023)
    
    touch[0] = touch_pin[0].read()
    touch[1] = touch_pin[1].read()
    touch[2] = touch_pin[2].read()
    
    if(touch[0] < threshold):
        led[0].duty(dim)
    else:
        led[0].duty(0)
    
    if(touch[1] < threshold):
        led[1].duty(dim)
    else:
        led[1].duty(0)
    
    if(touch[2] < threshold):
        led[2].duty(dim)
    else:
     led[2].duty(0)
     
    sleep(0.2)

