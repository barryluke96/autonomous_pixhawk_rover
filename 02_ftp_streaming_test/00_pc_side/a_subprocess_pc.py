#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules being used in the program
import subprocess as sp
import sys
import os

# check os compatibility
if os.name != 'nt':

    print ("\nThis codes only compatible with Windows OS!")
    exit()

# check python environment compatibility
if sys.version_info[0] < 3:

    print ("\nThis codes only compatible with Python 3 environment!")
    exit()

# getch class for windows
class _GetchWindows:

    def __init__(self):

        import msvcrt

    def __call__(self):

        import msvcrt
        return msvcrt.getch()

# initialization
condition = 0
getch = _GetchWindows()

# execute the subprocess based on user input
while True:

    os.system("cls")

    # show the subprocesses status
    if (condition == 0):

        print("[Condition] Subprocesses is not running.")
    
    else:
    
        print("[Condition] Subprocess is running.")

    # get the user input
    print("1 = start, 2 = stop, 3 = quit\n")
    input = getch()

    # start the subprocesses
    if (input == b'1' and condition == 0):
        
        condition = 1
        subproc1 = sp.Popen(['python3','b_video_server.py'])
        subproc2 = sp.Popen(['python3','c_distance_server.py'])
        subproc3 = sp.Popen(['python3','d_futaba_client.py'])

    # kill the subprocesses
    elif (input == b'2' and condition == 1):

        condition = 0
        sp.Popen.terminate(subproc1)
        sp.Popen.terminate(subproc2)
        sp.Popen.terminate(subproc3)

    # quit the program
    elif (input == b'3'):

        if (condition == 1):

            sp.Popen.terminate(subproc1)
            sp.Popen.terminate(subproc2)
            sp.Popen.terminate(subproc3)
            os.system("cls")
            break

        elif (condition == 0):
            
            os.system("cls")
            break