#!/usr/bin/python
 
import spidev
import time
import os
import uinput



 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

device =uinput.Device([uinput.BTN_JOYSTICK,
                      uinput.ABS_X+(0,1023,0,0),
                      uinput.ABS_Y+(0,1023,0,0),
                      ])



joy_x=0
joy_y=1
joy_button=2
joy_button_a=3

while True:
    joy_x_value=ReadChannel(joy_x)
    
    #print ("Joy X Value:{}".format(joy_x_value))
   
    device.emit(uinput.ABS_X,joy_x_value,syn=False)

    joy_y_value=ReadChannel(joy_y)
    
    #print ("Joy Y Value:{}".format(joy_y_value))
   
    device.emit(uinput.ABS_Y,joy_y_value)

    joy_button_value=ReadChannel(joy_button)

    if joy_button_value==1:
#      print ("Button Pressed {}".format(joy_button_value))
      device.emit(uinput.BTN_JOYSTICK,1)
    else:
#      print ("Button Not Pressed {}".format(joy_button_value))
      #device.emit(uinput.BTN_JOYSTICK,0)

      joy_button_a_value=ReadChannel(joy_button_a)

    if joy_button_a_value==1:
      print ("Button Pressed {}".format(joy_button_a_value))
      device.emit(uinput.BTN_JOYSTICK,1)
    else:
    #  print ("Button Not Pressed {}".format(joy_button_value))
      device.emit(uinput.BTN_JOYSTICK,0)
      

    time.sleep(0.020)
     

     
    
      
    
