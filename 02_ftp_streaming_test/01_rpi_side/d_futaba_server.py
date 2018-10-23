#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

#    CHANNEL 1 AND CHANNEL 3 READING REFERENCE
#
#      [channel 1: left and right]
#      - middle reading: 1515
#      - full left reading: 1104
#      - half left reading: 1310
#      - full right reading: 1924
#      - half right reading: 1720
#
#      [channel 3: forward and backward]
#      - middle reading: 1532
#      - full up reading: 1924
#      - half up reading: 1728
#      - full down reading: 1104
#      - half down reading: 1318

# setting up modules used in the program
from __future__ import print_function
from dronekit import connect
from socket import *
import socket
import time

# Establishing connection from RPi to PixHawk
vehicle = connect('/dev/ttyS0', heartbeat_timeout = 30, baud = 57600)
vehicle.armed = True

# global variables
forward = 1650  # channel 3
reverse = 1410  # channel 3
center = 1515   # channel 3
right = 1874    # channel 1
left = 1154     # channel 1
stop = 1532     # channel 1
end = 0.4       # end time

# create a socket and server setup
class FutabaServer(object):

    def __init__(self, host, port):

        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.streaming()

    def streaming(self):

        # loop
        try:

            # initial motor/servo state
            vehicle.channels.overrides = {'3':1515, '1':1532}
            
            while True:

                # server receive from client
                user_input = int(self.connection.recv(1024).decode())
                # print(user_input)

                # time after end second
                time_end = time.time() + end

                # continuously override the channels for specified second before stopping
                while time.time() < time_end:

                    # forward and the steering is centered
                    if (user_input == 1):

                        vehicle.channels.overrides = {'3':forward, '1':center}

                    # forward and the steering is turning right
                    elif (user_input == 2):

                        vehicle.channels.overrides = {'3':forward, '1':right}

                    # forward and the steering is turning left
                    elif (user_input == 3):

                        vehicle.channels.overrides = {'3':forward, '1':left}

                    # reverse and the steering is centered
                    elif (user_input == 4):

                        vehicle.channels.overrides = {'3':reverse, '1':center}

                    # brake and the steering is centered
                    elif (user_input == 5):

                        vehicle.channels.overrides = {'3':reverse, '1':center}
                        vehicle.channels.overrides = {'3':stop, '1':center}

                    # send override commands every 0.1 second
                    time.sleep(0.1)
                
                # stop the motor and the steering is centered
                if (user_input == 1 or user_input == 4 or user_input == 5):

                    vehicle.channels.overrides = {'3':stop, '1':center}

                # stop the motor and the steering is turning right                
                elif (user_input == 2):

                    vehicle.channels.overrides = {'3':stop, '1':right}
                
                # stop the motor and the steering is turning left
                elif (user_input == 3):

                        vehicle.channels.overrides = {'3':stop, '1':left}                

        finally:

            self.connection.close()
            self.server_socket.close()

if __name__ == '__main__':

    # host IP address and connection port
    h, p = "192.168.2.107", 8004 # change "〇.〇.〇.〇" to user's RPi IP address
    FutabaServer(h, p)