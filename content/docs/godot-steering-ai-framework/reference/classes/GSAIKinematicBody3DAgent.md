+++
title = "GSAIKinematicBody3DAgent"
description = "A specialized steering agent that updates itself every frame so the user does\nnot have to using a KinematicBody"
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAISpecializedAgent](../gsaispecializedagent) < [GSAISteeringAgent](../gsaisteeringagent) < [GSAIAgentLocation](../gsaiagentlocation)

## Description ##

A specialized steering agent that updates itself every frame so the user does
not have to using a KinematicBody

## Properties ##

Type | Name
 --- | --- 
KinematicBody | body
int | movement_type

## Functions ##

Type | Name
 --- | --- 
void | func _apply_steering(acceleration: GSAITargetAcceleration, delta: float) -> void

## Enumerations ##

### MovementType ###

{{< highlight gdscript  >}}const MovementType: Dictionary = {"COLLIDE":1,"POSITION":2,"SLIDE":0}{{< / highlight >}}

## Property Descriptions ##

### body ###

{{< highlight gdscript  >}}var body: KinematicBody{{< / highlight >}}

Setter | _set_body

The KinematicBody to keep track of

### movement\_type ###

{{< highlight gdscript  >}}var movement_type: int{{< / highlight >}}

The type of movement the body executes

## Method Descriptions ##

### \_apply\_steering <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _apply_steering(acceleration: GSAITargetAcceleration, delta: float) -> void{{< / highlight >}}

Moves the agent's `body` by target `acceleration`.