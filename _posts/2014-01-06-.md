---
layout: post
title: Thesis intro
categories: 
- thesis
- augmented reality
---

For my Master's thesis I will investigate marker-less tracking of a head-mounted display with a particle filter for augmented reality applications.  Sensor fusion will be applied to an inertial measurement unit and a stereocamera.

*Augmented reality* (AR) research tries to fuse a user's perception of the real world together with another virtual world.  This might be done for one's hearing, smell or taste, but most often the focus is on *augmenting* what is seen and felt.  In my research, I will focus on visual augments which will be presented by a *head mounted display* (HMD).

<figure>
<img src="/assets/img/sword_of_damocles.jpg" title="The first HMD">
<img src="/assets/img/toby.png" title="My supervisor with an HMD">
<figcaption>
Examples of head-mounted displays. Top: The <a href="#tamura2002steady">Sword of Damocles</a>, a virtual reality system with the first HMD, comes from the 1960s.  Bottom: My supervisor <a href="http://www.3me.tudelft.nl/en/about-the-faculty/departments/biomechanical-engineering/organisation/people/hijzen/toby-hijzen/">Toby</a> wearing one of <a href="http://cybermindnl.com">Cybermind's</a> <del>toys</del> research devices.
</figcaption>
</figure>

Adding the virtual objects to the display is not the biggest challenge; integrating them as if they really belong in that setting and allowing the user to interact with them is the hard part.  One such challenge is knowing the 3D pose of the system in the real world, such that the augments can be placed on a static real-world position.  Keeping this model up-to-date is essential to sustain the user's belief of a really fused percept.


<figure>
<img src="/assets/img/aibo_homestation.jpg" title="AIBO on its charger">
<figcaption>
The AIBO ERS-7's charger came with two markers, so that the robot could determine its distance and orientation with respect to the charger. <small>Image source: <a href="http://www.conscious-robots.com/en/download-./resources-for-aibo/aibo-ers-7-station-pole-image-pattern/details.html">Conscious Robotics</a>.</small>
</figcaption>
</figure>


To make this problem (slightly) easier, the real-world environment can be prepared with fiducial markers.  Tracking your position in that way is a solved problem, and the technology is used in consumer products, such as the Nintendo 3DS's [AR cards](http://youtu.be/43uSXA9qUe8). 

A big disadvantage of this approach is the need for preparation; new environments have to be enhanced with markers before the augments can be provided.  When the target of your augments is mobile, a marker should be attached to it.  In many cases this is infeasible or undesired, such as in many medical and military applications.


## Marker-less tracking
Earlier in my Master's study I have done some projects on self-localization within the RoboCup Standard Platform League (SPL), which resulted in [this](#gudi2013feature) and [this](#dekok2013victoria) project reports and a [publication](#methenitis2013orientation).  RoboCup SPL is a league of robotic soccer, where all robots of all teams are made of the same hardware.  The league uses the small NAO robot, and play on a field with set dimensions and colors.  Finding your pose on the field is done without any true markers; while there are specific landmarks, they are unique or result in only a little gain of information.  Placing markers in or around the field (such as team mates with easy-to-recognize shirts) is seen as cheating.

<figure>
<img src="/assets/img/cheesy_stock_nao.jpg" title="Cheesy stock photo of the NAO H25">
<figcaption>
Random dudes doing science with a NAO H25.  This is the small humanoid which is used in RoboCup SPL competitions.  <small>Image source: <a href="http://www.aldebaran-robotics.com/en/Discover-NAO/images-gallery.html#">Aldebaran Robotics</a>.</small>
</figcaption>
</figure>

However, in the SPL scenario, the map is already known.  In an unknown environment, the paradigma of *simultaneous localization and mapping* (SLAM) is more appropriate.  There is a lot of literature on SLAM, mainly coming from robotics.  In both the solely localization and SLAM problems, the robot makes an estimate of its displacement based on its performed action ("according to my wheel odometry, I moved one meter straight ahead, so I probably moved that much").  Depending on the mode of movement (precision of odometry) and the environment (for instance slipperiness, obstacles), this estimate can be off.  This estimate is enhanced by observations of other sensors, such as laser rangefinders and cameras.


## Sensors
In the case of AR, no estimate of odometry is available to the system; there is no sufficient predictor available to model the user's movement *without extra sensors*.  Adding an *inertial measurement unit* (IMU) to the sensors of the HMD, and we might be able to provide some basic information as input.  IMUs contain an accelerometer, gyroscope and magnetometer, which provides a single reading by means of sensor fusion.  A nice introductory talk is available [on YouTube](http://youtu.be/C7JQ7Rpwn2k).  These sensors provide you with accurate measurements of acceleration (accelerometer) and rotation (gyroscope).  The magnetometer lets you correct the rotational drift.

Further observations will be made with two cameras for stereovision.  Together with the odometry this should allow for pretty accurate pose estimates.  How all this information is going to be combined is my main topic of research.  This will most likely be done with a [marginalized particle filter](#schon2005marginalized).  Directly reusing the IMU observations should be avoided, but we will investigate a way of using this data optimally in this stage as well.


## Thesis details
Because of university requirements, I have several supervisors:

- [Toby Hijzen](http://www.3me.tudelft.nl/en/about-the-faculty/departments/biomechanical-engineering/organisation/people/hijzen/toby-hijzen/) is an employee of [Cybermind](http://cybermindnl.com), a Dutch company specializing in high-end HMDs.  Toby is my daily supervisor.  He is based in [Delft University of Technology's](http://tudelft.nl) [Biorobotics Lab](http://www.dbl.tudelft.nl/) (DBL).
- [Arnoud Visser](http://www.science.uva.nl/~arnoud/) is the supervisor from the [Universiteit van Amsterdam](http://uva.nl), where I am doing my Master's study in Artificial Intelligence.  As a member of the [Intelligent Systems Lab Amsterdam](http://isla.science.uva.nl/) (ISLA), he has supervised several projects ever since my Bachelor in AI, and I am glad to work with him.
- [Pieter Jonker](http://www.3me.tudelft.nl/en/about-the-faculty/departments/biomechanical-engineering/organisation/people/jonker/jonker-pp) is DBL staff member.

---

{% include bibliography.html keys="tamura2002steady,gudi2013feature,dekok2013victoria,methenitis2013orientation,schon2005marginalized" %}
