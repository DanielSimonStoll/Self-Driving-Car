import sys, tty, termios
import RPi.GPIO as GPIO
from motor import Motor
from drive import drive
import picamera
from trainingdata import createData

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
motor = Motor(15,16,18,13,11,7)

def getKey():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while(True):
    movement = [0,0,0]
    e = getKey()
    if e == 'x':
        GPIO.cleanup()
        exit()
    elif e == 'a':
        movement[0] = 1
    elif e == 'w':
        movement[1] = 1
    elif e == 'd':
        movement[2] = 1

    motor.stop()    
    if movement[0]:
        motor.forward_left(100)
    elif movement[1]:
        motor.forward(100)
    elif movement[2]:
        motor.forward_right(100)

    createData(movement)
