+++
title = "GSTKinematicBodyAgent"
description = "A specialized steering agent that updates itself every frame so the user does\n not have to using a KinematicBody"
author = "razoric"
date = "2020-02-07"
aliases = ["/docs/godot-steering-toolkit/reference/classes/gstkinematicbodyagent/"]
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSpecializedAgent

## Description ##

A specialized steering agent that updates itself every frame so the user does
 not have to using a KinematicBody

## Properties ##

Type | Name
 --- | --- 
KinematicBody | body
int | movement_type

## Methods ##

Type | Name
 --- | --- 
void | func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void

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

{{< highlight gdscript  >}}func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void{{< / highlight >}}

Moves the agent's `body` by target `acceleration`.