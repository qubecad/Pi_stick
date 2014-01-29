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

joy_x=0
joy_y=1

while True:
    joy_x_value=ReadChannel(joy_x)
    
    print ("Joy X Value:{}".format(joy_x_value))

    joy_y_value=ReadChannel(joy_y)

    print ("Joy Y Value:{}".format(joy_y_value))
    
