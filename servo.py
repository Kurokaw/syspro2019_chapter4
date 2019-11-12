import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

#y = (4.75/90)x + 7.25
def setservo(x):
	if x>90:
		servo.ChangeDutyCycle(top)
	elif x<-90:
		servo.ChangeDutyCycle(bottom)
	else :
		servo.ChangeDutyCycle((4.75/90)*x+7.25)

for i in range(5):
	setservo(-90)
	time.sleep(1.0)

	setservo(90)
	time.sleep(1.0)

	setservo(10)
	time.sleep(1.0)




