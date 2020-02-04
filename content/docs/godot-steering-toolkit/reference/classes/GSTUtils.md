+++
title = "GSTUtils"
description = "Math and vector utility functions."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** 

## Description ##

Math and vector utility functions.

## Methods ##

Type | Name
 --- | --- 
Vector3 | func clampedv3(vector: Vector3, limit: float) -> Vector3
float | func vector3_to_angle(vector: Vector3) -> float
Vector2 | func angle_to_vector2(angle: float) -> Vector2

## Method Descriptions ##


### clampedv3 <small>(static)</small> ###

```gdscript
func clampedv3(vector: Vector3, limit: float) -> Vector3
```

Returns the `vector` with its length capped to `limit`.

### vector3\_to\_angle <small>(static)</small> ###

```gdscript
func vector3_to_angle(vector: Vector3) -> float
```

Returns an angle in radians between the positive X axis and the `vector`.

 This assumes orientation for 2D agents or 3D agents that are upright and
 rotate around the Y axis.

### angle\_to\_vector2 <small>(static)</small> ###

```gdscript
func angle_to_vector2(angle: float) -> Vector2
```

Returns a directional vector from the given orientation angle.
 
 This assumes orientation for 2D agents or 3D agents that are upright and
 rotate around the Y axis.