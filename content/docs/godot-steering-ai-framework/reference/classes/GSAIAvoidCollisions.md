+++
title = "GSAIAvoidCollisions"
description = "Steers the agent to avoid obstacles in its path. Approximates obstacles as\nspheres."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAIGroupBehavior](../gsaigroupbehavior) < [GSAISteeringBehavior](../gsaisteeringbehavior)

## Description ##

Steers the agent to avoid obstacles in its path. Approximates obstacles as
spheres.

## Functions ##

Type | Name
 --- | --- 
bool | func _report_neighbor(neighbor: GSAISteeringAgent) -> bool

## Method Descriptions ##

### \_report\_neighbor <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _report_neighbor(neighbor: GSAISteeringAgent) -> bool{{< / highlight >}}

Callback for the proximity to call when finding neighbors. Keeps track of every `neighbor`
that was found but only keeps the one the owning agent will most likely collide with.