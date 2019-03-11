---
title: Synchronization statistics of Structure Core and RealSense D435i
layout: post
categories:
  - thesis
  - sensor/realsense
  - sensor/structure
---
Both sensors report to be "synchronized", but do not report which data streams are all synchronized.  This is an initial check to see how well-synchronized both sensors are.

All numbers are subject to floating-point rounding problems.

## Structure Core

For the Structure Core, I recorded 4 datasets.  I will present their separate statistics as well as those of the aggregate of all 4 datasets.  The average timespan between two frames and its standard deviation is computed for each stream, to indicate the variation of capture moments.  Duration of each quartile of the sequence is shown to indicate a change of capture speed over time, for instance because of mild sensor heating.

| Experiment 1                 | Accelerometer           | Gyroscope                | Visible frame          | Depth frame             |
|:-----------------------------|------------------------:|-------------------------:|-----------------------:|------------------------:|
| Frames (#)                   | 3039                    | 2403                     | 342                    | 342                     |
| Full recording duration (ms) | 12041.62522600017837    | 12038.97493600015878     | 11367.65530900083832   | 11363.26461700082291    |
| - µ frame (ms)               | 3.96236433892733686     | 5.009977085310095113     | 33.23875821345274062   | 33.22591993275094779    |
| - σ² frame (ms²)             | 0.005191025981201912408 | 1.953584414495976567e-05 | 0.06875941255987630396 | 0.009516990982518210365 |
| - σ frame (ms)               | ±0.07204877501527637285 | ±0.004419937120023288701 | ±0.2622201604756512761 | ±0.09755506641132591361 |
| - Quartile 1 (ms)            | 3009.792598999410984    | 3007.782460999806062     | 2837.32400500048243    | 2832.988584999839077    |
| - Quartile 2 (ms)            | 3013.371452001592843    | 3012.037775999488076     | 2865.654637998886756   | 2865.639408999413718    | 
| - Quartile 3 (ms)            | 3017.121379998570774    | 3017.080018000342534     | 2865.654695000557695   | 2865.639442999963649    | 
| - Quartile 4 (ms)            | 3001.339795000603772    | 3002.074681000522105     | 2799.021971000911435   | 2798.997180001606466    |


| Experiment 2                 | Accelerometer           | Gyroscope               | Visible frame           | Depth frame              |
|:-----------------------------|------------------------:|------------------------:|------------------------:|-------------------------:|
| Frames (#)                   | 23414                   | 18528                   | 2769                    | 2769                     |
| Full recording duration (ms) | 92840.6934619997628     | 92843.13572300015949    | 92238.48698099754984    | 92234.04957100137835     |
| µ frame (ms)                 | 3.965178673528647391    | 5.010963715619611847    | 33.31111844745306882    | 33.30951591585459681     |
| σ² frame (ms²)               | 0.003371298287579960282 | 0.004081208572344209584 | 0.008110184188772309732 | 0.0001452740751085405675 |
| σ frame (ms)                 | ±0.05806288218457605899 | ±0.06388433745719061807 | ±0.09005656105344189699 | ±0.01205296955561327953  |
| Quartile 1 (ms)              | 23201.28362699688296    | 23208.85135100252228    | 23062.969078997412      | 23058.53624099836452     |
| Quartile 2 (ms)              | 23208.74003500284743    | 23210.54916299908655    | 23058.49369200223009    | 23058.54214000282809     |
| Quartile 3 (ms)              | 23220.14308500001789    | 23216.44786599790677    | 23091.84596200066153    | 23091.74949499720242     |
| Quartile 4 (ms)              | 23210.52671500001452    | 23207.28734300064389    | 23025.17824799724622    | 23025.22169500298332     |

| Experiment 3                 | Accelerometer          | Gyroscope              | Visible frame          | Depth frame            |
|:-----------------------------|-----------------------:|-----------------------:|-----------------------:|-----------------------:|
| Frames (#)                   | 23579                  | 18661                  | 2793                   | 2793                   |
| Full recording duration (ms) | 93622.17069500184152   | 93633.60289300180739   | 93073.0003120006586    | 93068.55538500167313   |
| µ frame (ms)                 | 3.970574269265101819   | 5.017609072021960159   | 33.32366642033679227   | 33.32207496777718347   |
| σ² frame (ms²)               | 0.3881272417201211966  | 0.4938603821438762864  | 0.4052922694137864879  | 0.3976716647585425424  |
| σ frame (ms)                 | ±0.6229985888588522869 | ±0.7027520061471730362 | ±0.6366256901930572587 | ±0.6306121349597886283 |
| Quartile 1 (ms)              | 23467.69647800101666   | 23474.12857599920244   | 23297.39655600133119   | 23293.01529599979403   |
| Quartile 2 (ms)              | 23381.6045870007656    | 23379.10427300084848   | 23258.66070600022795   | 23258.58952500129817   |
| Quartile 3 (ms)              | 23387.12735299850465   | 23389.85915800003568   | 23291.6907299986633    | 23291.77451999930781   |
| Quartile 4 (ms)              | 23385.74227700155461   | 23390.51088600172079   | 23225.25232000043616   | 23225.17604400127311   |

| Experiment 4                 | Accelerometer         | Gyroscope             | Visible frame         | Depth frame           |
|:-----------------------------|----------------------:|----------------------:|----------------------:|----------------------:|
| Frames (#)                   | 18801                 | 14870                 | 2222                  | 2222                  |
| Full recording duration (ms) | 74651.87614200112876  | 74656.77039100410184  | 74079.97032900311751  | 74075.49377199757146  |
| µ frame (ms)                 | 3.970633271740925174  | 5.020630154068870254  | 33.33932058010940835  | 33.33730592799170722  |
| σ² frame (ms²)               | 0.8577167374723690951 | 1.057801154773015728  | 2.008274178440045077  | 1.999558727001227609  |
| σ frame (ms)                 | ±0.926129978713770563 | ±1.028494606098163233 | ±1.417135906834642745 | ±1.414057540201680618 |
| Quartile 1 (ms)              | 18631.92308900033822  | 18630.56408300326439  | 18499.26990500534885  | 18494.91064999892842  |
| Quartile 2 (ms)              | 18758.41932099865517  | 18760.08542999625206  | 18593.46599700074876  | 18593.43699699820718  |
| Quartile 3 (ms)              | 18635.02716000220971  | 18635.30738899862627  | 18526.85420799389249  | 18526.81509299873142  |
| Quartile 4 (ms)              | 18626.50657199992565  | 18630.81348900595913  | 18460.38021900312742  | 18460.33103200170444  |

The above tables indicate that there are three streams, all watching the same clock:
- Accelerometer
- Gyroscope
- RGB-camera and infrared cameras

The visible (from RGB) and depth frames (computed from infrared stereoimaging) send out "synchronized" as a `ST::CaptureSessionSample s` object with `s.type == ST::CaptureSessionSample::Type::SynchronizedFrames`, which guarantees that `s.visibleFrame` and `s.depthFrame` are set.  


To see if this irregularity would have a big impact, I analyzed the average difference between capturing time of the visible frame and depth frame, and its standard deviation.  In below table, I have captured data about:
- The average $$\mu$$and standard deviation $$\sigma$$ of $$d$$ = (capturing time of depth frame) - (capturing time of visible frame)
- The average $$\mu_+$$ and standard deviation $$\sigma_+$$ of $$d \geq 0$$
- The average $$\mu_-$$ and standard deviation $$\sigma_-$$ of $$d < 0$$

Note that below the unit of time is µs, instead of ms!


| Statistic            | Experiment 1             | Experiment 2           | Experiment 3           | Experiment 4           |
|:---------------------|-------------------------:|-----------------------:|-----------------------:|-----------------------:|
| Camera frames (#)    | 342                      | 24                     | 22                     | 20                     |
| Depth before RGB (#) | 4                        | 2769                   | 2793                   | 2222                   |
| $$\mu$$ (µs)         | 98.57857133533666172     | 76.83608111331449209   | 75.8099934348211093    | 76.59370666507062708   | 
| $$\sigma^2$$ (µs²)   | 114738.696270283006      | 15919.05557173031775   | 8862.051702575803574   | 10618.08396261802409   | 
| $$\sigma$$ (µs)      | ±338.7310087226780411    | 126.1707397605733263   | ±94.13847089567475734  | ±103.0440874704513305  |
| $$\mu_+$$ (µs)       | 99.46351594279263963     | 77.48546691152743904   | 76.39008449199822337   | 77.25964128115872143   | 
| $$\sigma_+^2$$ (µs²) | 115664.8064845397166     | 16001.61974778869808   | 8884.431914360100563   | 10657.79736070112267   | 
| $$\sigma_+$$ (µs)    | 340.0952903004387622     | 126.4975088600115498   | 94.2572645177022963    | 103.2366086264999439   | 
| $$\mu_-$$ (µs)       | -1.420169307190614516    | -0.6949363602831474251 | -0.7620261125599168128 | -0.619659610827894558  | 
| $$\sigma_-^2$$ (µs²) | 0.0005828981862428808062 | 0.2046875673708032362  | 0.1708257127946148368  | 0.09697874038889507664 | 
| $$\sigma_-$$ (µs)    | 0.02414328449575327967   | 0.4524241012267176676  | 0.4133106734583741892  | 0.3114140979289394262  | 

We see that there is an average of around 77 µs (with Experiment 1 an outlier?).  The "reversed" measurements have an average of less than 1 µs between D and RGB frames.  I would suggest that this is "close enough" for my experiments.


## RealSense D435i
