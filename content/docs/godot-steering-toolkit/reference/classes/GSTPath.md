+++
title = "GSTPath"
description = "Represents a path made up of Vector3 waypoints, split into segments path\n follow behaviors can use."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** Reference

## Description ##

Represents a path made up of Vector3 waypoints, split into segments path
 follow behaviors can use.

## Properties ##

Type | Name
 --- | --- 
bool | is_open
float | length

## Methods ##

Type | Name
 --- | --- 
void | func create_path(waypoints: Array) -> void
float | func calculate_distance(agent_current_position: Vector3) -> float
Vector3 | func calculate_target_position(target_distance: float) -> Vector3
Vector3 | func get_start_point() -> Vector3
Vector3 | func get_end_point() -> Vector3

## Property Descriptions ##


### is\_open ###

```gdscript
var is_open: bool
```

If `false`, the path loops.

### length ###

```gdscript
var length: float
```

Total length of the path.

## Method Descriptions ##


### create\_path ###

```gdscript
func create_path(waypoints: Array) -> void
```

Creates a path from a list of waypoints.

### calculate\_distance ###

```gdscript
func calculate_distance(agent_current_position: Vector3) -> float
```

Returns the distance from `agent_current_position` to the next waypoint.

### calculate\_target\_position ###

```gdscript
func calculate_target_position(target_distance: float) -> Vector3
```

Calculates a target position from the path's starting point based on the `target_distance`.

### get\_start\_point ###

```gdscript
func get_start_point() -> Vector3
```

Returns the position of the first point on the path.

### get\_end\_point ###

```gdscript
func get_end_point() -> Vector3
```

Returns the position of the last point on the path.