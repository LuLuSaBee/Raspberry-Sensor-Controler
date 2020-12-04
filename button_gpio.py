import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
GPIO.setup(3, GPIO.OUT)
GPIO.add_event_detect(15, GPIO.RISING)

while True:
    if GPIO.input(15) == 0:
        print("Off")
    if GPIO.event_detected(15):
        print("event detected")
        GPIO.output(3, 1)
        time.sleep(0.5)
        GPIO.output(3, 0)
