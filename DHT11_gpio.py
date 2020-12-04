import RPi.GPIO as GPIO
import time
import datetime
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

instance = dht11.DHT11(pin = 29)

while True:
    ret = instance.read()
    if ret.is_valid():
        print(f"Current time {str(datetime.datetime.now())}")
        print(f"Current temperature: {ret.temperature} C")
        print(f"Current humidity: {ret.humidity} %")
    
    time.sleep(1)
