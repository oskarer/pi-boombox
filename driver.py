#!/usr/bin/env python

import serial
import time

lcd = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", 9600,
               serial.EIGHTBITS,
                    serial.PARITY_NONE,
                    serial.STOPBITS_ONE,
                    timeout=5,
                    rtscts = False)
#time.sleep(0.1)
wait = 0.04

def BacklightOff():
   command = ["\xFE","\x46","\xFE","\x46"]
   for item in command:
      lcd.write(item)
   #time.sleep(wait)
   
   
def BacklightOn():
   command = ["\xFE","\x42","\x00","\xFE","\x42","\x00"]
   for item in command:
      lcd.write(item)   
   time.sleep(wait)
   
#This function writes the date to the lines passed in as a parameter eg Writeline("This is a test","1")
#will write "This is a test" to line 1. If the data is "$blank" it will print a blank line on the display.
#The string has to be 16 characters if it is not the funtion will pad spaces after it. If it is too long
#it will trim it. If an invalid line is specified it assumes line 1.

def Writeline(data,line):
   if data == "$blank":
      data ="                "
   elif line == "1":
      line = "\x01"
   elif line == "2":
      line = "\x02"
   elif line != "1" or "2":
      line = "1"
   import string
   data = data.ljust(16)
   data = data [:16]
   command = ["\xFE","\x47","\x01",line,data]   
   for item in command:
      lcd.write(item)
   time.sleep(wait)
