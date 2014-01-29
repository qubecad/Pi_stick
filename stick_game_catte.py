#!/usr/bin/python
 
import spidev
import time
import os
import uinput
import pygame
import sys


# setup pygame
pygame.init()

speed=[0,0]
alienspeed=[0,1]
black = 0,0,0
white = 255,255,255
grey = 205,205,193
green = 0,205,0

size=width,height=320,240

screen = pygame.display.set_mode(size)

cat = pygame.image.load("cat.gif")
w,h=cat.get_size()
cat = pygame.transform.scale(cat,(int(w*0.25),int (h*0.25)))

catrect=cat.get_rect()

alien=pygame.image.load("alien.gif")
w,h=alien.get_size()
alien = pygame.transform.scale(alien,(int(w*0.25),int (h*0.25)))
alienrect=alien.get_rect()

furball=pygame.image.load("furball.gif")
furballrect=furball.get_rect()

  
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# define analogue channels 

joy_x=0
joy_y=1

# setup text

myfont = pygame.font.SysFont("Times New Roman",10)


# set alien starting point
alienrect.right=300


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
  
    joy_x_value=ReadChannel(joy_x)
    
    if joy_x_value<500:
      speed[0]=-2
    elif joy_x_value>530:
      speed[0]=2
    else:
      speed[0]=0

    joy_y_value=ReadChannel(joy_y)

    if joy_y_value<500:
      speed[1]=-2
    elif joy_y_value>530:
      speed[1]=2
    else:
      speed[1]=0

      

    # move the cat sprite
    catrect=catrect.move(speed)

    # move the alien

    alienrect=alienrect.move(alienspeed)
    if alienrect.top <0 or alienrect.bottom >height:
      alienspeed[1]=-alienspeed[1]

        

    # update joystick text  
    location=("X: {} Y: {} ".format(joy_x_value,joy_y_value))
    label=myfont.render(location,1,green)
  
    # update screen
    screen.fill(grey)
    screen.blit(alien,alienrect)
    screen.blit(label,(10,10))
    screen.blit(cat,catrect)
    pygame.display.flip()
    
