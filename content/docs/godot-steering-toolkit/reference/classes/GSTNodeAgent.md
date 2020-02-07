+++
title = "GSTNodeAgent"
description = "A base class for a specialized steering agent that updates itself every frame\n so the user does not have to."
author = "razoric"
date = "2020-02-06"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSteeringAgent

## Description ##

A base class for a specialized steering agent that updates itself every frame
 so the user does not have to.

## Properties ##

Type | Name
 --- | --- 
bool | use_physics
bool | calculate_velocities
bool | apply_linear_drag
bool | apply_angular_drag
float | linear_drag_percentage
float | angular_drag_percentage
int | kinematic_movement_type

## Methods ##

Type | Name
 --- | --- 
void | func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void

## Property Descriptions ##


### use\_physics ###

```gdscript
var use_physics: bool
```

Setter | _set_use_physics

If `true`, will update before `_physics_process` is called. If `false`, will
 update before `_process` is called.
 
 `KinematicBody`, `KinematicBody2D`, `RigidBody`, and `RigidBody2D` should
 always use `_physics_process`.

### calculate\_velocities ###

```gdscript
var calculate_velocities: bool
```

If `true`, will calculate linear and angular velocities based on the previous
 frame. When `false`, the user must keep those values updated.

### apply\_linear\_drag ###

```gdscript
var apply_linear_drag: bool
```

If `true` and velocities and `calculate_velocities` is true, will interpolate
 the current linear velocity towards 0 by the `linear_drag_percentage` value.
 Does not apply to `RigidBody` and `RigidBody2D` nodes.

### apply\_angular\_drag ###

```gdscript
var apply_angular_drag: bool
```

If `true` and velocities and `calculate_velocities` is true, will interpolate
 the current angular velocity towards 0 by the `angular_drag_percentage` value.
 Does not apply to `RigidBody` and `RigidBody2D` nodes.

### linear\_drag\_percentage ###

```gdscript
var linear_drag_percentage: float
```

The percentage between the current linear velocity and 0 to interpolate by if
 `calculate_velocities` and `apply_linear_drag` are true.
 Does not apply to `RigidBody` and `RigidBody2D` nodes.

### angular\_drag\_percentage ###

```gdscript
var angular_drag_percentage: float
```

The percentage between the current angular velocity and 0 to interpolate by if
 `calculate_velocities` and `apply_angular_drag` are true.
 Does not apply to `RigidBody` and `RigidBody2D` nodes.

### kinematic\_movement\_type ###

```gdscript
var kinematic_movement_type: int
```

Determines how linear movement occurs if the body is a `KinematicBody` or
 `KinematicBody2D`.
 
 SLIDE uses `move_and_slide`
 COLLIDE uses `move_and_collide`
 POSITION changes global position directly

## Method Descriptions ##


### \_apply\_steering <small>(virtual)</small> ###

```gdscript
func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void
```

Moves the agent's body by target `acceleration`.