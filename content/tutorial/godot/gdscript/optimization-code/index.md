+++
title = "Optimization Code"
description = ""
author = "razoric"

date = 2020-08-18T19:08:58-04:00
weight = 5
draft = true

difficulty = "beginner"
keywords = ["tutorial"]
+++

## Focus optimization where it counts

An **important** disclaimer, as ever whenever talking about code optimization, is to not optimize where there is little gain. Making your `_ready` function blazing fast is all well and good, but this is something that gets called once and never again. The real gains for optimization are blocks of code that run often. A slow block of code inside a large loop is a far more important target for optimization than code that runs once.

You also do _not_ want to optimize in a vacuum. Unless you have the knowledge that some part of your code is actually slow, or is slow enough to impact the enjoyment of the game, you could be making your code harder to read for almost no gain. Run the profiler and measure your code.

## Avoid fetching nodes as needed. Cache calls to get_node

```gdscript
onready var timer = $Timer
```

## 1D arrays over 2D arrays

```gdscript
for x in range(50):
    for y in range(50):
        var element = my_array[y * width + x]
```

## Print lumps of data all at once instead of over time

```gdscript
var output = "["

for i in range(1000):
    output += "%s, " % get_some_string(i)

output += "]"

print(output)
```

## Arrays or Dictionaries

Arrays for sequences and iteration. Avoid removing elements from anywhere but the end of the array.

Dictionary for random access.

## Classes or Dictionaries

Classes that don't require functions or don't need to maintain/update a state can be dictionaries.

## Iteration over recursion

Recursion results in function calls which are not cheap. Try to convert recursive function calls into a loop.

## Invert loops of function calls with a function call with a loop

```gdscript
    # SLOW
    for i in range(1000):
        do_something(i)

    # FASTER
    do_something()


func do_something():
    for i in range(1000):
        #...
```

## Replace if/else chains with match where possible

## Do constant work before entering a loop

```gdscript
# SLOW
var alloy_strength = 1
var alloy_thickness = 5
var alloy_layers = 15

for robot in army:
    robot.armor = pow(alloy_strength * alloy_thickness, alloy_layers) + robot.native_armor


# FASTER
var alloy_strength = 1
var alloy_thickness = 5
var alloy_layers = 15

var base_armor = pow(alloy_strength * alloy_thickness, alloy_layers)

for robot in army:
    robot.armor = base_armor + robot.native_armor
```

## Leave loops and functions as soon as possible

Don't do more work than you need to.

## Micro-optimizations

### Reduce integer division

### Simplify expressions

### Order of boolean operations

`or` prefers something that will probably be true first

`and` prefers something that will probably be false first

### Bit-shift instead of power-of-2 multiplication or division

## Use GDNative

When all else fails and you've wrung every bit of performance optimization you can out of your algorithm and it's as fast as you can make it with GDScript, you're at a point where you should be investing into a C++ GDNative library.
