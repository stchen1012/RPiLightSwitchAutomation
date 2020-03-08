import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#set up pin 40 for servo
GPIO.setup(40, GPIO.OUT)

#set up pin 5 for button
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#set PWM for servo
p = GPIO.PWM(40, 50)

p.start(2.5) #Initialization
time.sleep(1)

'''
def startServo():
    # The below code is to control the servo
    p.start(2.5) #Initialization
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    print("turn either on or off")
    time.sleep(5)
    p.ChangeDutyCycle(12.5)
    print("turn either on or off")
    time.sleep(5)
    #p.stop()
'''

# monitor state of button
motorStatus = False

while True:
    input_state = GPIO.input(5)
    if input_state == False:
        print("button has been pressed")
        time.sleep(.3)
        if motorStatus == False:
            p.ChangeDutyCycle(12.5)
            motorStatus = True
            time.sleep(.3)
        else:
            p.ChangeDutyCycle(2.5)
            motorStatus = False
            time.sleep(.3)


'''
#CDC degrees
try:
    while True:
        p.ChangeDutyCycle(2.5)
        print("0 degrees")
        time.sleep(5)
        p.ChangeDutyCycle(5)
        print("45 degrees")
        time.sleep(5)
        p.ChangeDutyCycle(7.5)
        print("90 degrees")
        time.sleep(5)
        p.ChangeDutyCycle(12.5)
        print("180 degrees")
        time.sleep(5)
        p.ChangeDutyCycle(2.5)
        print("go back to 0")
        time.sleep(5)


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
'''
