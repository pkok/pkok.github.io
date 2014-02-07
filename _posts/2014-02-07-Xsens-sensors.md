---
layout: post
categories:
  - sensors
---

Today I have an Xsens MTi-28A53G35 and MTx-28A53G25 on my desk in Delft, cables included!  I am trying to figure out how to read data from them, and what their model numbers exactly mean.

After requesting the manuals of the [MTi](http://www.xsens.com/en/contact-form-6) and [MTx](http://www.xsens.com/en/contact-form-17) on the Xsens website, one of the employees contacted me by email.  After a short conversation, I received the URLs to the [SDK](http://www.xsens.com/en/mt-sdk) and [Software Suite](http://www.xsens.com/en/mt-software-suite).  The employee explained both the MTi and MTx return similar readings (including a filtered orientation estimate).  There is a difference in the type of gyroscope and accelerometer.  He included a document on the precision of the motion trackers.

Names can be split in 3 parts: MT{i,x}- *xx* A *yy* G *zz*, where:

- *xx* indicates the interface:
  - 28: RS-232
  - 48: RS-485
  - 49: Xbus
- A *yy* indicates "Full scale acceleration":
  - A53: 5 g (50 m/s^^2 )
  - A83: 18 g (180 m/s^^2 )
- G *zz* indicates "Full scale rate of turn":
  - G15: 150 deg/s
  - G35: 300 deg/s
  - G25: 1200 deg/s

(from the "Hardware Specifications" section on the "Spec" tab of the [MTi page](http://www.xsens.com/en/general/mtx))

----
Executing ``example_mfm_cpp`` did not work ("Device not found").  This was due to the extended cables used in an earlier project of Jurjen Caarls.  Somehow Linux either does not power them enough through the second USB plug, or something else.  Under Windows they work fine.  I asked Guus to look into this.
