+++
title = "GSTTargetAcceleration"
description = "A desired linear and angular amount of acceleration requested by the steering\n system."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** 

## Description ##

A desired linear and angular amount of acceleration requested by the steering
 system.

## Properties ##

Type | Name
 --- | --- 
Vector3 | linear
float | angular

## Methods ##

Type | Name
 --- | --- 
void | func set_zero() -> void
void | func add_scaled_accel(accel: GSTTargetAcceleration, scalar: float) -> void
float | func get_magnitude_squared() -> float
float | func get_magnitude() -> float

## Property Descriptions ##


### linear ###

```gdscript
var linear: Vector3
```

Linear acceleration

### angular ###

```gdscript
var angular: float
```

Angular acceleration

## Method Descriptions ##


### set\_zero ###

```gdscript
func set_zero() -> void
```

Sets the linear and angular components to 0.

### add\_scaled\_accel ###

```gdscript
func add_scaled_accel(accel: GSTTargetAcceleration, scalar: float) -> void
```

Adds `accel`'s components, multiplied by `scalar`, to this one.

### get\_magnitude\_squared ###

```gdscript
func get_magnitude_squared() -> float
```

Returns the squared magnitude of the linear and angular components.

### get\_magnitude ###

```gdscript
func get_magnitude() -> float
```

Returns the magnitude of the linear and angular components.