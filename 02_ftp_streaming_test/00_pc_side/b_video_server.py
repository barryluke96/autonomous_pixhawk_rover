#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
import numpy as np
import socket
import cv2

# create a socket and server setup
class VideoServer(object):

    def __init__(self, host, port):

        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.connection = self.connection.makefile('rb')
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.streaming()

    def streaming(self):

        try:

            # need bytes here
            stream_bytes = b' '
            
            while True:

                stream_bytes += self.connection.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')

                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)[120:240, :]

                    cv2.imshow('Video stream', image)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:

            # close connection
            self.connection.close()
            self.server_socket.close()


if __name__ == '__main__':

    # host IP address and connection port
    h, p = "192.168.2.105", 8000 # change "〇.〇.〇.〇" to user's PC IP address
    VideoServer(h, p)