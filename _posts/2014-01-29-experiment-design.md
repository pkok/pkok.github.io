---
title: Experiment design
layout: post
categories:
  - thesis
  - augmented reality
---

After the talk with all supervisors, one of the biggest questions is how the system evaluation will be performed.  A small discussion on AR system evaluation seems appropriate.

[Previously]({% post_url 2014-01-22-preparing-for-meeting %}), I mentioned the systems of [Bleser et al.](#bleser2008advanced) and [Ta et al.](#ta2013monocular).  While I like certain aspects of their approach, something certainly struck me while reading more and more AR papers; system evaluation is hard and often slightly neglected.

As an objective measure, Bleser et al. evaluate their system by reporting the root mean square prediction error in pixels for their different sensor fusion models, and the standard deviation.  But for as far as I can tell, this is based on estimated errors of the system, and not on measurements of an external system/observer.

Ta et al. have a different approach.  They plot the estimated path as an overlay on the ground floor of the environment.  I take this as a valid approach for them; for most purposes, a robot does not need to know a sub-milimeter precise location.  However, it is hard to deduce a quantitative evaluation from this map.

{% include bibliography.html keys="bleser2008advanced,ta2013monocular" %}
