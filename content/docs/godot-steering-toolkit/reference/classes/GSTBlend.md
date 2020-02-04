+++
title = "GSTBlend"
description = "Blends multiple steering behaviors into one, and returns a weighted\n acceleration from their calculations.\n\n Stores the behaviors internally as dictionaries of the form\n {\n 	behavior : GSTSteeringBehavior,\n 	weight : float\n }"
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSteeringBehavior

## Description ##

Blends multiple steering behaviors into one, and returns a weighted
 acceleration from their calculations.

 Stores the behaviors internally as dictionaries of the form
 {
 	behavior : GSTSteeringBehavior,
 	weight : float
 }

## Methods ##

Type | Name
 --- | --- 
void | func add(behavior: GSTSteeringBehavior, weight: float) -> void
Dictionary | func get_behavior_at(index: int) -> Dictionary

## Method Descriptions ##


### add ###

```gdscript
func add(behavior: GSTSteeringBehavior, weight: float) -> void
```

Appends a behavior to the internal array along with its `weight`.

### get\_behavior\_at ###

```gdscript
func get_behavior_at(index: int) -> Dictionary
```

Returns the behavior at the specified `index`, or an empty `Dictionary` if
 none was found.