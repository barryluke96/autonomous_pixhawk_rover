#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
import socket
import pickle

# create a socket and server setup
class DistanceServer(object):
    
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

        try:

            while True:

                # convert pickle to int
                distance = pickle.loads(self.connection.recv(1024))
                print ("Distance: %d [cm]" % distance)

        finally:

            # close connection
            self.connection.close()
            self.server_socket.close()


if __name__ == '__main__':

    # host IP address and connection port
    h, p = "192.168.2.105", 8002 # change "〇.〇.〇.〇" to user's PC IP address
    DistanceServer(h, p)