---
author: razoric
coAuthors:
- nathan
date: "2020-08-18T19:08:58-04:00"
description: A list of tips to write faster GDScript code in Godot.
difficulty: intermediate
keywords:
- gdscript optimization tutorial
- godot code optimizing
- godot optimization
title: Optimizing GDScript code
weight: 5
---

Some code optimizations are universal across most programming languages. Some are specific to GDScript.

In this guide, we share some general tips and GDScript-specific techniques to improve your code's execution speed in Godot 3.2.

{{< note >}}
We recommend you only optimize code you know is slowing down the game or hurting your players' experience. You should always use the profiler and measure how specific functions impact performances.

Things such as improvements to the GDScript compiler may remove the need for some of these optimizations.

To learn to use it and measure your code's performances, read our [Godot profiler guide]({{< ref "tutorial/godot/gdscript/optimization-measure/index.md" >}}).
{{< /note >}}

## Cache expensive calls ahead of time

Suppose you have an expression that always returns the same value. In that case, you should execute it ahead of time and store the result in a variable. A prime example in Godot is `get_node()` or its shorthand `$`. If there is no need to call `get_node()` more than once per node. It has a cost, and repeating it throughout a single frame is wasteful.

Avoid:

```gdscript
var direction

func _process(delta):
    var turret = $Turret

    direction = Vector2.UP.rotated(turret.rotation)
```

Prefer:

```gdscript
var direction

onready var turret = $Turret

func _process(delta):
    direction = Vector2.UP.rotated(turret.rotation)
```

Then, there is also no need to do more math than you need to. Cache the results of values that will stay constant throughout a loop before entering the loop.

```gdscript
# Slow
var alloy_strength = 1.0
var alloy_thickness = 5.0
var alloy_layers = 15.0

for robot in army:
    robot.armor = pow(alloy_strength * alloy_thickness, alloy_layers) + robot.native_armor


# Faster
var alloy_strength = 1.0
var alloy_thickness = 5.0
var alloy_layers = 15.0

# Here, we're calculating the base armor rating of robots outside of the loop
var base_armor = pow(alloy_strength * alloy_thickness, alloy_layers)

for robot in army:
    robot.armor = base_armor + robot.native_armor
```

## 1D array over an array of arrays

In small arrays that are not accessed often, iterating over nested arrays over a single array is negligible. But for large sets of data or arrays you access frequently, the time difference adds up.

```gdscript
# 0.115443 seconds
for x in 1000:
    for y in 1000:
        var element = my_array[y][x]


# 0.108107 seconds
for x in 1000:
    for y in 1000:
        var element = my_array[y * 1000 + x]


# 0.062938 seconds, about 45% faster than the first example
for i in 1000000:
    var element = my_array[i]
```

The most interesting part comes when using Godot's native iterator instead of using indices to access an array's elements. Both 1D and 2D arrays get similar, _superior_ speeds with code like this:

```gdscript
# 0.048952 seconds, almost 60% faster than the first example
for x in 1000:
    for element in my_array[x]:
        #...

# 0.047986 seconds
for element in my_array:
    #...
```

Of course, you do not always have the luxury of accessing elements in any order. Sometimes, you need to know the position of the element in the array for more processing. But it's a tradeoff to keep in mind.

If you want high performing arrays in GDScript, the main takeaways are:

- 1D arrays are faster than multi-dimensional arrays
- Single loops are faster than nested loops
- Accessing an array element with the iterator `for element in array` is faster than using indices, e.g. `for i in array.size()`.

## Remove elements from the back of the array

Whenever you add or remove an element at a given position within an array, Godot has to resize the array and move all its elements. The cost of this operation is proportional to the number of entries in the array. When the removed element is the last one, the engine only needs to resize the array, discarding the last value.

Favor `pop_back()` and `push_back()` or `append()` when removing or adding elements to an array. Avoid `pop_front()` and `push_front()`.

## Use the correct data structure and algorithm for the job

Choosing the right data structure is not a GDScript-specific issue, but the data structures you use affects all algorithms.

Here are three rules of thumb for choosing data structures with GDScript:

- If you want to remove elements from a collection at any location and at any time, use a `Dictionary`.
- If you will access elements from a collection by key randomly, use a `Dictionary`.
- If you lay your elements in order, use an `Array`.

For more information, read the [Data preferences](https://docs.godotengine.org/en/stable/getting_started/workflow/best_practices/data_preferences.html) page in the official manual.

## Use breakpoints instead of printing

Calling the `print()` function is expensive. You don't want to export your games with many print statements left in.

Instead, you can use [the built-in debugger]({{< ref "tutorial/godot/gdscript/debugging/index.md" >}}) to inspect your game at runtime. Another option is to call `print_debug()`, which only runs in your game's debug builds or when testing it from the editor.

{{< note >}}
Printing is slow because Godot has to build the string, pass it to the standard input, and display the printed data. The call to `print()` involves passing data to your computer's peripherals, like the display, which is slow. The print buffer also has a finite amount of space available, and it easy to fill it up. When the buffer is full, it pauses while outputting its content, which slows Godot down even further and prompts it to give the error `[output overflow, print less text!]`.
{{< /note >}}

It can have a significant impact on the framerate at no benefit to the end-user.

If you want to read a large dump of text or data, which is useful to analyze errors that are hard to track down, output text to a log file. You can do so by creating an [Autoload](https://docs.godotengine.org/en/stable/getting_started/step_by_step/singletons_autoload.html) dedicated to logging:

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

## Favor iteration over recursion

Every time you call a function, the compiler creates an object to store some information about it. One piece of information is which function called the current one, allowing the compiler to return to the caller. Recursion, that is to say, having a function call itself, causes these objects to stack up.

Recursion can be powerful and lead to code that's easy to read. For small recursion loops, the performance impact is negligible. You shouldn't optimize them away _just_ because you are using recursion. But if you _are_ looking to get more optimal code, consider converting recursive functions to a loop to avoid excessive calls.

```gdscript
# Loop over nodes recursively to find one of a given type.
# This is a recursive function as it calls itself.
func find_by_type_name_recursive(parent, type_name):
    for child in parent.get_children():
        if child.get_class() == type_name:
            return child
        else:
            var result = find_by_type_name_recursive(child, type_name)
            if result:
                return result

    return null

# Same as the previous function but using a while loop.
# The deeper the scene tree, the higher the performance gain.
func find_by_type_name(parent, type_name):
    var parent_stack = [parent]

    while parent_stack.size() > 0:
        var current = parent_stack.pop_back()

        if current.get_class() == type_name:
            return current

        for child in current.get_children():
            parent_stack.push_back(child)

    return null
```

## Avoid loops of function calls

Function calls are slower than instructions as the compiler needs to store some state for them. Instead of calling a function many times in a loop, putting the loop inside a single function is significantly faster.

```gdscript
var tiles = []
for i in range(1000):
    # We're calling `create_random_tile` one thousand times
    var new_tile = create_random_tile()
    tiles.append(new_tile)


func create_random_tile():
    #...
```

Is going to be much slower than:

```gdscript
# Here, we only have one function call
var tiles = create_random_tiles()


func create_random_tiles():
    var tiles = []
    for i in range(1000):
        # ...
    return tiles
```

## Conditional chains are 20% faster than match

You can use the `match` keyword as an equivalent of chains of if, elif, else statements. They can look a bit like `case` statements in some languages. Currently though, `match` is a little slower than `if` for equivalent code. In my tests, the speed difference was about 15% to 20%.

```gdscript
match student.eye_color:
    "Green":
        #...
    "Blue":
        #...
    "Brown":
        #...
    "Black":
        #...
    _:
        #...

# About 20% faster than the code above.
if student.eye_color == "Green":
    #...
elif student.eye_color == "Blue":
    #...
elif student.eye_color == "Brown":
    #...
elif student.eye_color == "Black":
    #...
else:
    #...


```

{{< note >}}
As always, the difference in execution speed is negligible in code that only runs once. It only starts to add up in loops.
{{< /note >}}

## Leave loops and functions as soon as possible

Use the `return` keyword in functions or `continue` and `break` in loops to skip instructions you don't need to run.

As soon as you have found the value you were looking, try to leave it as soon as possible.

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

You have some optimizations that cause large differences, like removing the elements from the back of an array or caching expensive results. Then, you have the little things you probably shouldn't sweat but can be good practices. Gains here are much smaller than with previous optimization tips.

Here are three examples:

1.  If you have a `or` or `and` boolean operation, try to put conditions that are _more likely_ to return true on the left side of `or`, and conditions that are _more likely_ to return false on the left side of `and`.
1.  In conditional chains or `match` statements, try to put the candidates that appear more commonly near the chain's top.
1.  Rephrase math to remove expensive operations. Compare `distance_squared_to` instead of `distance_to` to avoid a square root operation. If you divide by a value more than three times, pre-calculate that and store it in a variable.

## Use GDNative

Even with all the optimization you try to add, GDScript might fail you with performance-intensive algorithms, like heavy procedural generation or heatmap pathfinding.

If this happens, you will want to look into using either C# or C++ [GDNative](https://docs.godotengine.org/en/stable/tutorials/plugins/gdnative/gdnative-cpp-example.html) libraries.
