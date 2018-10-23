#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# test if the Pixhawk are armeable via MAVLink
#
#     note:
#       0 = Quit program
#       1 = Disarm
#       2 = Arm

# setting up modules used in the program
from dronekit import connect
import exceptions
import socket
import time
import os

# clear screen
os.system("clear")
# establish connection to the vehicle
vehicle = connect("/dev/ttyS0", heartbeat_timeout = 30, baud = 57600)
# print action to be carried
print ("Set vehicle state to disarm")
# for safety, disarm the vehicle before doing anything
vehicle.armed = False
print ("Armed: %s\n" % vehicle.armed)
time.sleep(5)
# clear screen
os.system("clear")

# initialization
a = 1

while (a > 0):

    # print the current vehicle state
    if  (a == 1):

        print ("Vehicle is in disarm state")
        
    if  (a == 2):
        print ("Vehicle is in arm state")

    # print information
    a = int(raw_input("Press [0] to quit the demo, [1] to disarm, enter [2] to arm: "))

    if (a == 1):

        # disarm the vehicle
        vehicle.armed = False
    
    if (a == 2):

        # disarm the vehicle
        vehicle.armed = True

    time.sleep(5)
    # clear screen
    os.system("clear")
