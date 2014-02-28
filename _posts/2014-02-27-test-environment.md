---
layout: post
categories:
  - augmented reality
---

**FINALLY** I got some basic tracking working under OpenGL!

Alright, this sounds way too basic to take serious.  I have been building a simple test application, so I can compile and run my experiments under Linux.  The maintainers of the framework have a licensed Unity SDK which works under Windows.  I must admit that I don't have any C++ development experience under Windows, and got attached to my Linux terminal tools for no better reason than "I have always done things this way, why change?".  

Toby and I decided it would be nice to write an own test environment, based on OpenGL.  There should be only really basic functionality.  On the background of the 3D environment, there should be the camera stream as a flat image.  As an overlay, a cube or other (orientation invariant) object should be drawn for each marker observed in the right 3D position and 3D orientation (6D pose).

However, I haven't had any experience with OpenGL and took the copy-paste-mashup approach in making my own program.  Guess what, you'll be missing parts.  Such as calls to `glPushMastrix()` and `glPopMatrix()`.

What I have done right now:

  - I put most OpenGL setup code in a `tracker::GLRenderer` class, and have it accept custom function handlers for `glutDisplayFunc`, `glutKeyboardFunc`, and `glutVisbilityFunc`.  It also provides defaults for `glutKeyboardFunc` and `glutVisibilityFunc`.  
  - Drawing the camera stream in the background is done by drawing a plane and adding the camera's image as a texture.  How far from the OpenGL world camera it is put, I have no clue.  I draw some 2D object in a 3D world, and seemingly, it works.  This whole functionality is hidden into the public methods `tracker::GLRenderer::setBackgroundTexture(cv::InputArray data)`, `tracker::GLRenderer::drawBackground()` and private method `tracker::GLRenderer::createBackgroundTexture(int width, int height, unsigned char* imageData)`.

I have tested this setup first by drawing a colored cube in front of the background, and then attempted to draw the cube on an observed ArUco marker's position.  The cube reacts on pose changes of the marker, but not correctly yet.  Distances of translation are not scaled.  Rotations are even worse; the center of rotation and rotation axes are not interpreted correctly.

I know that ArUco can return some transformation matrix specifically for OpenGL with `aruco::Marker::glGetModelViewMatrix(double[16])`, but I have no clue which OpenGL function should receive this array...
