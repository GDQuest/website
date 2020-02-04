+++
title = "GSTArrive"
description = "Calculates acceleration to take an agent to its target's location. The\n calculation attempts to arrive with zero remaining velocity."
author = "razoric"
date = "2020-02-04"
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

```gdscript
var target: GSTAgentLocation
```

Target agent to arrive to.

### arrival\_tolerance ###

```gdscript
var arrival_tolerance: float
```

Distance from the target for the agent to be considered successfully
 arrived.

### deceleration\_radius ###

```gdscript
var deceleration_radius: float
```

Distance from the target for the agent to begin slowing down.

### time\_to\_reach ###

```gdscript
var time_to_reach: float
```

Represents the time it takes to change acceleration.