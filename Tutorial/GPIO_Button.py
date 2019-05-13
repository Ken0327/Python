import RPi.GPIO as GPIO
import time

Pin_LED1 = 11
Pin_LED2 = 13
button1 = 3
button2 = 5

def button1_callback():
    GPIO.output(Pin_LED1, GPIO.HIGH)
    print("Button1 was pushed!")

def button2_callback():
    GPIO.output(Pin_LED2, GPIO.HIGH)
    print("Button2 was pushed!")
    
def twoButtonPressed():
    GPIO.output(Pin_LED1, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(Pin_LED1, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(Pin_LED2, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(Pin_LED2, GPIO.LOW)

def ResetGPIO():
    GPIO.output(Pin_LED1, GPIO.LOW)
    GPIO.output(Pin_LED2, GPIO.LOW)

def InitialGPIO():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 3 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 5 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(Pin_LED1, GPIO.OUT)
    GPIO.setup(Pin_LED2, GPIO.OUT)
    # GPIO.add_event_detect(button1, GPIO.RISING,callback=button1_callback) # Setup event on pin 3 rising edge
    # GPIO.add_event_detect(button2, GPIO.RISING,callback=button2_callback) # Setup event on pin 5 rising edge

InitialGPIO()
ResetGPIO()
print('Start')

while True:
    input_state1 = GPIO.input(button1)
    input_state2 = GPIO.input(button2)
    if input_state1 == False and input_state2 == False:
        print('two button pressed')
        twoButtonPressed()
    else:
        ResetGPIO()
    time.sleep(0.5)
    # message = input("Press enter to quit\n\n") # Run until someone presses enter
ResetGPIO()
GPIO.cleanup()