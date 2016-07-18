---
layout: page
text: Software writing plan
---

Following components are needed.  They are indicated with their names in software:

* Build a Gazebo world for generating data
    : _File:_ `gazebo/my.world`
    : _Status:_ 
    * Includes a ground plane
    * Includes a light source
    * Includes a single ArUco board, or a set of them
        : _File:_ `gazebo/models/aruco_board/`
        : _Status:_ **Single board finished**
        * Single board should have multiple markers on it
        * Single board should stand stable
        * Single board should be of known size
    * Includes a camera-IMU
        : _File:_ `gazebo/my.world`
        : _Status:_ Dependent on plugins
        * Contains a camera
        * Contains an IMU
        * Camera-IMU moves around with a little bit of noise
            : _File:_ `gazebo/animation/animation.cc`
            : _Status:_ **Finished**
            - Move in an 8-shape in the _x,y_-plane
            - Add Gaussian noise in movement, orientation at every timestep
            - Library: `gazebo/lib/libanimation.so`
        * Data streams are synchronized
            : _File:_ `gazebo/model_control_plugin.cc`
            : _Status:_ **Finished**
            - Assumption: Camera updates will occur less often than IMU updates. 
            - Conclusion: read data from IMU and system when the camera is updated.
        * Data is logged in some way:
            : _File:_ `gazebo/model_control_plugin.cc`
            : _Status:_ **Finished**
            - When camera is updated collect data from several modules, and write each to file:
                - Camera: timestamp, image (image itself to file; record image file name);
                - IMU: timestamp, orientation, angular velocity, linear acceleration
                - Model: world pose, world angular velocity, world linear acceleration, world angular acceleration, world linear velocity
            - Library: `gazebo/lib/libmodel_control_plugin.so`
* Recorded data can be played back
    : _File:_ `log_file.py`
    : _Status:_ **Finished**
* Re-record data with modifications
    : _File:_ `log_file.py`
    : _Status:_ **Finished**
* Blur images according to own model, papers?
    : _File:_ `blur_images.py`
    : _Status:_ own model is **finished**
    * Blur images according to [my own idea]({% post_url 2015-02-24- %}):
        : _Status:_ **Finished**
    * Optional: blur images according to a paper.
        : _Status_: Not Started
* Feed recorded data to any KF
* Implement EKF
* Implement Bleser's filter
* Implement GPEKF


Synchronize camera and IMU data streams in Gazebo.
: **File:** `src/gazebo_plugins/sensor_sync.cc` 
: **Status:** Finished
: **Implemented as:** Gazebo Sensor Plugin

Collect Gazebo data (`gazebo::msgs::Pose`, `gazebo::msgs::ImageStamped`, `gazebo::msgs::IMU`) in protobuf archive.
: **File:** `src/gazebo_plugins/sensor_sync.cc` 
: **Status:** Needs testing
: **Implemented as:** Gazebo Sensor Plugin

Blur images in protobuf archive, extract `gazebo::msgs::Pose` and add that to the archive.
: **File:**
: **Status:**
: **Implemented as:**

Process `gazebo::msgs::IMU` and `gazebo::msgs::Pose` in Bleser's filter to obtain new `geometry_msgs::Pose`, store in ROS bag.
: **File:**
: **Status:**
: **Implemented as:**
