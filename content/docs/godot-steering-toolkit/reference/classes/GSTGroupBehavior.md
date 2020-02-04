+++
title = "GSTGroupBehavior"
description = "Base type for group-based steering behaviors."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTSteeringBehavior

## Description ##

Base type for group-based steering behaviors.

## Properties ##

Type | Name
 --- | --- 
GSTProximity | proximity

## Methods ##

Type | Name
 --- | --- 
bool | func _report_neighbor(neighbor: GSTSteeringAgent) -> bool

## Property Descriptions ##


### proximity ###

```gdscript
var proximity: GSTProximity
```

Container to find neighbors of the agent and calculate group behavior.

## Method Descriptions ##


### \_report\_neighbor <small>(virtual)</small> ###

```gdscript
func _report_neighbor(neighbor: GSTSteeringAgent) -> bool
```

Internal callback for the behavior to define whether or not a member is
 relevant