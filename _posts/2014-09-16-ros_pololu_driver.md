---
layout: post
categories:
  - ROS
  - Arduino 
---

I will write a ROS wrapper for the Pololu MinIMU-9 v2 (L3GD20 and LSM303DLHC Carrier). More info inside.

The [Pololu MinIMU-9 v2](http://www.pololu.com/product/1268) comes with a driver for reading data in serial from the [L3GD20](https://github.com/pololu/l3g-arduino) accelerometer and gyroscope, and the [LSM303DLHC](https://github.com/pololu/lsm303-arduino) magnetometer.  There is a whole range of products these drivers work with, but the ROS driver/bridge will only be tested for the MinIMU9 v2.  My primary need is for the L3GD20 to work, so the focus will be on that for now.

This work will be in my [pololu_imu](http://github.com/pkok/pololu_imu) ROS package.  It will depend on [rosserial](http://wiki.ros.org/rosserial) and [rosserial_arduino](http://wiki.ros.org/rosserial_arduino).
