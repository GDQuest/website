+++
title = "GSAIFollowPath"
description = "Produces a linear acceleration that moves the agent along the specified path."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAIArrive](../gsaiarrive) < [GSAISteeringBehavior](../gsaisteeringbehavior)

## Description ##

Produces a linear acceleration that moves the agent along the specified path.

## Properties ##

Type | Name
 --- | --- 
GSAIPath | path
float | path_offset
bool | is_arrive_enabled
float | prediction_time

## Property Descriptions ##

### path ###

{{< highlight gdscript  >}}var path: GSAIPath{{< / highlight >}}

The path to follow and travel along.

### path\_offset ###

{{< highlight gdscript  >}}var path_offset: float{{< / highlight >}}

The distance along the path to generate the next target position.

### is\_arrive\_enabled ###

{{< highlight gdscript  >}}var is_arrive_enabled: bool{{< / highlight >}}

Whether to use `GSAIArrive` behavior on an open path.

### prediction\_time ###

{{< highlight gdscript  >}}var prediction_time: float{{< / highlight >}}

The amount of time in the future to predict the owning agent's position along
the path. Setting it to 0.0 will force non-predictive path following.