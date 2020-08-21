+++
title = "Writing more optimized code"
description = "A list of tips to write faster GDScript code in Godot."
author = "razoric"
menuTitle = "Optimization 3 - Write better code"

date = 2020-08-18T19:08:58-04:00
weight = 5
draft = true

difficulty = "intermediate"
keywords = ["gdscript optimization tutorial", "godot code optimizing", "godot optimization"]
+++

Some code optimizations are universal across most programming languages. Some are specific to GDScript.

## Focus optimization where it counts

An **important** disclaimer, as ever whenever talking about code optimization, is to not optimize where there is little gain. Making your `_ready` function blazing fast is all well and good, but this is something that gets called once and never again. The real gains for optimization are blocks of code that run often. A slow block of code inside a large loop is a far more important target for optimization than code that runs once.

You also do _not_ want to optimize in a vacuum. Unless you have the knowledge that some part of your code is actually slow, or is slow enough to impact the enjoyment of the game, you could be making your code harder to read for almost no gain. Run the profiler and measure your code.

_Never assume anything._ [Measure](../optimization-measure).

## Cache the results of expensive calls ahead of time

If you have an expression that always returns the same thing, you should calculate it ahead of time and put the result in a variable. A prime example in Godot is `get_node` (or its shorthand `$`). It has a cost and repeating it throughout a single frame is wasteful.

Avoid doing:

```gdscript
var direction

func _process(delta):
    var turret = $Turret

    direction = Vector2.UP.rotated(turret.rotation)
```

Prefer doing:

```gdscript
var direction

onready var turret = $Turret

func _process(delta):
    direction = Vector2.UP.rotated(turret.rotation)
```

If there is no need to call `get_node` more than once per node, then there is also no need to do more math than you need to. Cache the results of values that will stay constant throughout a loop before entering the loop.

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

## 1D array over an array of arrays

In small sizes that are not accessed often, iterating over an array of arrays is a negligible time difference measured in the order of nanoseconds. But for large arrays or arrays that you access often (or both!), the time difference adds up.

```gdscript
# 0.000009 seconds
for x in 9:
    for y in 3:
        var element = my_array[y][x]


# 0.000005 seconds
for x in 9:
    for y in 3:
        var element = my_array[y * 9 + x]

# 0.115443 seconds
for x in 1000:
    for y in 1000:
        var element = my_array[y][x]


# 0.108107 seconds
for x in 1000:
    for y in 1000:
        var element = my_array[y * 1000 + x]
```

If the order you access the elements does not matter, accessing a large 1D array sequentially instead of in a nested loop is almost twice as fast.

```gdscript
# 0.062938 seconds
for i in 1000000:
    var element = my_array[i]
```

The most interesting part comes when using Godot's native iterator instead of using indices to access elements in an array. Both 1D and 2D arrays get similar, _superior_ speeds with code like this:

```gdscript
# 0.048952 seconds
for x in 1000:
    for element in my_array[x]:
        #...

# 0.047986 seconds
for element in my_array:
    #...
```

Of course, you do not always have the luxury of accessing elements in any order, and sometimes you need the position of the element in the array for more processing. But it's a tradeoff to keep in mind.

If you want high performing arrays in GDScript, the main takeaways are:

-   1D arrays are faster than multi-dimensional arrays
-   Single loops are faster than nested loops
-   Accessing an array element with the iterator (`for element in array:`) is faster than using indices (`for i in array.size():`)

## Remove elements from the back of the array

Whenever you remove an element from an array, Godot has to resize the array. When the removed element is the last one, that's all it has to do. When the removed element is in the front or in the middle, Godot also has to move every element in its new place, and that's a slower operation.

Use `pop_back()` and `push_back()`/`append()` whenever possible when removing from or adding elements to an array.

## Use the correct data structure and algorithm

This is not a GDScript specific issue, but is one that affects all algorithms. It's also more difficult to give examples for as every algorithm will benefit differently from a good data structure.

But I can still give you a rule of thumb for GDScript in particular at the most basic level:

-   If you want to remove elements from a collection at any location at any time, prefer a Dictionary.
-   If you are going to access elements from a collection by key randomly, prefer a Dictionary.
-   If you lay your elements in order, use an Array.

Consider creating custom structure that better fit your needs. Don't be afraid to research how other people do it outside of GDScript and come up with your own version in Godot.

## Prefer debugging and breakpoints instead of printing

Calling `print()` is actually expensive. Godot has to build the string, inform the standard buffer, and display the printed data. The buffer has a finite amount of space available to it at any given time and it's easy to fill it up. When the buffer is full, it pauses while outputting what it does have, which slows Godot down even further and prompts it to give the error `[output overflow, print less text!]`.

It can have a significant impact on framerate at no benefit to the end-user.

You can get more benefit than printing by putting a breakpoint and looking at the variables. If you want to print some data for debug purposes, prefer small messages. If you want to have a large dump of data, which is useful to analyze any invisible or hard to track errors, prefer printing to a log file such as through an autoloaded singleton.

```gdscript
extends Node
onready var log = File.new()


func _ready():
    log.open("res://log.txt", File.WRITE)


func _exit_tree():
    log.close()


func print_msg(message, source):
    var current_time = OS.get_time()
    log.write_line("%s (%s:%s:%s): %s" % [source, current_time.hour, current_time.minute, current_time.second, message])
```

## Iteration over recursion

Function calls are not free and add up over time. Recursion is powerful, but deep recursion stacks can cause performance issues. You shouldn't optimize them away _just_ because you are using recursion, but if you _are_ looking to get more optimal code, consider converting them to a loop to avoid excessive numbers of function calls. The gains become significant the larger the stack.

```gdscript
func recursive_find_by_type_name(parent, type_name):
    for child in parent.get_children():
        if child.get_class() == type_name:
            return child
        else:
            var result = _find_by_type_name(child, type_name)
            if result:
                return result

    return null


func looped_find_by_type_name(parent, type_name):
    var parent_stack = [parent]

    while parent_stack.size() > 0:
        var current = parent_stack.pop_back()

        if current.get_class() == type_name:
            return current

        for child in current.get_children():
            parent_stack.push_back(child)

    return null
```

## Invert loops of function calls with a function call with a loop

As I said in the recursion example above, function calls are slower than instructions. Try to replace loops that call a function with a function that uses a loop and pass the data you need in its parameters.

```gdscript
for i in range(1000):
    do_something(i)


func do_something(x):
    #...
```

is going to be much slower than

```gdscript
    do_something()


func do_something():
    for i in range(1000):
        #...
```

## Replace if/else chains with match where possible

Long chains of if, elif and else blocks can grow in cost. Godot has to parse each condition one after the other so long as it's false. Match instead parses the value once, looks at the list of matches, and jumps to the correct one. It's faster and cleaner too.

```gdscript
if student.eye_color == "Green":
    #...
elif student.eye_color == "Blue":
    #...
elif student.eye_color == "Brown":
    #...
elif student.eye_color == "Black":
    #...
elif student.eye_color == "Red":
    #...
else:
    #...


match student.eye_color:
    "Green":
        #...
    "Blue":
        #...
    "Brown":
        #...
    "Black":
        #...
    "Red":
        #...
    _:
        #...
```

## Leave loops and functions as soon as possible

Don't do more work than you need to. As soon as you have found the value you were looking for or you have reached a point where you know for certain that the loop will always be false, try to leave it as soon as possible.

```gdscript
func get_inventory_from(container):
    if not container.inventory:
        return null

    var inventory_array = []
    for block in container.inventory:
        inventory_array.append(block.get_slots())

    if inventory_array.size() == 0:
        return null

    return parse_inventory(inventory_array)
```

## Micro-optimizations

You have some optimizations that cause large differences, like removing the elements from the back of an array or caching expensive results. Then you have the little things you probably shouldn't sweat but can be good practice. Gains here are much smaller than other optimization tips.

-   If you have a `or` or `and` boolean operation, try to put conditions that are _more likely_ to return true on the left side of `or`, and conditions that are _more likely_ to return false on the left side of `and`.
-   In `if/elif/else` chains and `match` statements, try to put the candidates that appear more commonly near the top of the chain.
-   Rephrase math to remove expensive operations. Compare `distance_squared_to` instead of `distance_to` to avoid square root. If you divide by `x` more than 3 times, pre-calculate `1/x` and multiply by that instead.

## Use GDNative

When all else fails and you've wrung every bit of performance optimization you can out of your algorithm and it's as fast as you can make it with GDScript, you're at a point where you should be investing into a C++ GDNative library.
