+++
title = "GSAISteeringBehavior"
description = "Base class for all steering behaviors.\n\nSteering behaviors calculate the linear and the angular acceleration to be\nto the agent that owns them.\n\nThe `calculate_steering` function is the entry point for all behaviors.\nIndividual steering behaviors encapsulate the steering logic."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

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
GSAISteeringAgent | agent

## Functions ##

Type | Name
 --- | --- 
void | func calculate_steering(acceleration: GSAITargetAcceleration) -> void

## Property Descriptions ##

### is\_enabled ###

{{< highlight gdscript  >}}var is_enabled: bool{{< / highlight >}}

If `false`, all calculations return zero amounts of acceleration.

### agent ###

{{< highlight gdscript  >}}var agent: GSAISteeringAgent{{< / highlight >}}

The AI agent on which the steering behavior bases its calculations.

## Method Descriptions ##

### calculate\_steering ###

{{< highlight gdscript  >}}func calculate_steering(acceleration: GSAITargetAcceleration) -> void{{< / highlight >}}

Sets the `acceleration` with the behavior's desired amount of acceleration.