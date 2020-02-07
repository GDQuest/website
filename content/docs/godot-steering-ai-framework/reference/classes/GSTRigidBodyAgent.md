+++
title = "GSTRigidBodyAgent"
description = "A specialized steering agent that updates itself every frame so the user does\n not have to using a RigidBody"
author = "razoric"
date = "2020-02-07"
aliases = ["/docs/godot-steering-toolkit/reference/classes/gstrigidbodyagent/"]
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSpecializedAgent

## Description ##

A specialized steering agent that updates itself every frame so the user does
 not have to using a RigidBody

## Properties ##

Type | Name
 --- | --- 
RigidBody | body

## Methods ##

Type | Name
 --- | --- 
void | func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void

## Property Descriptions ##

### body ###

{{< highlight gdscript  >}}var body: RigidBody{{< / highlight >}}

Setter | _set_body

The RigidBody to keep track of

## Method Descriptions ##

### \_apply\_steering <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void{{< / highlight >}}

Moves the agent's `body` by target `acceleration`.