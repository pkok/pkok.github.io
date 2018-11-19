---
layout: post
categories:
  - thesis
---

Together with Arnoud, I decided on a clearer, more up-to-date topic for my thesis.  Also, an investigation on available datasets for this topic.


## Motivation for pre-made datasets
During last week's meeting with Arnoud, we decided to renew the thesis topic.  I will investigate the merging of [Visual-Inertial ORB-SLAM](#murartal2017visual) into [ORB-SLAM2](#murartal2017orbslam2).  One of the interesting things to see here is whether ORB-SLAM2 will increase in its accuracy.  To test my models, I want to use a dataset.  This is more preferrable for multiple reasons:
1.  Setting up synchronized sensors can be time-consuming.
2.  Extrinsic calibration is error-prone, and has to be done precisely.
3.  Designing a path through a large state space that provides a robust test for the system is hard, and can be publication-worthy on its own (see links below).
4.  For these physics-driven experiments, a lot of real-world noise parameters (for example: motion blur, IMU noise) are not implemented or only in a very simplified way.
5.  Above points only distract from the topic I try to investigate.

## Overview of used datasets
Mur-Artal and Tardós have used several datasets in their paper series.  This is an investigation of the usability of those datasets for my setting.

Datasets per paper:
- [ORB-SLAM](#murartal2015orbslam):
    - "the large robot sequence of [NewCollege](#smith2009newcollege)" ([site](http://www.robots.ox.ac.uk/NewCollegeData/)),
    - "16 hand-held sequences of the [TUM RGB-D benchmark](#sturm2012benchmark)" ([site](https://vision.in.tum.de/data/datasets/rgbd-dataset)),
    - and "10 car outdoor sequences from the [KITTI dataset](#geiger2013kitti)" ([site](http://www.cvlibs.net/datasets/kitti/))

- [Visual-Inertial ORB-SLAM](#murartal2017visual):
    - the "11 sequences recorded from a micro aerial vehicle (MAV), flying around two different rooms and an industrial environment" in the [EuRoC dataset](#burri2016euroc) ([site](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets))

- [ORB-SLAM2](#murartal2017orbslam2):
    - [KITTI dataset](#geiger2013kitti)'s closed loop sequences: 00, 02, 05, 06, 07 and 09.
    - [EuRoC dataset](#burri2016euroc)
    - [TUM RGB-D benchmark](#sturm2012benchmark)


## Technical review of datasets
Requirements of a dataset for my experiments are:
- At least 1 RGB-D source, or at least 2 synchronized grayscale/RGB cameras:
  - Does the system have a global or rolling shutter?
  - When multicamera setup: relative position.
- At least 1 source of acceleration and angular velocity:
  - Timestamps are synchronized with cameras.
  - Extrinsic calibration to cameras is preferred.
  - The update frequency should be at least 2×, preferrably 10× higher than that of the cameras.
- Ground truth information should include information about:
  - position
  - orientation
  - linear velocity
  - angular velocity
  - acceleration
  - Error models over these measurements

| Dataset    | Optical sensors | Optical frame rate | Image resolution | Shutter type | Inertial sensor | Inertial frame rate | Calibrated system | Ground truth provider | GT: frame rate | GT: position? | GT: orientation? | GT: lin.vel.? | GT: lin.acc.? | GT: ang.vel.? | GT: error models? |
|:-----------|:----------------|:------------------:|:----------------:|:------------:|:----------------|:-------------------:|:------------------|:----------------------|:--------------:|:-------------:|:----------------:|:-------------:|:-------------:|:-------------:|:-----------------:|
| [NewCollege](http://www.robots.ox.ac.uk/NewCollegeData/) | Point Grey [Bumblebee](https://www.ptgrey.com/bumblebee2-firewire-stereo-vision-camera-systems) (stereo, gray) and [LadyBug 2](https://eu.ptgrey.com/ladybug2-360-degree-firewire-spherical-camera-systems) (spherical, RGB) | 20 Hz, 3 Hz | 512×384 px | ? | N/A | N/A | y | _GPS?_ | 5 Hz | y | n | ? | ?  | ? | n |
| [TUM RGB-D](https://vision.in.tum.de/data/datasets/rgbd-dataset) | Microsoft Kinect (RGB-D) | 30 Hz | 640×480 px | ? | Microsoft Kinect (3D acceleration only) | ? | y | "high-accuracy motion-capture system" | 100 Hz | y | ? | ? | ? | ? | ? |
| [KITTI](http://www.cvlibs.net/datasets/kitti/) | 2× Point Grey [Flea 2 (FL2-14S3M-C)](https://eu.ptgrey.com/flea2-14-mp-mono-firewire-1394b-sony-icx267-4-eu) (grey), 2× [Flea 2 (FL2-14S3C-C)](https://eu.ptgrey.com/flea2-14-mp-color-firewire-1394b-sony-icx267-3-eu) (color) | 15 Hz, 15 Hz | 1384×1032 px, 1384×1032 px | global, global | [OXTS RT 3003](https://www.oxts.com/products/rt3000/) (GPS/IMU) | 100 Hz | y | _GPS?_ | 100 Hz? | y | ? | ? | ? | ? | ? |
| [EuRoC](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets) | 2× Aptina MT9V034 (grey) | 2×20 Hz | 768×480 pz | global | [ADIS16448](https://www.analog.com/media/en/technical-documentation/data-sheets/ADIS16448.pdf) (MEMS IMU, acceleration and angular rate) | 200 Hz | y | Vicon motion-capture, Leica MS50 | ? | y | y | ? | ? | ? | ? |
| Own setup | [Intel RealSense D435i](https://realsense.intel.com/depth-camera/) | RGB: 30 Hz, D: 90 Hz | RGB: 1920×1080 px, D: 1280×720 px | Global | [Intel RealSense D435i](https://realsense.intel.com/depth-camera/) | ? | ? | [ABB IRB-4600-60/2.05](https://search-ext.abb.com/library/Download.aspx?DocumentID=ROB0109EN_G&LanguageCode=en&DocumentPartId=&Action=Launch) | ? | y | y | y? | y? | ? | ? |

One interesting fact from all this data, is that only EuRoC fully complies with my wishes: it has both camera images, IMU data *and* ground truth information.  However:
1. Is 1 data set with 2 scenes, each with multiple runs, enough for this thesis? 
   Arnoud: "Only if you can show your method is better than the authors'."
2. Is it valid to view GPS data as ground truth information?  If so, KITTI is also of interest.
   Arnoud: "No, rather use optitrack."
3. Can I do without angular velocity?  If so, TUM RGB-D is also of interest.

Arnoud suggests looking at the Intel RealSense D435i, which will soon be released.  It is an RGB-D sensor with integrated IMU.  What I can see from the API is that it will most probably have no issues with time synchronization, but I haven't found whether there is any extrinsic calibration between camera(s) and IMU.  As a ground truth provider of pose, I could use the ABB robotic arm of the HvA.

**Updated with Arnoud's answers on 2018-11-19**

{% include bibliography.html keys="murartal2015orbslam,murartal2017visual,murartal2017orbslam2,smith2009newcollege,sturm2012benchmark,geiger2013kitti,burri2016euroc" %}
