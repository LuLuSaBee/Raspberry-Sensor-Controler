import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 19
GPIO_ECHO = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measure():
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    
    c = 331+0.6*25 # m/s
    distance = elapsed * c*100 # cm
    
    distance /= 2

    return distance

print("Utralsonic Measurement")

while True:
    cm = measure()
    print(f"Distance is : {cm}cm")
