+++
title = "GSTTargetAcceleration"
description = "A desired linear and angular amount of acceleration requested by the steering\n system."
author = "razoric"
date = "2020-02-07"
aliases = ["/docs/godot-steering-toolkit/reference/classes/gsttargetacceleration/"]
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

{{< highlight gdscript  >}}var linear: Vector3{{< / highlight >}}

Linear acceleration

### angular ###

{{< highlight gdscript  >}}var angular: float{{< / highlight >}}

Angular acceleration

## Method Descriptions ##

### set\_zero ###

{{< highlight gdscript  >}}func set_zero() -> void{{< / highlight >}}

Sets the linear and angular components to 0.

### add\_scaled\_accel ###

{{< highlight gdscript  >}}func add_scaled_accel(accel: GSTTargetAcceleration, scalar: float) -> void{{< / highlight >}}

Adds `accel`'s components, multiplied by `scalar`, to this one.

### get\_magnitude\_squared ###

{{< highlight gdscript  >}}func get_magnitude_squared() -> float{{< / highlight >}}

Returns the squared magnitude of the linear and angular components.

### get\_magnitude ###

{{< highlight gdscript  >}}func get_magnitude() -> float{{< / highlight >}}

Returns the magnitude of the linear and angular components.