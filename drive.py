import RPi.GPIO as GPIO
from motor import Motor

def drive(movement):
    motor.stop()    
    if movement[0]:
        motor.left(100)
    elif movement[1]:
        motor.forward_left(100)
    elif movement[2]:
        motor.forward(100)
    elif movement[3]:
        motor.forward_right(100)
    elif movement[4]:
        motor.right(100)
    elif movement[5]:
        motor.backward(100)
