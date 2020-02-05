+++
title = "GSTArrive"
description = "Calculates acceleration to take an agent to its target's location. The\n calculation attempts to arrive with zero remaining velocity."
author = "razoric"
date = "2020-02-05"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSteeringBehavior

## Description ##

Calculates acceleration to take an agent to its target's location. The
 calculation attempts to arrive with zero remaining velocity.

## Properties ##

Type | Name
 --- | --- 
GSTAgentLocation | target
float | arrival_tolerance
float | deceleration_radius
float | time_to_reach

## Methods ##

Type | Name
 --- | --- 

## Property Descriptions ##


### target ###

{{< highlight gdscript  >}}var target: GSTAgentLocation{{< / highlight >}}

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