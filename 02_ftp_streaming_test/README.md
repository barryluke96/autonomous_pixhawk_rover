# Stream data via FTP protocol between Raspberry Pi and PC

## Introduction

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/autonomous_pixhawk_rover/master/02_ftp_streaming_test/stream_test.PNG" width = "650" height = "500"/>
</p>

After confirming that DroneKit-Python API is installed and serial connection is configured properly, we are going to test if (Raspberry Pi + PixHawk) and PC can send data between each other via Wi-Fi connection. This will ensure that there is no problems with the hardware or software configuration and ready for the next stage of adding neural network to drive the RC Rover.

## Guide

First, before we start executing the Python programs in order to test data transfer, we need to set up the sensors, configuring Python environment and installing required Python packages via ```pip install``` command.

1. [Setting up Camera Module](https://www.raspberrypi.org/documentation/usage/camera/)
    - Enable Camera Module from ```raspi-config``` and try taking some picture by using ```raspistill -o test.jpg``` command. The picture normally saved on directory where user execute the command with test.jpg filename.
2. [Setting up distance sensor](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)
    - Step by step instruction on how to set up HC-SR04 ultrasonic sensor to be connected with Raspberry Pi.
3. [Installing correct Python environment](https://www.python.org/)
    - **PC**: Python environment needed on PC is the latest version of Python 3. You can either install it by downloading the installer from Python website or via Visual Studio Installer. 
    - **Raspberry Pi**: At the time of writing, Python 2.7 is bundled together with Raspbian Stretch Lite (Kernel 4.14). There is no need to install it separately.
4. [Installing required Python packages](https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing)
    - Note that when using pip/pip2/pip3, on Windows you will need to run Command Prompt or PowerShell as administrator. On Raspbian always execute pip install with sudo. 
    - **PC** (pip3 install package_name): numpy, pygame, pip install opencv-contrib-python.
    - **Raspberry Pi** (pip2 install package_name): picamera, RPi.GPIO, dronekit.
5. [Download required Python program on PC](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/02_ftp_streaming_test/00_pc_side)
    - Download 00_pc_side contents onto PC.
6. [Download required Python program on Raspberry Pi](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/02_ftp_streaming_test/01_rpi_side)
    - Download 01_rpi_side contents on your PC first, then use Bitvise SSH Client to transfer it to Raspberry Pi via built in SFTP File Transfers.

## Test run

We are going to execute the Python program and test the data transfer between PC and Raspberry Pi. The data we are going to transfer is video stream, distance taken from sensor and user's input via FTP protocol implemented in Python.

First we need to turn on the Rover RC controller. During my test run, in order to override these RC channels, the channels itself need to exist thus the importance to leave the RC controller on. After that do not forget to turn on the ESC switch (if exist) and press the safety switch for a few seconds to allow arming.

After that on PC side, from Command Prompt or PowerShell, change directory to where the 00_pc_side is located and execute a_subprocess_pc.py only. Run this command ```python3 a_subprocess_pc.py```. After that select [1] to start the subprocess.

Then on Raspberry Pi side, change directory where the 01_rpi_side is located and execute a_subprocess_rpi.py only. Run this command ```python2 a_subprocess_rpi.py```. After that select [1] to start the subprocess.

By refering on the image above, "pygame window" and "Video stream" window should appear. The distance sensor reading should appear on Command Prompt or PowerShell window. To move the Rover, use arrow keys on keybaord. Every registered keystroke will move the Rover for 0.4 second.

## Tips

Before you execute the Python programs, it's better to run previously downloaded c_full_rc_reading.py and find the highest, lowest and middle reading for channel 3 (motor) and channel 1 (steering servo). Use this as reference to find preferable value to override these channels on d_futaba_server.py.

## Troubleshooting

If Rover motor forward movement feel too slow, jittery or not responding at all, it mean the pre-setted value for Channel 3 override is too low. Open d_futaba_server.py and set global variable for "forward" higher. As for backward movement, if it exhibit the same problem as stated before, set global variable for "backward" lower.

For the steering servo, do not set the channel 1 override too close with maximum or minimum values noted from c_full_rc_reading.py otherwise the Rover might accidentally enter the armed or disarmed state.