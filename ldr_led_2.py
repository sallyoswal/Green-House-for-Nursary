import RPi.GPIO as gpio
import SDL_DS1307
import datetime
import time

def readTime():
    try:
        ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
        return ds1307.read_datetime()
    except:
        # alternative: return the system-time:
        return datetime.datetime.utcnow()

def checkLight():
    timestamp = readTime()
    if 9 <= timestamp.hour <= 17
        if gpio.input(18) == 1:
            gpio.output(22, 1)
        else:
            gpio.output(22, 0)
    else:
        gpio.output(22, 1)

if __name__ == '__main__':
    try:
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        while True:
            checkLight()
            time.sleep(5000)
    except:
        gpio.cleanup()
