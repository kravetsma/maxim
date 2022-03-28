from RPi import GPIO as gpio


def cycle():
    num = input("Введите число от 0 до 100:\n")
    if num == 'q':
        return None
    if not num.isdigit():
        print('input error')
        return cycle()
    if abs(int(num)) != int(num):
        print('input error')
        return cycle()
    if int(num) > 100:
        print('input error')
        return cycle()
    return int(num)


gpio.setmode(gpio.BCM)
gpio.setup(22, gpio.OUT)
shim = gpio.PWM(22, 1000)
shim.start(0)

try:
    while __name__ == '__main__':
        num = cycle()
        shim.ChangeDutyCycle(num)
        print("approx. voltage: {:.4f}".format(3.3 * num / 100))
finally:
    gpio.output(22, 0)
    gpio.cleanup()