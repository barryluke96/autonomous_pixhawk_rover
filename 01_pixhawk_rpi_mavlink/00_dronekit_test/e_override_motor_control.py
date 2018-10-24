#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# override RC (in this case Futaba T10J) and allow us to control
# the drone from keyboard.

# setting up libraries used in the program
from __future__ import print_function
from dronekit import connect
import exceptions
import curses
import socket
import time
import os

# connecting to the PixHawk
os.system("clear")
vehicle = connect('/dev/ttyS0', heartbeat_timeout = 30, baud = 57600)
vehicle.armed = True
time.sleep(5)
os.system("clear")

# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)
 
try:

    while True:
        
        char1 = screen.getch()
        char2 = screen.getch()
        char3 = screen.getch()
        
        # print doesn't work with curses, use addstr instead
        screen.addstr(0, 0, 'A program that allow us to bypass Futaba T10J radio control.\n\nNum1 for left, Num [3] for right and Num [5] for center the steering.\nNum [8] for forward, Num [0] for backward and Num [5] to brake.\nTo quit press [q].')
        
        if char2 == ord('q'):

            break

        if char1 == ord('3'):

            vehicle.channels.overrides['1'] = 1924

        elif char1 == ord('1'):

            vehicle.channels.overrides['1'] = 1104

        elif char3 == ord('2'):

            vehicle.channels.overrides['1'] = 1515

        if char3 == ord('5'):

            vehicle.channels.overrides['3'] = 1924

        elif char3 == ord('0'):

            vehicle.channels.overrides['3'] = 1104

        elif char3 == ord('2'):
            
            vehicle.channels.overrides['3'] = 1532

finally:
    
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    print("Clear all overrides")
    vehicle.channels.overrides = {}
    print("\nClose vehicle object")
    vehicle.close()
    os.system("clear")
