---
title: ORB-SLAM2 keeps resetting in SLAMBench3
layout: post
categories:
  - thesis
---

Yesterday I reported that only after many frames ORB-SLAM2 started tracking in SLAMBench.  Today I performed some tests.

When running ORB-SLAM2 with SLAMBench3, the tracker keeps losing initialisation and the local mapper and loop closing threads are reset.  No to barely any "green dots" of ORB matches show up.  See the figure below for a screenshot of some output of running the following line:
```sh
$ cd slambench3/
$ build/bin/pangolin_loader -i ./datasets/EuRoCMAV/machine_hall/MH_02_easy/MH_02_easy.slam -load ./build/lib/liborbslam2-original-library.so
```

<figure>
![Screenshot of SLAMBench3](/assets/img/slambench3-orbslam2-reset-problems.png)
<figcaption>
Screenshot of terminal output and GUI of running SLAMBench3's `pangolin_loader` with dataset EuRoCMAV MH02 and benchmark ORB-SLAM2.
</figcaption>
</figure>

Running ORB-SLAM2 plainly works fine.  The following command has been used to generate the below image.
```sh
$ cd ORB-SLAM2
$ ./Examples/Stereo/stereo_euroc Vocabulary/ORBvoc.txt Examples/Stereo/EuRoC.yaml ../slambench3/datasets/EuRoCMAV/machine_hall/MH_02_easy/MH_02_easy.dir/mav0/cam{0,1}/data Examples/Stereo/EuRoC_TimeStamps/MH02.txt
```

<figure>
![Screenshot of ORB-SLAM2](/assets/img/orbslam2-no-problems.png)
<figcaption>
Screenshot of the GUI of running ORB-SLAM2's `stereo_euroc` with dataset EuRoCMAV MH2.
</figcaption>
</figure>

I have not been able to retrieve the source of the problem.  For now, I will focus on using and modifying the "official" ORB-SLAM2 tools.
