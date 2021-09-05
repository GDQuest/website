---
author: razoric
date: "2020-02-25"
description: |-
  Calculates acceleration to take an agent to its target's location. The
  calculation attempts to arrive with zero remaining velocity.
title: GSAIArrive
---

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAISteeringBehavior](../gsaisteeringbehavior)

## Description ##

Calculates acceleration to take an agent to its target's location. The
calculation attempts to arrive with zero remaining velocity.

## Properties ##

Type | Name
 --- | --- 
GSAIAgentLocation | target
float | arrival_tolerance
float | deceleration_radius
float | time_to_reach

## Property Descriptions ##

### target ###

{{< highlight gdscript  >}}var target: GSAIAgentLocation{{< / highlight >}}

Target agent to arrive to.

### arrival\_tolerance ###

{{< highlight gdscript  >}}var arrival_tolerance: float{{< / highlight >}}

Distance from the target for the agent to be considered successfully
arrived.

### deceleration\_radius ###

{{< highlight gdscript  >}}var deceleration_radius: float{{< / highlight >}}

Distance from the target for the agent to begin slowing down.

### time\_to\_reach ###

{{< highlight gdscript  >}}var time_to_reach: float{{< / highlight >}}

Represents the time it takes to change acceleration.