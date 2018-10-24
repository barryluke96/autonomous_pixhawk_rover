#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# source: http://python.dronekit.io/guide/connecting_vehicle.html#get-started-connect-string
# test the connection between Raspberry Pi 3 and PixHawk through serial connection.
# if the program's last output is 'DroneKit manage to connect with Pixhawk!', 
# there is no problem with the setup.

# setting up modules used in the program
import exceptions
import dronekit
import socket
import os

# clear screen
os.system("clear")

# connection setting
try:

    print ("Connecting to port /dev/ttyS0")
    print ("With baudrate = 57600\n")
    dronekit.connect("/dev/ttyS0", heartbeat_timeout = 30, baud = 57600)

# bad TTY connection error
except exceptions.OSError as e:

    print ("No serial exists!")

# API error
except dronekit.APIException:

    print ("Timeout!")

# other error
except:

    print ("Some other error!")

# succesful connection
else:
    
    print ("DroneKit manage to connect with Pixhawk!")
