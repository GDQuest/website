---
author: razoric
date: "2020-02-25"
description: |-
  Adds velocity, speed, and size data to `GSAIAgentLocation`.

  It is the character's responsibility to keep this information up to date for
  the steering toolkit to work correctly.
title: GSAISteeringAgent
---

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAIAgentLocation](../gsaiagentlocation)

## Description ##

Adds velocity, speed, and size data to `GSAIAgentLocation`.

It is the character's responsibility to keep this information up to date for
the steering toolkit to work correctly.

## Properties ##

Type | Name
 --- | --- 
float | zero_linear_speed_threshold
float | linear_speed_max
float | linear_acceleration_max
float | angular_speed_max
float | angular_acceleration_max
Vector3 | linear_velocity
float | angular_velocity
float | bounding_radius
bool | is_tagged

## Property Descriptions ##

### zero\_linear\_speed\_threshold ###

{{< highlight gdscript  >}}var zero_linear_speed_threshold: float{{< / highlight >}}

The amount of velocity to be considered effectively not moving.

### linear\_speed\_max ###

{{< highlight gdscript  >}}var linear_speed_max: float{{< / highlight >}}

The maximum speed at which the agent can move.

### linear\_acceleration\_max ###

{{< highlight gdscript  >}}var linear_acceleration_max: float{{< / highlight >}}

The maximum amount of acceleration that any behavior can apply to the agent.

### angular\_speed\_max ###

{{< highlight gdscript  >}}var angular_speed_max: float{{< / highlight >}}

The maximum amount of angular speed at which the agent can rotate.

### angular\_acceleration\_max ###

{{< highlight gdscript  >}}var angular_acceleration_max: float{{< / highlight >}}

The maximum amount of angular acceleration that any behavior can apply to an
agent.

### linear\_velocity ###

{{< highlight gdscript  >}}var linear_velocity: Vector3{{< / highlight >}}

Current velocity of the agent.

### angular\_velocity ###

{{< highlight gdscript  >}}var angular_velocity: float{{< / highlight >}}

Current angular velocity of the agent.

### bounding\_radius ###

{{< highlight gdscript  >}}var bounding_radius: float{{< / highlight >}}

The radius of the sphere that approximates the agent's size in space.

### is\_tagged ###

{{< highlight gdscript  >}}var is_tagged: bool{{< / highlight >}}

Used internally by group behaviors and proximities to mark the agent as already
considered.