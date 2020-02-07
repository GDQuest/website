+++
title = "GSTNode2DAgent"
description = "A specialized steering agent that updates itself every frame so the user does\n not have to."
author = "razoric"
date = "2020-02-06"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTNodeAgent

## Description ##

A specialized steering agent that updates itself every frame so the user does
 not have to.

## Properties ##

Type | Name
 --- | --- 
Node2D | body

## Methods ##

Type | Name
 --- | --- 
void | func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void

## Property Descriptions ##


### body ###

```gdscript
var body: Node2D
```

Setter | _set_body

The Node2D to keep track of

## Method Descriptions ##


### \_apply\_steering <small>(virtual)</small> ###

```gdscript
func _apply_steering(acceleration: GSTTargetAcceleration, delta: float) -> void
```

Moves the agent's `body` by target `acceleration`.