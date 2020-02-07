+++
title = "GSTProximity"
description = "Base container type that stores data to find the neighbors of an agent."
author = "razoric"
date = "2020-02-07"
aliases = ["/docs/godot-steering-toolkit/reference/classes/gstproximity/"]
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** Reference

## Description ##

Base container type that stores data to find the neighbors of an agent.

## Properties ##

Type | Name
 --- | --- 
GSTSteeringAgent | agent
Array | agents

## Methods ##

Type | Name
 --- | --- 
int | func _find_neighbors(callback: FuncRef) -> int

## Property Descriptions ##

### agent ###

{{< highlight gdscript  >}}var agent: GSTSteeringAgent{{< / highlight >}}

The owning agent whose neighbors are found in the group

### agents ###

{{< highlight gdscript  >}}var agents: Array{{< / highlight >}}

The agents who are part of this group and could be potential neighbors

## Method Descriptions ##

### \_find\_neighbors <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _find_neighbors(callback: FuncRef) -> int{{< / highlight >}}

Returns a number of neighbors based on a `callback` function.

 `_find_neighbors` calls `callback` for each agent in the `agents` array and
 adds one to the count if its `callback` returns true.