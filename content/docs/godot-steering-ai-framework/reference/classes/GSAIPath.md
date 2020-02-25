+++
title = "GSAIPath"
description = "Represents a path made up of Vector3 waypoints, split into segments path\nfollow behaviors can use."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [Reference](../reference)

## Description ##

Represents a path made up of Vector3 waypoints, split into segments path
follow behaviors can use.

## Properties ##

Type | Name
 --- | --- 
bool | is_open
float | length

## Functions ##

Type | Name
 --- | --- 
void | func create_path(waypoints: Array) -> void
float | func calculate_distance(agent_current_position: Vector3) -> float
Vector3 | func calculate_target_position(target_distance: float) -> Vector3
Vector3 | func get_start_point() -> Vector3
Vector3 | func get_end_point() -> Vector3

## Property Descriptions ##

### is\_open ###

{{< highlight gdscript  >}}var is_open: bool{{< / highlight >}}

If `false`, the path loops.

### length ###

{{< highlight gdscript  >}}var length: float{{< / highlight >}}

Total length of the path.

## Method Descriptions ##

### create\_path ###

{{< highlight gdscript  >}}func create_path(waypoints: Array) -> void{{< / highlight >}}

Creates a path from a list of waypoints.

### calculate\_distance ###

{{< highlight gdscript  >}}func calculate_distance(agent_current_position: Vector3) -> float{{< / highlight >}}

Returns the distance from `agent_current_position` to the next waypoint.

### calculate\_target\_position ###

{{< highlight gdscript  >}}func calculate_target_position(target_distance: float) -> Vector3{{< / highlight >}}

Calculates a target position from the path's starting point based on the `target_distance`.

### get\_start\_point ###

{{< highlight gdscript  >}}func get_start_point() -> Vector3{{< / highlight >}}

Returns the position of the first point on the path.

### get\_end\_point ###

{{< highlight gdscript  >}}func get_end_point() -> Vector3{{< / highlight >}}

Returns the position of the last point on the path.