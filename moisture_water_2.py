import RPi.GPIO as gpio
import time


def wateringPlants():
    # read moisture
    gpio.setup(15, gpio.in)
    value = gpio.input(15)
    if value == 1
        # turn pump on for some seconds
        GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
        time.sleep(5)
        GPIO.output(17, GPIO.HIGH)
        sleep(1000)

if __name__ == '__main__':
    try:
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        while True:
            wateringPlants()
            time.sleep(5000)
    except:
        gpio.cleanup()
