import time
import datetime
import RPi.GPIO as GPIO
import urllib2

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)


GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.LOW)

GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.LOW)

GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.LOW)

while True:

    GPIO.output(3,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)

    dat = datetime.datetime.now()
    dateTxt = dat.strftime("%Y-%m-%d")
    dat2  = datetime.datetime.now()
    dat2Txt = dat2.strftime("%H:%M:%S")
    data = urllib2.urlopen("http://users.du.se/~h19zifxi/ik2018distr/rpi_http_get.php?color=red&timeStamp="+dateTxt+dat2Txt)
    print data.read()

    time.sleep(2)
    GPIO.output(3,GPIO.LOW)

    GPIO.output(5,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(5,GPIO.LOW)

    GPIO.output(7,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(7,GPIO.LOW)

    # GPIO.output(5,GPIO.HIGH)
    # time.sleep(2)
    # GPIO.output(5,GPIO.LOW)

    # GPIO.output(3,GPIO.HIGH)
    # time.sleep(5)
    # GPIO.output(3,GPIO.LOW)

    # time.sleep(5)