+++
title = "Measuring the speed of your code"
description = "Using the profiler and measuring individual blocks of code with timers"
menuTitle = "Optimization 1 - Measure your code"
author = "razoric"

date = 2020-08-19T14:00:45-04:00
weight = 4
draft = true

difficulty = "intermediate"
tags = ["tutorial", "godot", "gdscript"]
keywords = ["gdscript optimization tutorial", "godot code optimizing", "godot optimization"]
+++

![The profiler](images/profiler.png)

## An overview of the profiler

### Starting profiling code

### Measurements

### Scope of measurement

![Measuring inclusive](images/split_curve.png)

![Measuring self](images/self_curve.png)

## Measuring manually in microseconds

```gdscript
var start = OS.get_ticks_usec()

worker_function()

var end = OS.get_ticks_usec()

print((end-start)/1000000.0)
```
