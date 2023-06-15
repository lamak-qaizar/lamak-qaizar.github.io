---
layout: post
title:  "Test pyramid and ice-cream cone"
tags: quality
---
The test ice-cream cone is an anti-pattern that indicates an over reliance
on manual and end-to-end testing, especially for components that
could be tested with forms of tests that are cheap to write, run and maintain,
as well as provide much faster feedback.

Although there are many images and variations of the ice-cream cone (and it's antithesis: the test pyramid)
out there, I find myself referring back to these by James Shore.
They are from his talk _[Agile without a dedicated QA](https://youtu.be/_Dv4M39Arec)_.
For easy reference, I am capturing them below.

### The test pyramid

An effective test strategy.

<center><img src="/assets/images/james-shore-test-pyramid.png" width="700" alt="Test pyramid"></center>

### The test ice-cream cone

A test strategy that results in expensive yet fragile tests and hard to change software.

<center><img src="/assets/images/james-shore-test-ice-cream-cone.png" width="700" alt="Test ice-cream cone"></center>