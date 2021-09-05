---
author: razoric
date: "2020-02-25"
description: |-
  A specialized steering agent that updates itself every frame so the user does
  not have to using a RigidBody2D
title: GSAIRigidBody2DAgent
---

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAISpecializedAgent](../gsaispecializedagent) < [GSAISteeringAgent](../gsaisteeringagent) < [GSAIAgentLocation](../gsaiagentlocation)

## Description ##

A specialized steering agent that updates itself every frame so the user does
not have to using a RigidBody2D

## Properties ##

Type | Name
 --- | --- 
RigidBody2D | body

## Functions ##

Type | Name
 --- | --- 
void | func _apply_steering(acceleration: GSAITargetAcceleration, _delta: float) -> void

## Property Descriptions ##

### body ###

{{< highlight gdscript  >}}var body: RigidBody2D{{< / highlight >}}

Setter | _set_body

The RigidBody2D to keep track of

## Method Descriptions ##

### \_apply\_steering <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _apply_steering(acceleration: GSAITargetAcceleration, _delta: float) -> void{{< / highlight >}}

Moves the agent's `body` by target `acceleration`.