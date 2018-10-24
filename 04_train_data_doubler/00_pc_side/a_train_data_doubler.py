#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules being used in the program
from datetime import datetime
from numpy import load
import numpy as np
import time
import glob
import cv2
import sys
import os

# specify directory path and file name
folder = "00_training_data"
subfolder = "00_unfiltered_image"
file = "label_array.npz"

# check os compatibility
if os.name != 'nt':

    print ("\nThis code is only compatible with Windows OS!")
    exit()

# check python environment compatibility
if sys.version_info[0] < 3:

    print ("\nThis code is only compatible with Python 3 environment!")
    exit()

# if folder doesn't exist end the program
if not os.path.exists(folder):

    print ("\nFolder 00_training_data, where the training data supposedly located does not exist!")
    exit()

# if subfolder doesn't exist end the program
if not os.path.exists(folder + "/" + subfolder):

    print ("\nFolder 00_training_data/00_unfiltered_image does not exist!")
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

# get the current time
timestr = datetime.now().strftime("%Y%m%d%H%M%S%f")

# depend on user input doubler will start
while True:

    os.system("cls")

    # get the user input
    print ("This program double the data needed to train the machine learning.")
    print ("Remember that this program is only usable once for single batch of training data.")
    print ("Running it more than once will cause machine learning to suffer from overfitting!\n")
    print ("1 = doubler, 2 = quit.\n")
    input = getch()

    # start the doubler
    if (input == b'1'):

        # load the filtered images into an array
        training_filtered = glob.glob(folder + "/*.jpg")
        image_filtered = np.array([cv2.imread(file) for file in training_filtered])
        # load the original images into an array
        training_original = glob.glob(folder + "/" + subfolder + "/*.jpg")
        image_original = np.array([cv2.imread(file) for file in training_original])
        # find how many images exist inside image_filtered
        filtered_size = len(image_filtered)
        # find how many images exist inside image_original
        original_size = len(image_original)
        print(original_size, "original images need to be flipped.")
        print(filtered_size, "filtered images need to be flipped.")

        # flip the filtered images and save it to designated folder
        for x in range(filtered_size):

            # get the current time
            timestr = datetime.now().strftime("%Y%m%d%H%M%S%f")
    
            # flip the image and save
            flipped_filtered = np.flip(image_filtered[x], 1)
            cv2.imwrite(folder + "/" + timestr + '.jpg', flipped_filtered)

        # flip the original images and save it to designated folder
        for y in range(original_size):

            # get the current time
            timestr = datetime.now().strftime("%Y%m%d%H%M%S%f")
    
            # flip the image and save
            flipped_original = np.flip(image_original[y], 1)
            cv2.imwrite(folder + "/" + subfolder + "/" + timestr + '.jpg', flipped_original)

        # load the tuple from .npz file
        original = load(folder + "/" + file)
        lst = original.files
        for item in lst: 

            a = (original[item])

        print(len(a), "arrays of tuple need to be flipped.\n")
        # flip the tuple
        b = np.flip(a, 1)
        # concatenate tuple a and b
        c = np.concatenate((a, b), 0)
        np.savez(folder + "/" + file, train_labels = c)

        print ("Doubler executed successfully, will quit in 5 seconds.")
        time.sleep(5)
        os.system("cls")
        exit()

    elif (input == b'2'):

        print ("Doubler canceled and no data were changed, will quit in 5 seconds.")
        time.sleep(5)
        os.system("cls")
        exit()