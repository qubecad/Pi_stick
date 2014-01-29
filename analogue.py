#!/usr/bin/python
 
import spidev
import time
import os
import uinput
import pygame


 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def convertLowerToJoystickRange(value):
  result =-1.0+(value/520.0)
  return result

def convertUpperToJoystickRange(value):
  result=((value-520.0)/520.0)
  return result



joy_x=0
joy_y=1

while True:
    joy_x_value=ReadChannel(joy_x)
    
    print ("Joy X Value:{}".format(joy_x_value))
   
    if joy_x_value<515:
     
      print("x converted value {}".format(convertLowerToJoystickRange(joy_x_value)))
    elif joy_x_value>525:
      
      print("x converted value {}".format(convertUpperToJoystickRange(joy_x_value)))
    else:
      print("x converted value 0")
    
