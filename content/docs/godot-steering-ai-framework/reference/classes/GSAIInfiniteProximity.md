+++
title = "GSAIInfiniteProximity"
description = "Determines any agent that is in the specified list as being neighbors with the\nowner agent, regardless of distance."
author = "razoric"
date = "2020-02-25"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** [GSAIProximity](../gsaiproximity) < [Reference](../reference)

## Description ##

Determines any agent that is in the specified list as being neighbors with the
owner agent, regardless of distance.

## Functions ##

Type | Name
 --- | --- 
int | func _find_neighbors(callback: FuncRef) -> int

## Method Descriptions ##

### \_find\_neighbors <small>(virtual)</small> ###

{{< highlight gdscript  >}}func _find_neighbors(callback: FuncRef) -> int{{< / highlight >}}

Returns a number of neighbors based on a `callback` function.

`_find_neighbors` calls `callback` for each agent in the `agents` array and
adds one to the count if its `callback` returns true.