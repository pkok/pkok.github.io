---
title: Benchmark of serializers
layout: post
categories:
  - thesis
---

As we have [previously seen](/2019/03/03/Designing-the-data-collector/), throughput is essential.  One major factor in throughput is how data is serialized.  With the experiments in this post, I motivate my choice for capnproto in this project.

Serialization is the process of translating in-memory objects in a format that can be stored or transmitted and reconstructed later.  There are several serialization protocols implemented for C++.  [Konstantin Sorokin](https://github.com/thekvs) has provided [a GitHub repository](https://github.com/thekvs/cpp-serializers) that performs a benchmark on a collection of these serializers, to perform a comparison on them.  I have updated the serializers to their latest versions in [this commit](https://github.com/pkok/cpp-serializers/tree/thesis-experiments), and performed the benchmark on [my own laptop](/hardware#laptop-lulu) (as a baseline) and on the [UDOO](/hardware#udoo) as this will be the data collector.

As I am writing this, the pull requests are not yet made.  Therefore I will refer to cpp-serializers repository with my own forked version.

## Experiment setup
To determine which serialization tool to use, I have used the following serializers (and their specific version):

| Serializer  | Version |
|:------------|:--------|
| thrift      | 0.13.0  |
| protobuf    | 3.11.2  |
| boost       | 1.72.0  |
| msgpack     | 3.1.1   |
| cereal      | 1.3.0   |
| avro        | 1.9.1   |
| capnproto   | 0.7.0   |
| flatbuffers | 1.11.0  |
| YAS         | 7.0.5   |

The benchmarks are performed on the [UDOO](/hardware#udoo).

The GitHub repository [pkok/cpp-serializers](https://github.com/pkok/cpp-serializers) has been compiled on the UDOO:

```bash
cd ~
git clone git@github.com:pkok/cpp-serializers.git
cd cpp-serializers
git checkout thesis-experiments
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

Afterwards, the UDOO has been rebooted, to know that there are no unneccessary background processes running, we can run two small experiments

The tiny scripts presented below are stored in the repository's `./images/generate_graph_data.sh`.

### Size
To determine the message sizes, the following bash script is executed:
```bash
cd ~/cpp-serializers/build/
for t in thrift-binary thrift-compact protobuf boost msgpack cereal avro capnproto flatbuffers yas yas-compact;
do
  ./benchmark -i 1 -s $t | grep Size | awk "{printf \"%d, # %s\n\", \$3, \"$t\"}";
done
```

### Time
As stated in the original experiment, for the time experiment, 1.000.000 serialize-deserialize operations are 50 times performed.  The presented results are averaged over the 50 runs.


While connected through SSH with GNU-screen, the results of the following bash script are presented:
```bash
for t in thrift-binary thrift-compact protobuf boost msgpack cereal avro yas yas-compact capnproto flatbuffer;
do
  rm -f /tmp/$t.time
  for i in `seq 1 50`
  do 
    ./benchmark -i 1000000 -s $t | grep Time | awk '{print $3}' >>/tmp/$t.time
  done;
  awk "{ sum += \$1 } END {printf \"%f, # %s\n\", sum/50, \"$t\"}" /tmp/$t.time
done
```

As capnproto and flatbuffers store the direct in-memory representation of the data, we measure the full build-serialize-deserialize cycle of the data structure.  For the other libraries, only the serialize-deserialize cycle of the already built data structures is measured.

## Results

The results of above experiments are reported in the tables below.  The results are sorted based on how much time it took on the UDOO, fastest first.  The two different experiments are reported in separate tables.

<figure>

| Serializer     | Object size (bytes) | Time on [laptop](/hardware#laptop-lulu) (ms) | Time on [UDOO](/hardware#udoo) (ms) | $$T_{U} / T_{l}$$ |
|:---------------|--------------------:|---------------------------------------------:|------------------------------------:|------------------:|
| yas            |               17416 |                                      3307.36 |                            12526.64 |           3.78750 |
| cereal         |               17416 |                                     14203.78 |                            43540.38 |           3.06541 |
| thrift-binary  |               17017 |                                     13795.10 |                            45265.94 |           3.28131 |
| boost          |               17470 |                                     14231.32 |                            52358.60 |           3.67911 |
| msgpack        |               13402 |                                     31668.70 |                            74930.82 |           2.36608 |
| protobuf       |               16116 |                                     30041.42 |                            89314.20 |           2.97304 |
| yas-compact    |               13321 |                                     28981.90 |                            92681.32 |           3.19790 |
| thrift-compact |               13378 |                                     41831.28 |                           128487.80 |           3.07157 |
| avro           |               16384 |                                     55352.74 |                           139369.58 |           2.51784 |

<figcaption>
Results of running the serialize-deserialze experiments.
</figcaption>
</figure>

<figure>

| Serializer     | Object size (bytes) | Time on [laptop](/hardware#laptop-lulu) (ms) | Time on [UDOO](/hardware#udoo) (ms) | $$T_{U} / T_{l}$$ |
|:---------------|--------------------:|---------------------------------------------:|------------------------------------:|------------------:|
| capnproto      |               17768 |                                      4512.32 |                            15054.64 |            2.70578 |
| flatbuffers    |               17632 |                                      5821.92 |                            15752.86 |            3.33634 |

<figcaption>
Results of running the build-serialize-deserialize experiments.
</figcaption>
</figure>

## Discussion
When comparing between the performance on my laptop and on the UDOO, it is interesting to look at the differences in ranking.  Differences in ranking seldomly occur, and if present, do not exceed more than 1. These changes seem neglectable.

The final colum in both tables present the speedup ratio the laptop provides over the UDOO.  We see that this lies between 2.4 (msgpack) and 3.8 (yas).  This might be explained by unexpected background tasks running on any platform, or specific CPU optimalizations performed by the compiler or serialization library. If a good comparison between platforms is needed, more investigation is needed.  For my purposes, this is not needed, but might be interesting for future projects.

yas seems to be the fastest on both platforms in the serialize-deserialize category.  It is a factor 3.5 (UDOO) to 4.3 (laptop) faster than the number two in that category.  However, it differs not that much with capnproto (factor 1.2 (UDOO) to 1.4 (laptop)) or flatbuffers (factor 1.3 (UDOO) to 1.8 (laptop)), while these two also build the data structure during the experiments.  Including the build step in yas will most certainly increase the duration of each simulation, and probably making it slower than capnproto and flatbuffers.

Differences in speed between capnproto and flatbuffers are present but relatively small. 

Object size ranges from 13321 bytes (yas-compact) to 17768 bytes (capnproto).  The object sizes of yas, capnproto and flatbuffers also barely differ, with a maximum size difference of 352 bytes between capnproto and yas.

## Conclusion

The differences between the top-tier serializers -- yas, capnproto and flatbuffers -- are small, but present.  Having a faster serializer comes with the price of larger objects.  For this project, speed is more limiting than object size.  Therefore I will use capnproto for this project.
