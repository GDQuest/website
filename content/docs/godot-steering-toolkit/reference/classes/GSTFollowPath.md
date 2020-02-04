+++
title = "GSTFollowPath"
description = "Produces a linear acceleration that moves the agent along the specified path."
author = "razoric"
date = "2020-02-04"
+++

<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

**Extends:** GSTArrive

## Description ##

Produces a linear acceleration that moves the agent along the specified path.

## Properties ##

Type | Name
 --- | --- 
GSTPath | path
float | path_offset
bool | is_arrive_enabled
float | prediction_time

## Methods ##

Type | Name
 --- | --- 

## Property Descriptions ##


### path ###

```gdscript
var path: GSTPath
```

The path to follow and travel along.

### path\_offset ###

```gdscript
var path_offset: float
```

The distance along the path to generate the next target position.

### is\_arrive\_enabled ###

```gdscript
var is_arrive_enabled: bool
```

Whether to use `GSTArrive` behavior on an open path.

### prediction\_time ###

```gdscript
var prediction_time: float
```

The amount of time in the future to predict the owning agent's position along
 the path. Setting it to 0.0 will force non-predictive path following.