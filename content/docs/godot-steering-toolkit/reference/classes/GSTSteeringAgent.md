+++
title = "GSTSteeringAgent"
description = "Adds velocity, speed, and size data to `GSTAgentLocation`.\n\n It is the character's responsibility to keep this information up to date for\n the steering toolkit to work correctly."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTAgentLocation

## Description ##

Adds velocity, speed, and size data to `GSTAgentLocation`.

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

## Methods ##

Type | Name
 --- | --- 

## Property Descriptions ##


### zero\_linear\_speed\_threshold ###

```gdscript
var zero_linear_speed_threshold: float
```

The amount of velocity to be considered effectively not moving.

### linear\_speed\_max ###

```gdscript
var linear_speed_max: float
```

The maximum speed at which the agent can move.

### linear\_acceleration\_max ###

```gdscript
var linear_acceleration_max: float
```

The maximum amount of acceleration that any behavior can apply to the agent.

### angular\_speed\_max ###

```gdscript
var angular_speed_max: float
```

The maximum amount of angular speed at which the agent can rotate.

### angular\_acceleration\_max ###

```gdscript
var angular_acceleration_max: float
```

The maximum amount of angular acceleration that any behavior can apply to an
 agent.

### linear\_velocity ###

```gdscript
var linear_velocity: Vector3
```

Current velocity of the agent.

### angular\_velocity ###

```gdscript
var angular_velocity: float
```

Current angular velocity of the agent.

### bounding\_radius ###

```gdscript
var bounding_radius: float
```

The radius of the sphere that approximates the agent's size in space.

### is\_tagged ###

```gdscript
var is_tagged: bool
```

Used internally by group behaviors and proximities to mark the agent as already
 considered.