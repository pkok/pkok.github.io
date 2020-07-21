---
title: Getting SLAMBench to work
layout: post
categories:
  - thesis
---

Today I'm trying to get [SLAMBench 3](https://github.com/mihaibujanca/slambench3/commit/4b85237ff1009f3567c4b2be222fb761871a4768) to work. It needed some modifications.

I'm working on a fairly fresh install (not too many packages installed through `apt`) of Ubuntu 18.04.  After cloning, I had to do the following steps:

1. **Start by downloading the dependencies.**  When that is done, download the required datasets.  This is the command I used:
  ```sh
$ make deps;
$ ### EuRoC MAV Machine Hall
$ make ./datasets/EuRoCMAV/machine_hall/MH_01_easy/MH_01_easy.slam;
$ make ./datasets/EuRoCMAV/machine_hall/MH_02_easy/MH_02_easy.slam;
$ make ./datasets/EuRoCMAV/machine_hall/MH_03_medium/MH_03_medium.slam;
$ make ./datasets/EuRoCMAV/machine_hall/MH_04_difficult/MH_04_difficult.slam;
$ make ./datasets/EuRoCMAV/machine_hall/MH_05_difficult/MH_05_difficult.slam;
$ ### EuRoC MAV Vicon Room
$ make ./datasets/EuRoCMAV/vicon_room1/V1_01_easy/V1_01_easy.slam;
$ make ./datasets/EuRoCMAV/vicon_room1/V1_02_medium/V1_02_medium.slam;
$ make ./datasets/EuRoCMAV/vicon_room1/V1_03_difficult/V1_03_difficult.slam;
$ make ./datasets/EuRoCMAV/vicon_room2/V2_01_easy/V2_01_easy.slam;
$ make ./datasets/EuRoCMAV/vicon_room2/V2_02_medium/V2_02_medium.slam;
$ make ./datasets/EuRoCMAV/vicon_room2/V2_03_difficult/V2_03_difficult.slam;
  ```
  **This will take quite some time.** In the meantime, continue with the below steps.
  After `make deps` is finished, you can use `make datasetslist` to see all available datasets.
2. **Fix a small bug in the `CMakeLists.txt` file.**  The `CMAKE_MODULE_PATH` variable is not set, because the authors have used `MESSAGE()` to do that, instead of `SET()`.  I will make a small pull request for this.  Change line line 9 from:
  ```cmake
MESSAGE(STATUS CMAKE_MODULE_PATH=${CMAKE_MODULE_PATH})
  ```
  to:
  ```cmake
SET(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake_modules/)
  ```
3. **Fixing pre-compile errors.** I went through the list of libraries that are not found in the process.  If it's only a `apt install LIBNAME`, I will not describe it here.  Libraries that needed a bit more work to get them to work:
  - PAPI: `libsensors.so` is not present. Do:
  ```sh
$ cd /usr/lib/<YOUR ARCHITECTURE>
$ sudo ln -s libsensors.so.4 libsensors.so
  ```
  - CUDA: On my system with an NVIDIA GPU and driver, I had to install `nvidia-cuda-toolkit` through `apt`.
  - OpenCL: Related to CUDA, I had to install `ocl-icd-opencl-dev` and `libpoclu-dev` through `apt`.
  - Ensenso: I downloaded the latest `.deb` from [the Ensenso website](https://www.ensenso.com/support/sdk-download/) and installed it.
  - David SDK: I have not tried to fix this. It probably requires [this modified copy](https://gitlab.com/InstitutMaupertuis/davidSDK) of the official David SDK.  You still need a copy of the official David SDK which costs money.
  - DSSDK: This probably refers to the SDK of Sony's DepthSense.  I don't have access to that.
  - The following warnings are generated from the hardcoded configuration for the PCL cmake config.  I ignored them.
  ```
** WARNING ** io features related to dssdk will be disabled
** WARNING ** io features related to pcap will be disabled
** WARNING ** io features related to png will be disabled
  ```
  - VTK: Two VTK related files could not be found.  I created symlinks to them:
  ```sh
$ sudo ln -s /usr/lib/python2.7/dist-packages/vtk/libvtkRenderingPythonTkWidgets.x86_64-linux-gnu.so /usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so
$ sudo ln -s /usr/bin/vtk6 /usr/bin/vtk
  ```
  - RSSDK: **Installing the RealSense SDK did not resolve this message!!!** *What I did what didn't help is:* This probably refers to the RealSense SDK.  I installed it by following the steps from [the Intel RealSense SDK website](https://www.intelrealsense.com/sdk-2/):
  ```sh
$ echo "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo $(lsb_release --short --codename) main" | sudo tee /etc/apt/sources.list.d/realsense-public.list
$ sudo apt-key adv --keyserver keys.gnupg.net --recv-key 6F3EFCDE 
$ sudo apt update
$ sudo apt install -y librealsense2-dkms librealsense2-utils librealsense2-dev
   ```
4. **Fixing compile errors.**
  - in `slambench3/framework/tools/accuracy-tools/pointcloud_aligner.cpp`, both `HAVE_OPENNI` and `HAVE_OPENNI2` need to be `undef`d:
  ```sh
$ sed -i "s/^#undef HAVE_OPENNI$/&\n#undef HAVE_OPENNI2/" slambench3/framework/tools/accuracy-tools/pointcloud_aligner.cpp 
  ```
  - During compilation, the compiler links `libpapi.a`, which does not contain all symbol definitions. To fix it, only link to the `.so` file. In `slambench3/cmake_modules/FindPAPI.cmake`, remove `libpapi.a` from the `find_library(PAPI_LIBRARY ...)` command:
  ```sh
$ sed -i "s/\<libpapi.a\>//" slambench3/cmake_modules/FindPAPI.cmake
  ```
5. **Start compilation.** When `make deps` from the first step is finished, build slambench with the required algorithms.  From the Slambench3 repository root directory, run
  ```sh
$ make slambench APPS=orbslam2 -j
```
6. **Now I can use Slambench3 on Ubuntu 18.04.**

On my first run of
```sh
$ ./build/bin/benchmark_loader -i datasets/EuRoCMAV/vicon_room1/V1_01_easy/V1_01_easy.slam -load build/lib/liborgslam2-original-library.so -o output.log
```
the output indicated that ORB-SLAM did not report any changes in X/Y/Z until frame 831 (after 41.5 s(?) passed).  Not sure why though.  Running `./build/bin/pangolin_loader` with the same arguments did not show the camera moving during the process.  Something new to figure out tomorrow!
