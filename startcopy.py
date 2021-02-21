import RPi.GPIO as GPIO
import time
from time import sleep 
import urllib2
import os

global maxCount

count = 0
text = os.walk("/home/pi/people")
for a,b,s in text:
    for n in s:
        f = "/home/pi/people/%s" % n
        os.remove(f)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def add(channel):
    global count        
    count = count + 1
    file = "/home/pi/people/%d.dat" % count
    open(file, "w+")
   
    if count >  maxCount:
        print ("Too Many People")
	count2 =  count - maxCount
	print (count2,"People Over Capacity")
    else: 
        print (count)

def sub(channel):
        global count
        if count == 0:
		print(count)
		return None
        file = "/home/pi/people/%d.dat" % count
        os.remove(file)
        count = count - 1
        print (count)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=add)
GPIO.add_event_detect(12, GPIO.RISING, callback=sub)

testText = input("Please Enter Max Capacity: \n")
maxCount = int(testText)
os.remove("/home/pi/max/%s" %  os.listdir('/home/pi/max')[0])
file = "/home/pi/max/%d" % maxCount
open(file, "w+")

print ("Max Capacity: ", maxCount)
message = input("Start \n")


GPIO.cleanup()

