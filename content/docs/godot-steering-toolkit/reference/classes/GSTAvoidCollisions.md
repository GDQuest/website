+++
title = "GSTAvoidCollisions"
description = "Steers the agent to avoid obstacles in its path. Approximates obstacles as\n spheres."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTGroupBehavior

## Description ##

Steers the agent to avoid obstacles in its path. Approximates obstacles as
 spheres.

## Methods ##

Type | Name
 --- | --- 
bool | func _report_neighbor(neighbor: GSTSteeringAgent) -> bool

## Method Descriptions ##


### \_report\_neighbor <small>(virtual)</small> ###

```gdscript
func _report_neighbor(neighbor: GSTSteeringAgent) -> bool
```

Callback for the proximity to call when finding neighbors. Keeps track of every `neighbor`
 that was found but only keeps the one the owning agent will most likely collide with.