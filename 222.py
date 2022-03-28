from RPi import GPIO as gpio
import time


def dectobin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]


gpio.setup(dac, gpio.OUT, initial=1)
period = float(input(("write\n")))
try:
    x=0
    while True:
        for i, val in enumerate(dectobin(x%256)):
            gpio.output(dac[i], val)
        time.sleep(period/(2*256))
        x+=1

        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
