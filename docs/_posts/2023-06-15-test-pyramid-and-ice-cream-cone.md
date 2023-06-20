---
layout: post
title:  "Test pyramid and ice-cream cone"
tags: quality
---
The test ice-cream cone is a strategic anti-pattern.
It indicates excessive reliance on expensive and flaky forms of testing,
such as manual and end-to-end, especially for components that
could otherwise be tested with cheaper and much faster tests.

Although there are many variations of the ice-cream cone (and it's antithesis: the test pyramid)
out there, I find myself referring back to these by James Shore.
They are from his talk _[Agile without a dedicated QA](https://youtu.be/_Dv4M39Arec)_.
For my own reference, I am capturing the images from his slides below.

### The test pyramid

An effective test strategy.

<center><img src="/assets/images/james-shore-test-pyramid.png" width="700" alt="Test pyramid"></center>

### The test ice-cream cone

A test strategy that results in expensive yet fragile tests and hard to change software.

<center><img src="/assets/images/james-shore-test-ice-cream-cone.png" width="700" alt="Test ice-cream cone"></center>

**What are focused integration tests?**
These are integration tests that test just the interface between our code and external systems.
Since integration tests are generally slow to run, by keeping the integration layer thin
and the subsequent tests "focused", we can limit the number of integration tests we write
(i.e. proportional to how many integrations there are in our system).