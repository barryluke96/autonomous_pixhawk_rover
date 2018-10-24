## Introduction

List of Python programs to be executed on PC in order to test data transfer via FTP protocol. Do note that Firewall clearance for Python is needed in order to transmit or receive data.

1. [a_subprocess_pc.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/00_pc_side/a_subprocess_pc.py)
    - Act as main program that utilize subprocess in order to run all the programs below.
2. [b_video_server.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/00_pc_side/b_video_server.py)
    - Receive the video from Camera Module.
3. [c_distance_server.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/00_pc_side/c_distance_server.py)
    - Receive distance length from distance sensor.
4. [d_futaba_server.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/00_pc_side/d_futaba_client.py)
    - Send user input to Raspberry Pi.