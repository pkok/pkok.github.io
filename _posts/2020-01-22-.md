---
title: Thesis outline and dataset requirements
layout: post
categories:
  - thesis
  - disability
---

After speaking with Arnoud, I'm restarting again.  Focus for today: thesis outline, and getting the requirements for the dataset on paper.

Last year, I suddenly had to stop due to health issues.  Things are going better now again, and I've got a good support system behind me to start working again.

## Thesis outline

The main issue with the outline is how to present the dataset and algorithm, two connected-but-separate parts of work.  Two structures are in my head:

<table>
<thead>
<tr>
  <th>Outline 1</th>
  <th>Outline 2</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">
<ul>
  <li>Title page</li>
  <li>Acknowledgements</li>
  <li>Abstract</li>
</ul>
<ol>
  <li>
    Introduction
    <ul>
      <li>Casual introduction to tracking, localization and mapping</li>
      <li>Casual introduction to the problem</li>
      <li>Examples of the problem</li>
      <li>State research questions and hypotheses</li>
    </ul>
    <ol>
      <li>Thesis outline
        <ul><li>The "In section X, topic Y will be discussed"-talk</li></ul>
      </li>
    </ol>
  </li>
  <li>
    Background
    <ol>
      <li>Simultaneous localization and mapping
        <ul>
          <li>Formal introduction to SLAM</li>
          <li>Formal introduction to the problem?</li>
          <li>Introduce old SLAMs (refs?), sensor-fused localization [<a href="#bleser2008advanced">1</a>, <a href="#bleser2009towards">2</a>], <a href="#klein2007">PTAM</a></li>
          <li>Introduce <a href="#murartal2015orbslam">ORBSLAM</a>, <a href="#murartal2017visual">VI-ORBSLAM</a>, <a href="#murartal2017orbslam2">ORBSLAM2</a></li>
        </ul>
      </li>
      <li> Available datasets
        <ul>
          <li>Discuss datasets of (VI-)ORBSLAM(2) and other cited papers</li>
          <li>Show measured quantities</li>
        </ul>
      </li>
      <li>Calibration
        <ul>
          <li>Casual introduction to calibration</li>
          <li>Formal introduction to calibration</li>
          <li>Investigate different "calibration modalities"</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>
    Method
    <ul>
      <li>Thorough explanation of different techniques used in (VI-)ORBSLAM(2)</li>
      <li>Explain how merging them would increase metrics</li>
    </ul>
  </li>
</ol>
</td>
</tr>

<tr>
<td style="vertical-align:top">
<ol start="4">
  <li>Datasets
    <ul>
      <li>Show that only <a href="#burri2016euroc">EuRoC MAV</a> is applicable</li>
      <li>Motivate that only 1 dataset is not enough</li>
    </ul>
    <ol>
      <li><a href="#burri2016euroc">EuRoC MAV Visual Inertial Dataset</a></li>
      <li>Industrial Robot Arm Dataset
        <ol>
          <li>Method/Design: Hardware/software architecture
            <ul>
              <li>Sensors used</li>
              <li>Ground truth/robot arm</li>
              <li>Computing/recording device</li>
              <li>Clock synchronisation</li>
            </ul>
          </li>
          <li>Method/Design: Dataset features
            <ul>
              <li>Number of sequences</li>
              <li>Calibration methods used</li>
              <li>Visual features: fractal ArUco markers [<a href="#garrido2015generation">1</a>, <a href="#romero2018speeded">2</a>, <a href="#romero2019fractal">3</a>]</li>
              <li>Path features: number of loops/intersections with own path</li>
              <li>Motion features: max Δacceleration, noisiness</li>
              <li>More?</li>
            </ul>
          </li>
          <li>Results/Realisation: analysis of created dataset</li>
          <li>Discussion: dataset</li>
        </ol>
      </li>
    </ol>
  </li>
  <li>Visual-Inertial ORBSLAM2
    <ol>
      <li>Algorithm: discuss how VI-ORBSLAM and ORBSLAM2 are merged into this new work</li>
      <li>Experiment: test ORBSLAM, VI-ORBSLAM, ORBSLAM2, and own algorithm on above datasets</li>
      <li>Results: analysis of algorithms performance on datasets</li>
      <li>Discussion: algorithms</li>
    </ol>
  </li>
</ol>
</td>
<td style="vertical-align:top">
<ol start="4">
  <li>Implementation: discuss how VI-ORBSLAM and ORBSLAM2 are merged into this new work</li>
  <li>Experiment
    <ol>
      <li>Datasets
        <ul>
          <li>Show that only <a href="#burri2016euroc">EuRoC MAV</a> is applicable</li>
          <li>Motivate that only 1 dataset is not enough</li>
        </ul>
        <ol>
          <li><a href="#burri2016euroc">EuRoC MAV Visual Inertial Dataset</a></li>
          <li>Industrial Robot Arm Dataset
            <ol>
              <li>Method/Design: Hardware/software architecture
                <ul>
                  <li>Sensors used</li>
                  <li>Ground truth/robot arm</li>
                  <li>Computing/recording device</li>
                  <li>Clock synchronisation</li>
                </ul>
              </li>
              <li>Method/Design: Dataset features
                <ul>
                  <li>Number of sequences</li>
                  <li>Calibration methods used</li>
                  <li>Visual features: fractal ArUco markers [<a href="#garrido2015generation">1</a>, <a href="#romero2018speeded">2</a>, <a href="#romero2019fractal">3</a>]</li>
                  <li>Path features: number of loops/intersections with own path</li>
                  <li>Motion features: max Δacceleration, noisiness</li>
                  <li>More?</li>
                </ul>
              </li>
            </ol>
          </li>
        </ol>
      </li>
      <li>Algorithms
        <ul>
          <li>Motivate why (ORBSLAM,) VI-ORBSLAM, ORBSLAM2 and own algorithm need to be tested to give a proper comparison of own algorithm and dataset</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>Results
    <ol>
      <li>Dataset
        <ul>
          <li>Does created dataset tick all boxes from experiment design?</li>
          <li>Any important differences between the two IMU-camera modules?</li>
        </ul>
      </li>
      <li>Algorithms
        <ul>
          <li>Compare results from (ORBSLAM,) VI-ORBSLAM, ORBSLAM2 and own algorithm</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>Discussion
    <ol>
      <li>Dataset</li>
      <li>Algorithms</li>
    </ol>
  </li>
</ol>
</td>
</tr>

<tr>
<td colspan="2">
<ol start="8">
  <li>Conclusion
    <ol>
      <li>Dataset</li>
      <li>SLAM method</li>
      <li>Future work</li>
    </ol>
  </li>
</ol>
<ol type="A">
  <li>Appendices...</li>
</ol>
<ul>
  <li>Bibliography</li>
</ul>
</td>
</tr>
</tbody>
</table>

In Outline 1, the projects of dataset creation and performing experiments on the dataset are viewed as separate.  A motivation for this might be that this might leave space to analyse the two projects as independent from each other as possible.  Outline 2 presents the dataset creation project as "experiment design" for the algorithm evaluation.  The experimental setup will be evaluated together with the outcomes.  In this matter, the link between the projects is demonstrated stronger, but might come over as a bit more messy.

This should be discussed with Arnoud.


## Creating the dataset

Last year's stop was health related.  While still recovering, I am looking into how to continue.  The main issue right now is pain when having an "active posture" for more than (roughly, on a good day) 2 hours.  This will decrease over time, but I cannot just be idle in the meantime.  So, I'm looking into how to create the right circumstances that I can make this dataset, without physically harming myself.

### Lab assistant
Arnoud suggested to look for a lab assistant for doing the physical work.  This person should do the physical tasks, while I can remain seated for most of the time.  This does mean that my lab time will be even more precious, and should be prepared even better beforehand, as costs will increase when working longer than expected (for instance, when fixing bugs).  One of the possible sources of getting a lab assistant, would be to contact student initiatives like the [Dutch Nao Team](https://www.dutchnaoteam.nl/nl/homepage/), the students association of Information Sciences at the UvA, [via](https://www.dutchnaoteam.nl/nl/homepage/), or students from the mechatronics and robotics programme at the HvA where I work.

The lab assistant should be paid for their labor.  I have sent a request for support to [UWV](https://www.uwv.nl), the national institute responsible for implementation of laws regarding disability&disease and work&education, for financial support.  They are known to be slow in reply, so I have also contacted the [student counsellor](https://student.uva.nl/en/content/az/student-counsellors/contact/contact-student-counsellors.html) ([studentendecaan](https://student.uva.nl/content/az/studentendecanen/contact/contact-studentendecanen.html)).  I expect a soon reply from the counsellors, based on prior communications.



{% include bibliography.html keys="bleser2008advanced,bleser2009towards,murartal2015orbslam,murartal2017visual,murartal2017orbslam2,garrido2015generation,romero2018speeded,romero2019fractal" %}

