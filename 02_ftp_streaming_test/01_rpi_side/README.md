## Introduction

List of Python programs to be executed on Raspberry Pi in order to test data transfer via FTP protocol.

1. [a_subprocess_rpi.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/01_rpi_side/a_subprocess_rpi.py)
    - Act as main program that utilize subprocess in order to run all programs below.
2. [b_video_client.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/01_rpi_side/b_video_client.py)
    - Send the video from Camera Module.
3. [c_distance_client.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/01_rpi_side/c_distance_client.py)
    - Send distance length from distance sensor.
4. [d_futaba_server.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/01_rpi_side/d_futaba_server.py)
    - Receive user input from the PC and translate it to specified values in order to move the servo and motor.
5. [e_disarm_exit.py](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/02_ftp_streaming_test/01_rpi_side/e_disarm_exit.py)
    - Ensure the PixHawk is properly disarm to prevent the user accidentally pressed the Futaba T10J remote control.
