#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
from numpy import load

# specify file location and name
folder = "00_training_data"
file = "label_array.npz"

# load the file into data
data = load(folder + "/" + file)
lst = data.files

# printout the content
for item in lst:
    print(item)
    print(data[item])