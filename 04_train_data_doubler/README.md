# Doubling saved training data

## Introduction

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/autonomous_pixhawk_rover/master/04_train_data_doubler/data_doubling.PNG" width = "700" height = "400"/>
</p>

Double the training data by flipping/mirroring saved images and input array to y-axis. This will create a mirror to the original data.

## Guide

First, copy required Python programs [00_pc_side](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/04_train_data_doubler/00_pc_side) to PC. After that copy 00_training_data folder into the same directory as [a_train_data_doubler.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/04_train_data_doubler/00_pc_side/a_train_data_doubler.py) Python program.

## Doubling the data

Simply execute [a_train_data_doubler.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/04_train_data_doubler/00_pc_side/a_train_data_doubler.py) Python program and follow the instructions. Remember that this Python program is usable once for single batch of training data. Running it more than once will cause machine learning to suffer from overfitting thanks to duplicated training data.