# Build Custom PixHawk based RC Rover

## Introduction

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/autonomous_pixhawk_rover/master/00_build_pixhawk_rover/pixhawk_rover.png" width = "650" height = "400"/>
</p>

As explained from Ardupilot: Rover website, Rover is an advanced open source autopilot for guiding ground vehicles and boats. It can run fully autonomous missions that are defined using mission planning software or pre-recorded by the driver during a manual run.

## Guide

In this research we are going to build our own custom PixHawk based RC Rover, configure it to bypass pre-arming GPS check for indoor test run and set the driving mode to "Manual" for direct control without any correction.

1. [Start page](http://ardupilot.org/ardupilot/index.html)
    - Ardupilot mainpage on building RC vehicle.
2. [Building custom RC Rover](http://ardupilot.org/rover/docs/apmrover-setup.html)
    - Step by step instruction and information on how to build PixHawk based RC Rover.
3. [Tuning and calibrating RC Rover](http://ardupilot.org/rover/docs/rover-first-drive.html)
    -  Set up required for first drive including basic tuning to get vehicle driving reasonably well.
4. [Mode for override RC Rover control](http://ardupilot.org/rover/docs/manual-mode.html)
    - Set the default mode to manual for direct control to vehicle’s throttle and steering output without any correction.
5. [Disable pre-arm safety check](http://ardupilot.org/copter/docs/prearm_safety_check.html#disabling-the-pre-arm-safety-check)
    - Disable it in order to bypass pre-arming GPS check before arm sequence start.

## Reference

Refer to [parameter](https://github.com/hafiz-kamilin/autonomous_pixhawk_rover/blob/master/00_build_pixhawk_rover/2018-06-05.param) or simply load the param file above into PixHawk via Mission Planner and initiate calibrating to make sure Rover is configured to bypass pre-arming GPS check and set to Manual Mode.

## Tip

When you're choosing battery to power your Rover, it is always better to go for Ni-MH battery rather than going for typical Ni-Cd battery used in RC car. Reason for this is Ni-Cd battery take longer time to charge, low milliampere hour (mah) and require post-run maintenance by draining all the power left to prevent memory effect (technically Ni-MH also exhibit memory effect to a certain degree but periodically discharging and followed with full charge will eliminate the problem). Lithium-ion battery also can be an alternative to Ni-MH and Ni-Cd battery but you will need to find one that support high discharge rate. Last but not least, always go for a proper battery designed for RC car.
