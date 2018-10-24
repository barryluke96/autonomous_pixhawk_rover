#!/usr/bin/env python2
# -*- coding: utf-8 -*-  


# read values sent from RC controller (in this case Futaba T10J) to PixHawk
# and calculate the biggest, smallest and average values, from channels 1 and 3.
# note : channel 3 is motor and channel 1 is steering servo.

# setting up libraries used in the program
from __future__ import print_function
from dronekit import connect
import exceptions
import socket
import time
import sys
import os

# establish connection to the vehicle
os.system("clear")
vehicle = connect('/dev/ttyS0', heartbeat_timeout = 30, baud = 57600)

# arming
vehicle.armed = True

# reminder to center each throttles
print ("\nCenter each throttles in order to get accurate reading in 5 seconds")

# initialize variables
a = 0
b1 = vehicle.channels['1']
c1 = vehicle.channels['1']
d1 = 0
b3 = vehicle.channels['3']
c3 = vehicle.channels['3']
d3 = 0
f = 1

# clear screen
time.sleep(5)
os.system("clear")

# print instruction
print ("Starting now, move each throttles corresponding to channels 1 and 3 in every direction to the fullest.") 
print ("The max, min, and avg reading values for each channels will be shown after 15 seconds. \n") 
print ("In order to quit without getting the reading press [Ctrl] + [C]." )
os.system("clear")

# loop will end after 30 seconds
while (a < 150):
    
    # calculating max, min, avg for channel 1
    print ("Channel 1 reading in real time: %s" % vehicle.channels['1'])

    if (b1 < vehicle.channels['1']):

        b1 = vehicle.channels['1']

    if (c1 > vehicle.channels['1']):

        c1 = vehicle.channels['1']

    d1 = (b1 + c1)/2

    # calculating max, min, avg for channel 3

    print ("Channel 3 reading in real time: %s" % vehicle.channels['3'])

    if (b3 < vehicle.channels['3']):

        b3 = vehicle.channels['3']

    if (c3 > vehicle.channels['3']):

        c3 = vehicle.channels['3']

    d3 = (b3 + c3)/2

    time.sleep(0.1)
    os.system("clear")
    a += 1

# clear screen
os.system("clear")

# print out the min, max, avg for channel 1 and 3
print ("From Channel 1,")
print ("» Biggest value is %s, smallest value is %s, average value is %s. \n" % (b1, c1, d1))
print ("From Channel 3,")
print ("» Biggest value is %s, smallest value is %s, average value is %s. \n" % (b3, c3, d3))