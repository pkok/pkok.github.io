---
layout: post
categories:
  - thesis
---

The timestamps of observations are important for sensor fusion.  Sensor fusion finds a relation between observations of multiple sensors with respect to the time of observation.  The necessary precision of these timestamps is related to the highest update frequency.  When timestamps are made on a non-dedicated unit, timestamps have a variable offset from the time of observation.  An experimental analysis is given and possible approaches for solving this problem are presented.

First I will introduce the problem in a single-sensor setting.  After that I will point at the implications in the multisensor setting.  Then some causes of the issues will be discussed.  Possible solutions will be presented.  As a demonstration that this effect occurs in real-life systems, a short analysis of experimental results concludes this post.

$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$

## Single-sensor setting
Assume we have a single sensor \$$s\$$.  The observation of \$$s\$$ at (unobserved) time $$t$$ is denoted as $$o(s,t)$$.  Its timestamp is given by $$τ(s,t)$$.  The system receives a message $$m(s,t) = (o(s,t), τ(s,t))$$ containing both values.  In real-world systems, an observation's timestamp and the time of observation will be different.  The magnitude of this temporal offset $$d^s = τ(s,t) - t$$ does not matter much, as long as it is (fairly?) constant.  Detecting whether $$d^s$$ is constant or not is a different topic which will not be discussed here.  We will assume that observations are done with a constant interval.  In this case, $$d^s$$ can be considered constant if the standard deviation $$σ^d^s > ε$$ where $$ε$$ is some small constant, depending on the refresh rate of the sensor.  Otherwise, one might be able to model $$d^s$$ as drawn from a distribution $$D^s$$.  Note that this introduces a variance when interpolating between two observations.

The big problem here does not lay with a constant temporal offset.  If $$d$$ is constant, we still know the exact offset between events.


## Multisensor setting
Let us now consider the setting where we have *n* sensors *s^0, ..., s^n-1* with associated temporal offsets *d^0, ..., d^n-1* (we simplify the notation of a sensor *s^i* in superscripts to its identifier *i* such that *d^s^i := d^i*).  We can describe this problem of timestamping in several scenarios:

1. All offsets are constant and equal to each other: *&forall;i, j &lt; n: d^i = d^j*;
2. All offsets are constant and at least some are different from others: *&exist;i, j &lt; n: d^i &ne; d^j*;
3. All offsets are stochastic and drawn from unknown distributions;
4. Some offsets are constant, some offsets are stochastic.

I will discuss each scenario below, some a bit more thorough than the other because of my current needs.

### All offsets are constant and equal to each other: *&forall;i, j &lt; n: d^i = d^j*
The first scenario is trivial and does not increase the problem from the similar case in the single-sensor setting.  This is also the scenario least likely to occur in real-life systems, as they tend to have some sort of variation between clock speeds and processing time.

No new problems here.

### All offsets are constant and at least some are different from others: *&exist;i, j &lt; n: d^i &ne; d^j*
Consider the case where all temporal offsets are constant, but some differ from others.

Consider the diagram below.  It schematically shows a set of occurances: some events occur at time *t^0*, *t^1* and *t^2*, and are observed at the same time by sensors *s^0* and *s^1*.  The temporal offsets of their timestamps differ: *d^0* is fairly small, but *d^1* is so big that the timestamping *τ( s^1, t^0 )* occurs after *t^1*.  Symbols on the bottom line indicate the order of events: observations `o`, timestamping of sensor *s^0*'s data `■` and timestamping of sensor *s^1*'s data `▲`.

```
o(s0, t0)          τ(s0, t0)
o(s1, t0)              |         τ(s1, t0)
    +--------d0--------+             |
    +---------------d1-|-------------+
    |                  | o(s0, t1)   |      τ(s0, t1)
    |                  | o(s1, t1)   |          |         τ(s1, t1)
    |                  |     +-------|d0--------+             |
    |                  |     +-------|-------d1-|-------------+
    |                  |     |       |          |             |
    |                  |     |       |          | o(s0, t2)   |
    |                  |     |       |          | o(s1, t2)   |
    |                  |     |       |          |     |       |
----o------------------■-----o-------▲----------■-----o-------▲⋯
```

The problem here is that we need to categories the observations as belonging to the right observation.  Or, posed as a machine learning, cluster the sensor readings accordingly.  We could assume that the sequence of timestamps starts to be generated when our system has started and we do not miss readings.  This situation is sketched in the above diagram.  If it has been recorded somewhere later, there would be an extra instance of timestamping by *s^1* (the sequence on the bottom timeline `o■o▲■o▲⋯`  would be `⋯o▲■o▲■o▲⋯`).  

If we start observing the sequence of timestamps while it is being generated, associating the timestamps of the same observation can be done in several approaches:

1. Associate the *n*th occurance of each sensor's timestamp to an *n*th event.  Here we make the assumption that a consistently wrong association does not impose too much of a problem for the sensor fusion method later.
2. Associate the messages by inspecting the observations.  This should be attempted with machine learning algorithms.
3. **Any more methods?**

The special case where some *d^i* approximately equals some other *d^j* modulo refresh time is difficult to disambiguate from the former case.

For the rest of this discussion we assume that the sequence of timestamps starts to be generated when our system has started and we do not miss readings.

### All offsets are stochastic and drawn from unknown distributions
This case inherits the issues of the single-sensor stochastic setting and the multisensor constant but mutually unequal temporal offsets.  The combination of the problems makes this harder to solve than Scenario 2.  Approach 1. is surely to be invalid, as there are no guaranteed repetitive patterns.  Approach 2. will also be more problematic, as it is even noisier, while relating the events is already difficult for multimodal (or multi-viewpoint) data.  This will be outside the scope of my thesis (but it seems, without other hardware, this is the problem I am facing).

### Some offsets are constant, some offsets are stochastic
Probability theory lets non-stochastic processes be modeled just like processes that are stochastic.  For some sensor *s^i* which has a constant *d^i*, setting the standard deviation to *σ^d^i = 0* and the average to *μ^d^i = d^i* of a normal distribution has this case converted to the scenario above.

No new problems here (but other solutions might have room for optimization).


## What is causing this delay?
We will break down the (perhaps non-exhaustive) list of possible causes of the problems states above.

The act of making an observation of some event always consumes some time; information has to travel from the source to the sensor (for cameras: speed of light), the sensor needs some exposure to capture enough data (for cameras: exposure time), and stored data needs to travel to the processing unit.  Whether *t* is taken at the onset or ending of an observation does not matter for this discussion.  If the sensor supports this, data could be timestamped by the sensor itself.  This does reduce the problem heavily, but not completely.  The clocks of sensor and processing unit are probably unsynchronized, so there still is some *d^s &ne; 0*.

When the sensor cannot timestamp its own data, we will most probably be stuck with the stochastic case.  This can have several origins:

1. The transfer speed between sensor and processing unit is not constant.  The processing unit is often not dedicated to timestamping a single sensor's data.  It often has multiple processes to execute, which are given access to system resources by the CPU's [scheduler](http://en.wikipedia.org/wiki/Scheduling_(computing)).  Due to load balancing this is not predictable on a higher level.  
2. Some processing of the data happens before the timestamp can be given, for any reason.  This procedure probably does not always use the same operations.  (I cannot come up with a situation where you need to timestamp processed data; maybe storage of large amounts?)

Origin 1. can be solved in two ways, each with its use cases:
- Including a dedicated processing unit that gives a timestamp as soon as some data arrives might be desirable in cases where the size of the physical system does not matter too much.  In most cases this could be achieved with a microcontroller. (Personal problem: I don't know how to connect USB devices to microcontrollers.)
- Using a processing unit with more CPU threads can reduce the noise as will be demonstrated with the following experiment.

## Experiments
As an experiment I have recorded three ROS bags.  Information of the Xsens MTx-28A53G25 has been published to topics of type `geometry_msgs/Vector3Stamped` (magnetometer) and `sensor_msgs/Imu` (accelerometer, gyroscope and filtered orientation) with 200 Hz.  Camera images of 640×480 px have been recorded by an Logitech C920 with `sensor_msgs/Image` messages, and its accompanying `sensor_msgs/CameraInfo` has been captured as well.  Two laptops have been used: system A has USB 2.0, 8 GB RAM and a "AMD Turion(tm) II Neo K625 Dual-Core Processor" (2 threads, no hyperthreading); system B has USB 3.0, ?? RAM and a "Intel i7 ??" (4 threads, hyperthreading enabled).  The table below shows how long the recording was, how much messages of each topic have been recorded and which laptop has been used.

Bag | Recording time | #`geometry_msgs/Vector3Stamped` | #`sensor_msgs/Imu` |  #`sensor_msgs/CameraInfo` | #`sensor_msgs/Image` | Capturing system
----|----------------|---------------------------------|--------------------|----------------------------|----------------------|------------------
  1 |          28.4s |                            5681 |               5682 |                        568 |                  568 | A
  2 |          38.2s |                            7637 |               7638 |                        752 |                  753 | A
  3 |          12.3s |                            2466 |               2467 |                        246 |                  246 | B

The next few tables display the quartiles, average and standard deviation between two timestamps of each bag's `sensor_msgs/Imu` and `sensor_msgs/Image` data.  The results of the other two topics were to similar to their related topics.  All unit, where relevant, are in nanoseconds.

IMU dataset | Q1       | Q2       | Q3       | μ              | σ             | σ / μ × 100%
------------|----------|----------|----------|----------------|---------------|-------------
1           |  4567146 |  4997968 |  5096913 |  4999343.24221 | 2043642.16065 | 40.87821 
2           |  4252911 |  4996061 |  5120039 |  4999349.48461 | 2310632.19841 | 46.21866
3           |  4994869 |  4999876 |  5005121 |  5000027.23358 |   89027.84114 |  1.78055

Camera dataset | Q1       | Q2       | Q3       | μ              | σ             | σ / μ × 100%
---------------|----------|----------|----------|----------------|---------------|-------------
1              | 45519206 | 49337046 | 54509003 | 49999311.22928 | 6682960.35315 | 13.36610
2              | 45048240 | 50009256 | 55519187 | 50743640.82580 | 8182783.54824 | 16.12573
3              | 48026294 | 49272892 | 51976151 | 50008300.27755 | 1983129.63581 |  3.96560

From this we can see that using more threads does reduces the variance of the intervals. 
