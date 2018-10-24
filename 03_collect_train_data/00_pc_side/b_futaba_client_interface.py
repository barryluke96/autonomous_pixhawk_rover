#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
from socket import *
import time

# create a socket and bind socket to the host later
client_socket = socket(AF_INET, SOCK_STREAM)
HOST = '192.168.2.107' # change '〇.〇.〇.〇' to user's RPi IP address
PORT = 8004


# initialization
connected = False

# server not connected
while not connected:

    # bind socket to the host
    try:

        client_socket.connect((HOST, PORT))
        connected = True

    # loop (pass) back to while not connected
    except Exception as e:

        pass

# if it is ↑↑
def forward():

    client_socket.send("1".encode())

# if it is ↑→
def forward_right():

    client_socket.send("2".encode())

# if it is ←↑
def forward_left():
            
    client_socket.send("3".encode())

# if it is ↓↓
def reverse():

    client_socket.send("4".encode())

# if it is b
def brake():

    client_socket.send("5".encode())

# close the socket
def close_socket():

    client_socket.close()