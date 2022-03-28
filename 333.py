from RPi import GPIO as gpio
import time
def cycle():
    num=input("Input number in range 0-100:\n")
    if num == "q":
        return None
    if not num.isdigit():
        print("error")
        return cycle()
    if abs(int(num))!=int(num):
        print("error")
        return cycle()
    if int(num)>100:
        print("error")
        return cycle()
    return int(num)
def dectobin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)
a= gpio.PWM(23, 1000)
a.start(0)
try:
    while True:
        num = cycle()
        a.ChangeDutyCycle(num)
        print("approx.voltage: {:.4f}".format(3.3 * num /100))
    
finally:
    gpio.output(23, 0)
    gpio.cleanup()