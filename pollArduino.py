import serial
import re

#TODO LIST USB devices and select Arduino
ser = serial.Serial('/dev/cu.usbmodem621', 9600)
while True:
	linein = ser.readline()
	parsed = re.split(r',', linein)
	print "lowpulse", parsed[0]
	print "ratio", parsed[1]
	print "concentration", parsed[2]
    
