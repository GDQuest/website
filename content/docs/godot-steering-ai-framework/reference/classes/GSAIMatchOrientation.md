+++
title = "GSAIMatchOrientation"
description = "Calculates an angular acceleration to match an agent's orientation to that of\nits target. Attempts to make the agent arrive with zero remaining angular\nvelocity."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAISteeringBehavior](../gsaisteeringbehavior)

## Description ##

Calculates an angular acceleration to match an agent's orientation to that of
its target. Attempts to make the agent arrive with zero remaining angular
velocity.

## Properties ##

Type | Name
 --- | --- 
GSAIAgentLocation | target
float | alignment_tolerance
float | deceleration_radius
float | time_to_reach
bool | use_z

## Property Descriptions ##

### target ###

{{< highlight gdscript  >}}var target: GSAIAgentLocation{{< / highlight >}}

The target orientation for the behavior to try and match rotations to.

### alignment\_tolerance ###

{{< highlight gdscript  >}}var alignment_tolerance: float{{< / highlight >}}

The amount of distance in radians for the behavior to consider itself close
enough to be matching the target agent's rotation.

### deceleration\_radius ###

{{< highlight gdscript  >}}var deceleration_radius: float{{< / highlight >}}

The amount of distance in radians from the goal to start slowing down.

### time\_to\_reach ###

{{< highlight gdscript  >}}var time_to_reach: float = 0.1{{< / highlight >}}

The amount of time to reach the target velocity

### use\_z ###

{{< highlight gdscript  >}}var use_z: bool{{< / highlight >}}

Whether to use the X and Z components instead of X and Y components when
determining angles. X and Z should be used in 3D.