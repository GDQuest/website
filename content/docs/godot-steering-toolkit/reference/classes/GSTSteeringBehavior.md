+++
title = "GSTSteeringBehavior"
description = "Base class for all steering behaviors.\n\n Steering behaviors calculate the linear and the angular acceleration to be\n to the agent that owns them.\n\n The `calculate_steering` function is the entry point for all behaviors.\n Individual steering behaviors encapsulate the steering logic."
author = "razoric"
date = "2020-02-05"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** 

## Description ##

Base class for all steering behaviors.

 Steering behaviors calculate the linear and the angular acceleration to be
 to the agent that owns them.

 The `calculate_steering` function is the entry point for all behaviors.
 Individual steering behaviors encapsulate the steering logic.

## Properties ##

Type | Name
 --- | --- 
bool | is_enabled
GSTSteeringAgent | agent

## Methods ##

Type | Name
 --- | --- 
GSTTargetAcceleration | func calculate_steering(acceleration: GSTTargetAcceleration) -> GSTTargetAcceleration

## Property Descriptions ##


### is\_enabled ###

{{< highlight gdscript  >}}var is_enabled: bool{{< / highlight >}}

If `false`, all calculations return zero amounts of acceleration.

### agent ###

{{< highlight gdscript  >}}var agent: GSTSteeringAgent{{< / highlight >}}

The AI agent on which the steering behavior bases its calculations.

## Method Descriptions ##


### calculate\_steering ###

{{< highlight gdscript  >}}func calculate_steering(acceleration: GSTTargetAcceleration) -> GSTTargetAcceleration{{< / highlight >}}

Returns the `acceleration` modified with the behavior's desired amount of
 acceleration.