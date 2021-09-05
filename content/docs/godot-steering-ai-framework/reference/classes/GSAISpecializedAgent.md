---
author: razoric
date: "2020-02-25"
description: |-
  A base class for a specialized steering agent that updates itself every frame
  so the user does not have to. All other specialized agents derive from this.
title: GSAISpecializedAgent (abstract)
---

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAISteeringAgent](../gsaisteeringagent) < [GSAIAgentLocation](../gsaiagentlocation)

## Description ##

A base class for a specialized steering agent that updates itself every frame
so the user does not have to. All other specialized agents derive from this.

## Properties ##

Type | Name
 --- | --- 
bool | calculate_velocities
bool | apply_linear_drag
bool | apply_angular_drag
float | linear_drag_percentage
float | angular_drag_percentage

## Functions ##

Type | Name
 --- | --- 
void | func _apply_steering(_acceleration: GSAITargetAcceleration, _delta: float) -> void

## Property Descriptions ##

### calculate\_velocities ###

{{< highlight gdscript  >}}var calculate_velocities: bool{{< / highlight >}}

If `true`, calculates linear and angular velocities based on the previous
frame. When `false`, the user must keep those values updated.

### apply\_linear\_drag ###

{{< highlight gdscript  >}}var apply_linear_drag: bool{{< / highlight >}}

If `true`, interpolates the current linear velocity towards 0 by the
`linear_drag_percentage` value.
Does not apply to `RigidBody` and `RigidBody2D` nodes.

### apply\_angular\_drag ###

{{< highlight gdscript  >}}var apply_angular_drag: bool{{< / highlight >}}

If `true`, interpolates the current angular velocity towards 0 by the
`angular_drag_percentage` value.
Does not apply to `RigidBody` and `RigidBody2D` nodes.

### linear\_drag\_percentage ###

{{< highlight gdscript  >}}var linear_drag_percentage: float{{< / highlight >}}

The percentage between the current linear velocity and 0 to interpolate by if
`apply_linear_drag` is true.
Does not apply to `RigidBody` and `RigidBody2D` nodes.

### angular\_drag\_percentage ###

{{< highlight gdscript  >}}var angular_drag_percentage: float{{< / highlight >}}

The percentage between the current angular velocity and 0 to interpolate by if
`apply_angular_drag` is true.
Does not apply to `RigidBody` and `RigidBody2D` nodes.

## Method Descriptions ##

### \_apply\_steering <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _apply_steering(_acceleration: GSAITargetAcceleration, _delta: float) -> void{{< / highlight >}}

Moves the agent's body by target `acceleration`.