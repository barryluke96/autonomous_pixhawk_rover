#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# setting up modules used in the program
import picamera
import socket
import struct
import time
import io

# create a socket and bind socket to the host later
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '192.168.2.105' # change '〇.〇.〇.〇' to user's PC IP address
PORT = 8000

# sending the data
try:
    
    # initialization
    connected = False
    
    # server not connected
    while not connected:

        # bind socket to the host
        try:

            client_socket.connect((HOST, PORT))
            connection = client_socket.makefile('wb')
            connected = True

        # loop (pass) back to while not connected
        except Exception as e:

            pass

    # server connected
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)      # pi camera resolution
        camera.framerate = 15               # 15 frames/second
        time.sleep(2)                       # give 2 secs for camera to initilize
        start = time.time()
        stream = io.BytesIO()

        # send jpeg format video stream
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):

            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())

            # video streaming will stop automatically after 1 hour
            if time.time() - start > 600:
                
                break

            stream.seek(0)
            stream.truncate()

    connection.write(struct.pack('<L', 0))

finally:
    
    connection.close()
    client_socket.close()