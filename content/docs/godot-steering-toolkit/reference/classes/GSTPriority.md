+++
title = "GSTPriority"
description = "Container for multiple behaviors that returns the result of the first child\n behavior with non-zero acceleration."
author = "razoric"
date = "2020-02-04"
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

```gdscript
var last_selected_index: int
```

The index of the last behavior the container prioritized.

### zero\_threshold ###

```gdscript
var zero_threshold: float
```

If a behavior's acceleration is lower than this threshold, the container
 considers it has an acceleration of zero.

## Method Descriptions ##


### add ###

```gdscript
func add(behavior: GSTSteeringBehavior) -> void
```

Appends a steering behavior as a child of this container.

### get\_behavior\_at ###

```gdscript
func get_behavior_at(index: int) -> GSTSteeringBehavior
```

Returns the behavior at the position in the pool referred to by `index`, or
 `null` if no behavior was found.