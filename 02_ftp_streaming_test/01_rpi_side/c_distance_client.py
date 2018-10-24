#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# setting up modules used in the program
import RPi.GPIO as GPIO
import socket
import pickle
import time

GPIO.setwarnings(False)

# create a socket and bind socket to the host later
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '192.168.2.105' # change '〇.〇.〇.〇' to user's PC IP address
PORT = 8002

# measuring the distance from ultrasonic sensor
def measure():

    time.sleep(0.1)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:

        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:

        stop = time.time()

    elapsed = stop - start
    measured = (elapsed * 34300) / 2

    return measured

# truncate 'out of range' reading to 100 cm 
def truncate():
    
    truncated = measure()

    if (truncated > 50):

        truncated = 50
    
    return truncated

# 5 seconds of median reading between 0.1 sec interval
def median():

    take0 = truncate()
    take1 = truncate()
    take2 = truncate()
    take3 = truncate()
    take4 = truncate()
    array = [take0, take1, take2, take3, take4]
    array.sort()

    return array[2]

# referring to the pins by GPIO numbers
GPIO.setmode(GPIO.BCM)

# define pi GPIO
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# output pin: Trigger
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
# input pin: Echo
GPIO.setup(GPIO_ECHO,GPIO.IN)
# initialize trigger pin to low
GPIO.output(GPIO_TRIGGER, False)

# sending the data
try:

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

    # send the data
    while True:
        
        distance = int(median())
        client_socket.send(pickle.dumps(distance))
        # print ("Distance: %d [cm]" % distance)

# close the socket
finally:
    
    client_socket.close()
    GPIO.cleanup()