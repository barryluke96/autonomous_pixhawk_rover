#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# setting up modules used in the program
from dronekit import connect
import time

# wait until all the codes stop gracefully
time.sleep(1)

# establish connection to the vehicle
vehicle = connect('/dev/ttyS0', heartbeat_timeout = 30, baud = 57600)

# put motor/servo to the original position and release the override
vehicle.channels.overrides = {'3':1515, '1':1532}
vehicle.channels.overrides = {'3':None, '1':None}

# wait until override completed
time.sleep(1)

# disarm the vehicle
vehicle.armed = False
vehicle.close()