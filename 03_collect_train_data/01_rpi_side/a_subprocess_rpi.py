#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

# setting up modules being used in the program
import subprocess as sp
import sys
import os

# check os compatibility
if os.name == 'nt':

    raise Exception("\nThis codes only compatible with Linux OS!")

# check python environment compatibility
if sys.version_info[0] > 2:

    raise Exception("\nThis codes only compatible with Python 2 environment!")

# getch class for unix
class _GetchUnix:

    def __init__(self):
        
        import tty, sys

    def __call__(self):
    
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
    
        try:
    
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
    
        finally:
    
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
        return ch

# initialization
condition = 0
getch = _GetchUnix()

# execute the subprocess based on user input
while True:

    os.system("clear")
    
    # show the subprocesses status
    if (condition == 0):
    
        print("[Condition] Subprocesses is not running.")
    
    else:
    
        print("[Condition] Subprocess is running.")

    # get the user input
    print("1 = start, 2 = stop, 3 = quit.\n")
    input = getch()

    # start the subprocesses
    if (input == '1' and condition == 0):

        condition = 1
        subproc1 = sp.Popen(['python', 'b_video_client.py'])
        subproc2 = sp.Popen(['python2', 'c_distance_client.py'])
        subproc3 = sp.Popen(['python2', 'd_futaba_server.py'])

    # kill the subprocesses
    elif (input == '2' and condition == 1):

        condition = 0
        sp.Popen.terminate(subproc1)
        sp.Popen.terminate(subproc2)
        sp.Popen.terminate(subproc3)

    # quit the program
    elif (input == '3'):

        if (condition == 1):

            sp.Popen.terminate(subproc1)
            sp.Popen.terminate(subproc2)
            sp.Popen.terminate(subproc3)
            # disarming the rover
            os.system("python e_disarm_exit.py > /dev/null 2>&1 &")
            os.system("clear")
            break

        elif (condition == 0):

            # disarming the rover
            os.system("python e_disarm_exit.py > /dev/null 2>&1 &")
            os.system("clear")
            break