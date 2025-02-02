# Bike Speed and Distance Logger
---


## Overview

script for logging average speed, instantaneous speed, and total distance traveled by a bike.
It uses a hall effect sensor to detect wheel rotations and calculates the speed and distance based on the wheel's circumference.

## Requirements

* Microcontroller with uPython support (e.g., Raspberry Pi, ESP32)
* Hall effect sensor module

## Usage

1. Connect the hall effect sensor to the microcontroller.
2. Run the script.
3. The script will log the average speed, instantaneous speed, and total distance traveled to `log.txt` every time the wheel completes a rotation.

## Connections
* `GND -> GND`
* `VCC -> 3V3`
* `D0  -> GPIO5`

## Results
![sample.gif](https://github.com/Qvme/bicycleStats/blob/fe53ad084d41ab1b3f51f927b445a7a7a2a54a53/assets/sample.gif?raw=true)
