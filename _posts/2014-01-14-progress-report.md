---
layout: post
title: Progress report
---

A small report on what I have done in a little less than a week's time.

### Practical todo's ###
1. **Read out an IMU with a programming language or to file:**
   I wrote an [Arduino sketch]({{site.url}}/assets/arduino_imu/tempimu.ino), based on code from Pololu's example programs for its [gyroscope](https://github.com/pololu/lsm303-arduino/blob/master/LSM303/examples/Serial/Serial.ino) and [accelerometer and magnetometer](https://github.com/pololu/l3g-arduino/blob/master/L3G/examples/Serial/Serial.ino) boards.  I hooked up the Arduino with an [LM35DZ temperature sensor](http://www.ti.com/lit/ds/symlink/lm35.pdf), as the IMU's sensitivity depends on the temperature.  Data is read out by a [simple Python script]({{ site.url }}/asset/arduino_imu/serial_reader.py) which writes it to file.  

   Currently, I am reading out data while a breadboard with both sensors is stuck to a wall, such that it should be very stable.  Data between the several sensors needs to be fused; the IMU chip doesn't do this for you.

2. **Track a camera's distance with respect to a marker:** 
   I installed ArUco and will work on this point after this post.

3. **Perform a simple kind of fusion between the tracked position and the IMU data:**
   Not done yet. 

### Theoretical todo's ###
4. **Read in on Kalman filters:**
   I have watched and done the homework for several of the 2012 lectures of  
[Cyrill Stachniss](http://ais.informatik.uni-freiburg.de/teaching/ws12/mapping/).  I now understand the "ordinary" Kalman filter (KF), extended Kalman filter (EKF), unscented Kalman filter (UKF), extended information filter (EIF), and sparse extended information filter (SEIF).  I will write a part for my thesis about the KF methods soon, which might be included in my final thesis.

5. **In [Caarls](#caarls2009pose)' PhD thesis, read up on specific Kalman filters and "continuous time processes":**
   Nothing done yet.

6. **Collect papers on IMU -- (stereo)camera fusion:**
   Nothing done yet.

{% include bibliography.html keys="caarls2009pose" %}
