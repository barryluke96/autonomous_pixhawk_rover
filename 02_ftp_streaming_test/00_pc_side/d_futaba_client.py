#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
from pygame.locals import *
import pygame.display
from socket import *
import pygame
import time
import os

# create a socket and bind socket to the host later
client_socket = socket(AF_INET, SOCK_STREAM)
HOST = '192.168.2.107' # change '〇.〇.〇.〇' to user's RPi IP address
PORT = 8004

# open small pygame windows to take user input
pygame.display.init()
screen = pygame.display.set_mode((250,250))

# sending the data
try:

    # initialization
    loop = True
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

    # server connected
    while loop:

        # get user input to control the rover
        for event in pygame.event.get():
        
            # when the key was pressed down
            if event.type == KEYDOWN:
                
                # register the pressed down key
                user_input = pygame.key.get_pressed()

                # if it is ↑
                if user_input[pygame.K_UP]:

                    client_socket.send('1'.encode())

                # if it is →
                elif user_input[pygame.K_RIGHT]:

                    client_socket.send('2'.encode())

                # if it is ←
                elif user_input[pygame.K_LEFT]:

                    client_socket.send('3'.encode())

                # if it is ↓
                elif user_input[pygame.K_DOWN]:

                    client_socket.send('4'.encode())

                # if it is b
                elif user_input[pygame.K_b]:

                    client_socket.send('5'.encode())

                # to end the program press [q] key on Pygame window
                elif key_input[pygame.K_q]:
                    
                    loop = False
                    break

            # when the key were lifted loop back
            elif event.type == pygame.KEYUP:

                break

# close the socket
finally:
    
    client_socket.close()