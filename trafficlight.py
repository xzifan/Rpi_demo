# First we need to import the libraries that
# we need
# Import the time library so that we can make
# the program pause for a fixed amount of time
import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 3 on the GPIO header to act as
# an output
GPIO.setup(3,GPIO.OUT)
# Set Pin 5 on the GPIO header to act as
# an output
GPIO.setup(5,GPIO.OUT)
# Set Pin 7 on the GPIO header to act as
# an output
GPIO.setup(7,GPIO.OUT)
# This loop runs forever and flashes the LED
while True:

    # Turn on the red LED
    GPIO.output(3,GPIO.HIGH)
    # Wait for 2 seconds
    time.sleep(2)
    # Turn on the yellow LED
    GPIO.output(5,GPIO.HIGH)
    # Wait for 2 seconds
    time.sleep(2)
    # Turn off the yellow LED
    GPIO.output(5,GPIO.LOW)
    # Turn off the red LED
    GPIO.output(3,GPIO.LOW)
    # Turn on the green LED
    GPIO.output(7,GPIO.HIGH)
    # Wait for 2 seconds
    time.sleep(2)
    # Turn off the green LED
    GPIO.output(7,GPIO.LOW)
    # Turn on the yellow LED
    GPIO.output(5,GPIO.HIGH)
    # Wait for 2 seconds
    time.sleep(2)