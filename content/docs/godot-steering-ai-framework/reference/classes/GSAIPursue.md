---
author: razoric
date: "2020-02-25"
description: |-
  Calculates an acceleration to make an agent intercept another based on the
  target agent's movement.
title: GSAIPursue
---

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAISteeringBehavior](../gsaisteeringbehavior)

## Description ##

Calculates an acceleration to make an agent intercept another based on the
target agent's movement.

## Properties ##

Type | Name
 --- | --- 
GSAISteeringAgent | target
float | predict_time_max

## Property Descriptions ##

### target ###

{{< highlight gdscript  >}}var target: GSAISteeringAgent{{< / highlight >}}

The target agent that the behavior is trying to intercept.

### predict\_time\_max ###

{{< highlight gdscript  >}}var predict_time_max: float{{< / highlight >}}

The maximum amount of time in the future the behavior predicts the target's
location.