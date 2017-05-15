from motor import Motor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
car = Motor(11,13,7,154,16,18)

car.forward(100)
time.sleep(3)
car.stop()
car.backward(100)
time.sleep(3)
car.stop()

GPIO.cleanup()
