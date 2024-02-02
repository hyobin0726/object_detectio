import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
soundpin =37
GPIO.setup(soundpin,GPIO.IN)
global soundlevel

while(True):
	soundlevel=GPIO.input(soundpin)
	if(soundlevel==1):
		break
