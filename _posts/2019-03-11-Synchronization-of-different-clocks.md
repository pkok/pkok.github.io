---
title: 
layout: post
categories:
  - thesis
---

How do I synchronize signals with timestamps from 3 different clocks?

Each capturing device (the robotic arm, the RealSense sensor, and the Structure sensor) has its own internal clock.  In [October 2014]({% post_url 2014-10-16-Why-ROS's-timestamps-are-not-enough %}) I already discussed the different forms of difficulties in sensor timestamping, and argued in favor of sensor-local timestamping.  In this discussion, I presumed a common clock signal for each sensor.  That was reasonable to do back then, because these sensors could physically be wired to an external clock signal.  

However, this is not the case in this setup.  The two sensors are USB-devices, which cannot be configured to receive a clock input, nor can their internal clock periodically be reset.  The same goes for the robotic arm.

A solution is the following logging schedule:

- The data collector pc will log to $$N = \|\mbox{capturing devices}\|$$ files through $$N + 1$$ logging threads.
- Each thread with ID $$\in 0 \leq n < N$$ will write, in a standardized format, to its corresponding log file.
- Thread with ID $$N$$ will write its own observed timestamp to each of the $$N$$ files on a specified frequency.

By doing this, a rough version of time alignment can be performed.

**Question:** Would logging the data collector's clock value at the moment of calling the callback of each of the $$0 \leq n < N$$ threads be sufficient?
