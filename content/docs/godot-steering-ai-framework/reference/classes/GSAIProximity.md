---
author: razoric
date: "2020-02-25"
description: Base container type that stores data to find the neighbors of an agent.
title: GSAIProximity (abstract)
---

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [Reference](../reference)

## Description ##

Base container type that stores data to find the neighbors of an agent.

## Properties ##

Type | Name
 --- | --- 
GSAISteeringAgent | agent
Array | agents

## Functions ##

Type | Name
 --- | --- 
int | func _find_neighbors(_callback: FuncRef) -> int

## Property Descriptions ##

### agent ###

{{< highlight gdscript  >}}var agent: GSAISteeringAgent{{< / highlight >}}

The owning agent whose neighbors are found in the group

### agents ###

{{< highlight gdscript  >}}var agents: Array{{< / highlight >}}

The agents who are part of this group and could be potential neighbors

## Method Descriptions ##

### \_find\_neighbors <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _find_neighbors(_callback: FuncRef) -> int{{< / highlight >}}

Returns a number of neighbors based on a `callback` function.

`_find_neighbors` calls `callback` for each agent in the `agents` array and
adds one to the count if its `callback` returns true.