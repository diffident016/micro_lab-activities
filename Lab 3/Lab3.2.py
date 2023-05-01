from machine import Pin, PWM, ADC, TouchPad
from time import sleep

frequency = 5000
threshold = 300

led_pins = [25, 33 , 32]
touch_pins = [13, 14, 27]

led = []
touch = [False, False, False]
touch_pin = []

for i in range(3):
    led.append(PWM(Pin(led_pins[i]), frequency))
    touch_pin.append(TouchPad(Pin(touch_pins[i], mode=Pin.IN)))
        
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)   

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    dim = convert(pot.read(), 0, 4095, 0, 1023)
    
    touch[0] = touch_pin[0].read() < threshold
    touch[1] = touch_pin[1].read() < threshold
    touch[2] = touch_pin[2].read() < threshold
    
    
    if touch[0] or touch[1] or touch[2]:
        if not touch[0]:
            led[0].duty(0)
        else:
            led[0].duty(dim)
        
        if not touch[1]:
            led[1].duty(0)
        else:
            led[1].duty(dim)
        
        if not touch[2]:
            led[2].duty(0)
        else:
            led[2].duty(dim)
    else:
        led[0].duty(dim)
        led[1].duty(dim)
        led[2].duty(dim)
 
    sleep(0.2)


