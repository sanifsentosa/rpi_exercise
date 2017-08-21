import RPi.GPIO as GPIO
import time

ledpin = 11
ledpin1 = 15
ledpin2 = 13
#3led = [11, 13, 15]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(ledpin1, GPIO.OUT)
GPIO.setup(ledpin2, GPIO.OUT)


try:
    while True:
        GPIO.output(ledpin,False)
        GPIO.output(ledpin1,False)
        GPIO.output(ledpin2,False)

        command = input("B, R, or Y:")
        if command == "B":
             GPIO.output(ledpin,True)
        elif command == "R":
             GPIO.output(ledpin1,True)
        elif command == "Y":
             GPIO.output(ledpin2,True)
        elif command == "A":
             GPIO.output(ledpin,True)
             GPIO.output(ledpin1,True)
             GPIO.output(ledpin2,True)
        input("Press any key to continue...")

except KeyboardInterrupt:
    GPIO.output(ledpin,False)
    GPIO.output(ledpin1,False)
    GPIO.output(ledpin2,False)
    GPIO.cleanup()
