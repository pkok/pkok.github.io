---
title: First attempt with RealSense D435i
layout: post
categories:
  - thesis
  - sensor/realsense
---

Installed the drivers for RealSense D435i, and `realsense-view` works directly.

Installation under Ubuntu 16.04 with Linux kernel 4.15.0-43.  I followed the steps as instructed in [Intel's installation walkthrough](https://github.com/IntelRealSense/librealsense/blob/4c8fe6dd382fb7476fb3ce10cdf2eac1f264db14/doc/distribution_linux.md):

```sh
sudo apt-key adv --keyserver keys.gnupg.net --recv-key C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C8B3A55A6F3EFCDE
sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo xenial main" -u
sudo rm -f /etc/apt/sources.list.d/realsense-public.list
sudo apt-get update
sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils
sudo apt-get install librealsense2-dev
sudo apt-get install librealsense2-dev
```

Afterwards, I rebooted my laptop and started `realsense-viewer`, and it just worked.  Data collected through the GUI is shown below.

<figure>
![Depth image of my cat, captured by the RealSense D435i](/assets/img/d435i_cat_depth.png)
![Color image of my cat, captured by the RealSense D435i](/assets/img/d435i_cat_color.png)
<figcaption>
A picture of my cat, captured with the RealSense D435i and its GUI, `realsense-viewer`.  First: depth image.  Second: 'regular' color image.  Notice on the second image the little red dots on the table leg, which indicate at least a structured light approach built into the D435i.
</figcaption>
</figure>

Some errors did occur though.

## No accelerometer data

This problem manifests in two ways.

Firstly, when recording a rosbag through the `realsense-viewer` GUI, the `/device_0/sensor_2/Accel_0/imu/data` topic has 0 messages.   The `/device_0/sensor_2/Gyro_0/imu/data` topic contains `sensor_msgs/Imu` messages, but the `linear_acceleration` field is always set to `[0 0 0]`.

The second way shows up in the `realsense-viewer` GUI.  When toggling on the "Motion Module" in `realsense-viewer`, two windows should appear, displaying Gyro and Accel stream visualizations.  The Accel window always displays an error: "*⚠️ No Frames Received!*" on a white background.  Sometimes, the Accel window does not display at regular width, but is reduced to a really narrow window.  Widening the window shows the same thing as a "regularly sized" window.


## Mysterious device error

When toggling off the "Motion Module" in `realsense-viewer`, an error message appears sometimes:

```
Backend in rs2_stop(sensor:0x1a0ab80):
Failed to enable_sensor /sys/devices/pci0000:00/0000:00:14.0/usb4/4-1/4-1:1.5/0003:8086:0B3A.0008/HID-SENSOR-2000e1.4.auto/enable_sensor Last Error: No such file or directory
```

Not sure what this means.  Not sure about the conditions to get this error.

I inspected the exported configuration file `custom.json` to see if there is any setting about the IMU settings.  I found nothing yet.  Just assuming this is a fluke for now.

## To do next time
- Get the [ROS wrapper for the D435i](https://github.com/intel-ros/realsense) working
