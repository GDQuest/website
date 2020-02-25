+++
title = "GSAISeparation"
description = "Calculates an acceleration that repels the agent from its neighbors in the\ngiven `GSAIProximity`.\n\nThe acceleration is an average based on all neighbors, multiplied by a\nstrength decreasing by the inverse square law in relation to distance, and it\naccumulates."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAIGroupBehavior](../gsaigroupbehavior) < [GSAISteeringBehavior](../gsaisteeringbehavior)

## Description ##

Calculates an acceleration that repels the agent from its neighbors in the
given `GSAIProximity`.

The acceleration is an average based on all neighbors, multiplied by a
strength decreasing by the inverse square law in relation to distance, and it
accumulates.

## Properties ##

Type | Name
 --- | --- 
float | decay_coefficient

## Functions ##

Type | Name
 --- | --- 
bool | func _report_neighbor(neighbor: GSAISteeringAgent) -> bool

## Property Descriptions ##

### decay\_coefficient ###

{{< highlight gdscript  >}}var decay_coefficient: float{{< / highlight >}}

The coefficient to calculate how fast the separation strength decays with distance.

## Method Descriptions ##

### \_report\_neighbor <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _report_neighbor(neighbor: GSAISteeringAgent) -> bool{{< / highlight >}}

Callback for the proximity to call when finding neighbors. Determines the amount of
acceleration that `neighbor` imposes based on its distance from the owner agent.