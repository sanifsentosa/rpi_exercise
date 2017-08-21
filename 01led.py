import RPi.GPIO as GPIO
import time

ledpin = 11
ledpin1 = 15
ledpin2 = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.output(ledpin, GPIO.HIGH)
GPIO.setup(ledpin1, GPIO.OUT)
GPIO.output(ledpin1, GPIO.HIGH)
GPIO.setup(ledpin2, GPIO.OUT)
GPIO.output(ledpin2, GPIO.HIGH)


try:
    while True:
        GPIO.output(ledpin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(ledpin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(ledpin1, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(ledpin1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(ledpin2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(ledpin2, GPIO.HIGH)
        time.sleep(0.3)
	
except KeyboardInterrupt:
    GPIO.output(ledpin, GPIO.HIGH)
    GPIO.output(ledpin1, GPIO.HIGH)
    GPIO.output(ledpin2, GPIO.HIGH)
    GPIO.cleanup()
