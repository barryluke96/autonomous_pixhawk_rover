## Introduction

List of Python programs to be executed on PC in order to collect user inputs from keyboard and picture from Raspberry Pi Camera Module the moment input is received.

1. [a_data_collection.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/03_collect_train_data/00_pc_side/a_data_collection.py)
    - Crop and collect images every time a direction is input by the driver. Images will be saved at 00_training_data folder at the end of data collection.
    - Record user inputs as an array, each new one being vstacked below the previous. Compiles to npz file at the end.
2. [b_futaba_client_interface.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/03_collect_train_data/00_pc_side/b_futaba_client_interface.py)
    - Extension module for a_data_collection.py program to control the Rover (PixHawk) via TCP protocol passed through Raspberry Pi.
3. [c_open_npz.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/03_collect_train_data/00_pc_side/c_open_npz.py)
    - Python program that can open and view .npz file contents. Not necessarily needed to collect data but useful to confirm that the data stored as tuple in npz is correct.