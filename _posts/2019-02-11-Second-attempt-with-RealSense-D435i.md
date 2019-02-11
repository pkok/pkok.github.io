---
layout: post
categories:
  - thesis
  - sensor/realsense
---

No problems* with the D435i anymore.

After talking with Arnoud, it seemed like the sensor should have worked with `realsense-viewer`.  He showed [in his labbook](https://staff.fnwi.uva.nl/a.visser/activities/IMAV/Labbook2018.html) that it works with `realsense-viewer` v2.17.0 on Ubuntu 18.04.

At home, I saw that I use `realsense-viewer` v2.18.0 on Ubuntu 16.04.  It turned out that after an update on those packages through `apt-get`, it all works.  The Linux kernel was also updated, from 4.15.0-43 to 4.15.0-45.
