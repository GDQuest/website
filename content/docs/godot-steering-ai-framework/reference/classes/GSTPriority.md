+++
title = "GSTPriority"
description = "Container for multiple behaviors that returns the result of the first child\n behavior with non-zero acceleration."
author = "razoric"
date = "2020-02-07"
aliases = ["/docs/godot-steering-toolkit/reference/classes/gstpriority/"]
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSteeringBehavior

## Description ##

Container for multiple behaviors that returns the result of the first child
 behavior with non-zero acceleration.

## Properties ##

Type | Name
 --- | --- 
int | last_selected_index
float | zero_threshold

## Methods ##

Type | Name
 --- | --- 
void | func add(behavior: GSTSteeringBehavior) -> void
GSTSteeringBehavior | func get_behavior_at(index: int) -> GSTSteeringBehavior

## Property Descriptions ##

### last\_selected\_index ###

{{< highlight gdscript  >}}var last_selected_index: int{{< / highlight >}}

The index of the last behavior the container prioritized.

### zero\_threshold ###

{{< highlight gdscript  >}}var zero_threshold: float{{< / highlight >}}

If a behavior's acceleration is lower than this threshold, the container
 considers it has an acceleration of zero.

## Method Descriptions ##

### add ###

{{< highlight gdscript  >}}func add(behavior: GSTSteeringBehavior) -> void{{< / highlight >}}

Appends a steering behavior as a child of this container.

### get\_behavior\_at ###

{{< highlight gdscript  >}}func get_behavior_at(index: int) -> GSTSteeringBehavior{{< / highlight >}}

Returns the behavior at the position in the pool referred to by `index`, or
 `null` if no behavior was found.