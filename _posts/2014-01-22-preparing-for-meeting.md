---
layout: post
categories:
  - thesis
  - augmented reality
---

As a preparation for the first meeting with all supervisors, Toby and I discussed several options of combinations of papers to base my thesis on, and made a (semi-)concrete proposal.

## Parallel Tracking and Mapping ##
We like the idea of parallel tracking and mapping (PTAM), first described by [Klein et al.](#klein2007ptam). It is an extension of simultaneous localization and mapping (SLAM) from the domain of robotics, made available for AR.  In many cases, AR systems require more pose updates per second than robotic systems, as AR systems must maintain a illusion, which is perceived continuously.  In SLAM, during every round/frame of the algorithm, localization/tracking and mapping are done sequentially.  While tracking can be done relatively fast, mapping takes a lot of time, and most of the times does not result in a big improvement of the map's precision.

[Klein et al.](#klein2007ptam)'s PTAM takes another approach to this problem.  Here, a single thread for tracking and another thread for mapping exist.  The tracking routine occassionally sends a frame to the mapping routine.  The frame is accepted by the mapper if "Tracking quality must be good; time since the last keyframe was added must exceed twenty frames; and the camera must be a minimum distance away from the nearest keypoint already in the map."  This parallelization of the two procedures allows for real-time tracking and slow but precise mapping, which does not interfere with the tracking, especially now that basic computing devices (smartphones, tablets, notebook and desktop PCs) contain multicore processors.

## Inertial measurement unit ##
An inertial measurement unit (IMU) allows for scenarios where no reliable features can be extracted from the camera.  Most often, this is because the camera images are blurred because of motion, or because there is a feature-poor environment ([Ta et al.](#ta2013monocular) mentions office hallways).  Combining readings of several sensors is not trivial, and subject of active research.

[Bleser et al.](#bleser2008advanced) investigates four different models where different quantities of the IMU are combined in different ways.  They combine the observations by means of an (extended) Kalman filter.  The first model, *gyro*, only includes gyrometer data (high in process noise).  The second model, *gravity*, includes extra accelerometer data to stabilize images.  The third model, *acc*, includes the full accelerometer data as observation.  The fourth and final model, *acc input*, does not include the accelerometer data as observation data, but models it as odometry data for the motion model of the Kalman filter.  This results in a simpler expression.  In their evaluation, the first two and final two methods have comparable root mean square prediction errors in pixels.  There is a big difference in performance between the first two and final two methods if there are fast motions.  In the fast motion case, the fourth model outperforms all.

## Continuous time processes ##
Because IMUs have a higher refresh rate than cameras ([Caarls](#caarls2009pose)' machinery has 100 Hz and 25 Hz; camera images must be processed which takes time as well), more pose updates (and thus a more precise estimate of the true pose) can be obtained by being able to consider IMU observations separately from camera features observations from time to time.  For one, this would mean that the update intervals cannot be assumed to be equal anymore.  The second point is that the filters combining the data should be able to only sometimes consider the camera images, as not at every IMU update new camera data is available.  Both of these problems are discussed by [Caarls](#caarls2009pose) and can be handled by his *plug-in Kalman filter*.

## Initial approach and evaluation ##
For now, we suggest to look at an approach that transfers Bleser's method to the PTAM framework.  When there is time left/performance to gain, we will consider the plug-in Kalman filters to fully use the IMU.

It would be nice if it is possible to have a ground truth about the system's 6D pose.  Arnoud suggested to use Delft's [optitrack](http://www.naturalpoint.com/optitrack/systems/#motive-tracker) system for another project.  We have looked, but it seems it is quite difficult to place in a new location.  Another option is to use a synchronized, high-speed camera setup (3 cameras? 4? 5?) that will track a cube with markers on all sides.  Most systems do not evaluate their performance based on the precision of localization.  Some evaluate the root mean square prediction error in pixels of a point in the camera (such as Bleser), while Ta evaluates its system by overlaying the estimated trajectory over the actual map.

---

## Older todos ##
In addition, a small update on the todos mentioned in the previous entry.

### Practical todos ###

1. **Read out an IMU with a programming language or to a file:** Done. I got a log file of the IMU in a stationary mode for a bit more than 24 hours.
2. **Track a camera's distance with respect to a marker:**
3. **Perform a simple kind of fusion between the tracked position and the IMU data:** Not done, but the basic setup is fully described above.

### Theoretical todos ###

4. **Read in on Kalman filters:** Done; finished the Kalman filter related videos of Cyrill Stachniss's lectures.  I heard from Auke there is a set of [Sebastian Thrun on Udacity](https://www.udacity.com/course/cs373), and I will try to watch that one as well.
5. **In [Caarls](#caarls2009pose)' PhD thesis read up on specific Kalman filters and "continuous time processes":** Done, while it still is a bit confusing.
6. **Collect papers on IMU -- (stereo)camera fusion:**  Firstly, I contacted Leo Dorst on an [unpublished paper](#dorstCombining).  He wrote a tutorial on combining orientation measurements/estimates "from averaging and interpolation to filtering".  [Ta et al.](#ta2013monocular) implemented PTAM with minor changes for usage on the Parrot's AR.Drone 2.  Its results are not promosing, but their way of fusing IMU readings (they make a factor graph and optimize it during runtime) is interesting, however slow with a tracker of 10 fps.  As described above, [Bleser et al.](#bleser2008advanced) use a method where they include IMU readings as an input for the AR system.

{% include bibliography.html keys="dorstCombining,caarls2009pose,ta2013monocular,bleser2008advanced,klein2007ptam" %}
