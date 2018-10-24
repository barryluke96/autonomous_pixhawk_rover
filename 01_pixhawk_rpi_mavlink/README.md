# Connect PixHawk based RC Rover to a Raspberry Pi

## Introduction

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/autonomous_pixhawk_rover/master/01_pixhawk_rpi_mavlink/rpi_pixhawk.png" width = "650" height = "400"/>
</p>

As explained from Ardupilot: Dev website, by connecting and configure a Raspberry Pi (RPi) so that it is able to communicate with a PixHawk flight controller using the MAVLink protocol over a serial connection, it can perform additional tasks which simply cannot be done by the PixHawk due to the processing and memory constraint.

## Guide

In this research we are going to connect Raspberry Pi as companion computer to PixHawk microcontroller, enable access to serial link connection and test if Raspberry Pi and PixHawk can communicate to each other via MAVLink protocol.

1. [Raspbian OS](https://www.raspberrypi.org/downloads/raspbian/)
    - Download the latest version of Raspbian Lite image.
2. [Write the image to SD Card](https://www.raspberrypi.org/documentation/installation/installing-images/)
    - Step by step instruction and information on how to write the downloaded image to SD Card.
3. [Configure Wi-Fi connection on Raspberry Pi](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
    - Connect Raspberry Pi to a router via Wi-Fi to avoid bounding our Rover with LAN cable. 
4. [Enabling Raspberry Pi SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)
    - Step by step instuction and information on how to enable SSH. After that use [Advanced IP Scanner](https://www.advanced-ip-scanner.com/) to find Raspberry Pi IP address and [Bitvise SSH Client](https://www.bitvise.com/ssh-client-download) to access the command line of a Raspberry Pi remotely from another computer or device on the same network using SSH.
5. [Communicating with Raspberry Pi via MAVLink](http://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html)
    - Step by step instuction and information on how to set up MAVLink. Follow the instruction until "Testing the connection" section only.
6. [Installing DroneKit-Python API](http://python.dronekit.io/develop/installation.html)
    - Alternative to MAVProxy that ease the work to interfacing PixHawk with Python code. Do not configure MAVProxy to always run to prevent oversaturating the serial connection. Note that Python 2.7 is needed on companion computer to install and run DroneKit, if installation fail execute this command instead ```sudo pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org dronekit```. Further reading
      - [DroneKit-Python API reference](http://python.dronekit.io/automodule.html): API reference for the DroneKit-Python API
      - [DroneKit-Python API example program](http://python.dronekit.io/examples/index.html#example-toc): documentation for a number of useful DroneKit-Python examples

## Alternative guide

Alternatively you can skip most of the part by simply by downloading the pre-configured [Custom Raspbian Stretch Lite](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/releases/tag/v1.0) and set up the Wi-Fi connection.
  - Network name: ardurover-dronekit
  - Username: pi
  - Password: Chobi0520

## Test run

Head over to [00_dronekit_test](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/tree/master/01_pixhawk_rpi_mavlink/00_dronekit_test) folder and download the contents on your PC first, then use Bitvise SSH Client to transfer it to Raspberry Pi via built in SFTP File Transfers. After that run it to see if DroneKit-Python API are being installed and configured properly.



## Tips

Do not power your Raspberry Pi from GPIO rail because the power are not regulated. Plus with added RPi camera and sensors, Raspberry Pi might exceed the power taken from PixHawk serial connection and forced to shutdown or refuse to boot up. Solution to this problem is by adding portable power bank to the Rover and power Raspberry Pi via micro USB.
