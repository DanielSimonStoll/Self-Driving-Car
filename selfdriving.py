import sys, tty, termios
import RPi.GPIO as GPIO
from motor import Motor
import picamera
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from model import load_model

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
motor = Motor(15,16,18,13,11,7)
load_model()

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
    camera = picamera.Camera()
    camera.resolution = (128, 128)
    camera.capture('/Desktop/Self-Driving-Car/CurrentData/img.jpeg',format='jpeg')
    
    
