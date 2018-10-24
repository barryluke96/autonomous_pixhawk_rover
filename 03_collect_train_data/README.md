# Data collection for post-collect processing or machine learning training

## Introduction

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/autonomous_pixhawk_rover/master/03_collect_train_data/training_data.png" width = "650" height = "500"/>
</p>

Create test track for Rover to drive on and by using this Python programs, collect the images taken from Raspberry Pi Camera Module and user input taken from keyboard when driving. The data saved will be saved on  00_training_data for post-collect processing or machine learning training.

## Guide

First, copy required Python programs [00_pc_side](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/03_collect_train_data/00_pc_side) to PC and [01_rpi_side](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/03_collect_train_data/01_rpi_side) to Raspberry Pi. If Python programs used from [02_ftp_streaming_test](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/02_ftp_streaming_test) test run still exist on Raspberry Pi, there is no need to copy the new one. 

## Collecting data

In order to run the Python programs and start collecting data, on Raspberry Pi side run [a_subprocess_rpi.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/03_collect_train_data/01_rpi_side/a_subprocess_rpi.py) by following the guide from [02_ftp_streaming_test](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/02_ftp_streaming_test). After that on PC side, run [a_data_collection.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/03_collect_train_data/00_pc_side/a_data_collection.py).

Place Rover on test track and start driving by pressing single arrow key at a time. Every time the user press the arow key, the data will be saved in folder 00_training_data (if folder 00_training_data does not exist, it will be generated automatically).

If you want to take a break and continue later, press [q] key and it will stop. After that when you want to resume it again simply rerun the programs and it will automatically continue stacking the data on previously saved data.

After the training was completed and the user want to confirm the data saved on .npz file, use [c_open_npz.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/03_collect_train_data/00_pc_side/c_open_npz.py).

## Tips

In a situation where the training collection Python programs suddenly fail and stop (i.e. FTP protocol connection dropped thanks to unstable WI-Fi connection), simply rerun the program again. It will automatically remove broken saved data from temporary folders and continue stacking the saved data normally.