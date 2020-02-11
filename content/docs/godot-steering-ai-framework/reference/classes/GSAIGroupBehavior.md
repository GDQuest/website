+++
title = "GSAIGroupBehavior"
description = "Base type for group-based steering behaviors."
author = "razoric"
date = "2020-02-11"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSAISteeringBehavior

## Description ##

Base type for group-based steering behaviors.

## Properties ##

Type | Name
 --- | --- 
GSAIProximity | proximity

## Methods ##

Type | Name
 --- | --- 
bool | func _report_neighbor(_neighbor: GSAISteeringAgent) -> bool

## Property Descriptions ##

### proximity ###

{{< highlight gdscript  >}}var proximity: GSAIProximity{{< / highlight >}}

Container to find neighbors of the agent and calculate group behavior.

## Method Descriptions ##

### \_report\_neighbor <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _report_neighbor(_neighbor: GSAISteeringAgent) -> bool{{< / highlight >}}

Internal callback for the behavior to define whether or not a member is
 relevant