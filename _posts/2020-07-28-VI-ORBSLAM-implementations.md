---
title: VI-ORBSLAM(2) implementations
layout: post
categories:
  - thesis
---

I've been looking for already existing implementations of a visual-inertial ORB-SLAM or ORB-SLAM2.  So far, I haven't found anything yet.

Links of interest:
- Of course, the canonical implementation of [ORB-SLAM 1 and 2](https://github.com/raulmur/ORB_SLAM2), provided by Raúl Mur-Artal et al. under the GPLv3 license.  However, they don't supply any visual-inertial implementations.
- Russell Buchanan [has started implementing](https://github.com/raabuchanan/VIOS.git) some VI-integrations in a fork of the above repository.  It does not seem finished, or strictly adhering to [the VI-ORBSLAM](#murartal2017visual) paper.
- [Jing Wang](https://github.com/jingpang/LearnVIORB/) has implemented VI-ORBSLAM on the (non-forked, copy-pasted) canonical ORB-SLAM2 implementation.  I found [a paper](https://www.mdpi.com/2218-6581/7/3/45/htm) using that implementation as an implementation of VI-ORBSLAM as there is no canonical version.
- VI-ORBSLAM heavily leans on the work done in [this paper](#forster2017onmanifold).  [GTSAM 4](https://github.com/borglab/gtsam) improves upon that paper, and provides an implementation of this library under the simplified BSD license.  I might integrate this in ORB-SLAM2.

{% include bibliography.html keys="murartal2017visual,forster2017onmanifold" %}
