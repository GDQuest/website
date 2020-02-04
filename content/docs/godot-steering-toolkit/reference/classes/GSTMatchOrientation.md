+++
title = "GSTMatchOrientation"
description = "Calculates an angular acceleration to match an agent's orientation to that of\n its target. Attempts to make the agent arrive with zero remaining angular\n velocity."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSteeringBehavior

## Description ##

Calculates an angular acceleration to match an agent's orientation to that of
 its target. Attempts to make the agent arrive with zero remaining angular
 velocity.

## Properties ##

Type | Name
 --- | --- 
GSTAgentLocation | target
float | alignment_tolerance
float | deceleration_radius
float | time_to_reach

## Methods ##

Type | Name
 --- | --- 

## Property Descriptions ##


### target ###

```gdscript
var target: GSTAgentLocation
```

The target orientation for the behavior to try and match rotations to.

### alignment\_tolerance ###

```gdscript
var alignment_tolerance: float
```

The amount of distance in radians for the behavior to consider itself close
 enough to be matching the target agent's rotation.

### deceleration\_radius ###

```gdscript
var deceleration_radius: float
```

The amount of distance in radians from the goal to start slowing down.

### time\_to\_reach ###

```gdscript
var time_to_reach: float = 0.1
```

The amount of time to reach the target velocity