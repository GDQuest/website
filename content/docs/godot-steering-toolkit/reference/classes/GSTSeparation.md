+++
title = "GSTSeparation"
description = "Calculates an acceleration that repels the agent from its neighbors in the\n given `GSTProximity`.\n\n The acceleration is an average based on all neighbors, multiplied by a\n strength decreasing by the inverse square law in relation to distance, and it\n accumulates."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTGroupBehavior

## Description ##

Calculates an acceleration that repels the agent from its neighbors in the
 given `GSTProximity`.

 The acceleration is an average based on all neighbors, multiplied by a
 strength decreasing by the inverse square law in relation to distance, and it
 accumulates.

## Properties ##

Type | Name
 --- | --- 
float | decay_coefficient

## Methods ##

Type | Name
 --- | --- 
bool | func _report_neighbor(neighbor: GSTSteeringAgent) -> bool

## Property Descriptions ##


### decay\_coefficient ###

```gdscript
var decay_coefficient: float
```

The coefficient to calculate how fast the separation strength decays with distance.

## Method Descriptions ##


### \_report\_neighbor <small>(virtual)</small> ###

```gdscript
func _report_neighbor(neighbor: GSTSteeringAgent) -> bool
```

Callback for the proximity to call when finding neighbors. Determines the amount of
 acceleration that `neighbor` imposes based on its distance from the owner agent.