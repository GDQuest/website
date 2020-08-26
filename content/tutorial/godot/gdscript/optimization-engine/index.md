+++
title = "Making the most of Godot's speed"
description = "A list of tips to reduce the amount of manual work you do and use the speed of Godot's C++."
author = "razoric"
coAuthors = ["nathan"]
menuTitle = "Using Godot's Speed"

date = 2020-08-18T11:07:59-04:00
weight = 4

difficulty = "intermediate"
keywords = ["gdscript optimization tutorial", "godot code optimizing", "godot optimization"]
+++

To make a game run fast, you need your code to run fast too. You can try to write optimized GDSCript patterns to get decent performances. But there is often a better way that makes your code run faster and with less effort: letting Godot do the work for you.

## GDScript, Godot, and C++

Every feature built into the engine relies on _compiled_, native, and fast C++ code. The engine's code also tends to get faster and more stable over time, as many contributors optimize it. In GDScript, every function that you did not code yourself calls the C++ code. As a result, you can have much faster code by using Godot's built-in functions and objects instead of writing them yourself.

On the other hand, GDScript is an interpreted language. In Godot 3.2, it runs about as fast as interpreted Python, so it is probably two orders of magnitude slower than compiled C++.

By relying on built-in nodes and features:

1. You have to write less code.
2. You get code that is shorter and easier to read.
3. Your game runs faster.

## Optimize when it makes a difference

A necessary disclaimer: only optimize code when it makes a measurable difference. Optimizing for no gain in the player's experience is a waste of time.

For example, functions like `_ready()` only get called once upon adding a node to the scene tree. The real performance gains are in blocks of code that run often, or in performance-intensive code, like procedural world generation. In general, a slow block of code inside a loop should be a priority target for optimization.

You also do _not_ want to optimize in a vacuum. Unless you know that some part of your code impacts the game's performances, do not optimize it. Optimizing code generally increases its complexity and reduces your ability to change it later.

{{< note >}}
You should always run the profiler and measure your code's execution speed before optimizing a function. To learn to use it and measure your code's performances, read our [profiler guide]({{< ref "tutorial/godot/gdscript/optimization-measure/index.md" >}}).
{{< / note >}}

## Make the engine work for you

Let's look at a non-exhaustive list of tips for some common tasks the engine can do for you.

## Use built-in math functions over manual calculations

GDScript exposes a library of functions to do math calculations. Explore @GDScript in the built-in class reference to find functions built into the language. You should use those instead of manually calculating values whenever possible. Here are a few common ones.

Checking if a value is negative or positive:

```gdscript
# Slow
var result = 0
if value < 0:
    result = -1
elif value > 0:
    result = 1

# Fast
result = sign(value)
```

Remapping a value from the [current_min, current_max] range to [intended_min, intended_max] range:

```gdscript
# Slow
value = (value - current_min) / (current_max - current_min) * (intended_max - intended_min) - intended_min

# Fast
value = range_lerp(value, current_min, current_max, intended_min, intended_max)
```

Finding the next power of two:

```gdscript
# Slow
value = pow(2, ceil(log(value) / log(2)))

# Fast
value = nearest_po2(value)
```

## Favor instancing scenes

It's common to manually build scene trees because you want to have a custom node set up for each entity you create. But calling `new()` and `add_child()` one at a time means many separate function calls into the engine. Doing so is a lot slower than instancing a `PackedScene` with its `instance()` method.

```gdscript
# Slow: building the scene in GDScript
var CustomBody = preload("res://player/TimedKinematic.gd")
var body = CustomBody.new()

var circle_shape = CircleShape2D.new()
circle_shape.radius = 30.0

var collider = CollisionShape2D.new()
collider.shape = circle_shape

var timer = Timer.new()
timer.process_mode = Timer.TIMER_PROCESS_PHYSICS
timer.wait_time = 3.0
timer.autostart = false
timer.one_shot = true

body.add_child(collider)
body.add_child(timer)
timer.connect("timeout", body, "_on_Timer_timeout")

add_child(body)

# Fast: Build a script with a kinematic body 2D circle with a timer
var body = preload("res://player/TimedKinematic.tscn").instance()
add_child(body)
```

Look at how you are creating node trees and try to find common elements. If they all follow the same template but have different properties, save the node branch as a scene and instance it. You can always change some of the instance's properties at runtime, using GDScript.

```gdscript
var body = preload("res://Shared/KinematicActor.tscn").instance()

var enemy_behavior = preload("res://Enemies/EnemyBehavior.gd").new()
body.behavior = enemy_behavior

add_child(body)
```

## Use Area nodes to find the nearest neighbor

Finding the nearest object is a common task for path-finding, AI targeting, or interactive switches. When you are not dealing with physics, it can be tempting to check for distances between objects to find the nearest one.

Here's a code example that does so by looping over all interactive objects in the current level:

```gdscript
# Slow: 
var interactive_objects = get_tree().find_nodes_in_group("interactive")
var minimum_distance = INF
var nearest_object

var current_position = global_transform().origin

for object in interactive_objects:
    var distance = object.global_transform.origin.distance_to(current_position)
    if distance < minimum_distance:
        minimum_distance = distance
        nearest_object = object

return object
```

Depending on the number of interactive objects in your scene, it can run fine or be an utter disaster.

Imagine a puzzle room where you can pick up every piece of bread, spoon, plate, or wheel of cheese! Instead, you can attach an `Area` node to the objects with which you can interact and add an `Area` node to the player's interaction detector. Let the physics engine find objects for you and filter out the rest. Physics engines can have many optimizations like splitting the world in a grid to compare with few as few objects as possible.

The following code finds the nearest interactive object that is close to the player, using an area.

```gdscript
# Fast: 
var interactive_objects = interact_area.get_overlapping_areas()

var minimum_distance = INF
var nearest_object

var current_position = global_transform().origin

for object in interactive_objects:
    var distance = object.global_transform.origin.distance_to(current_position)
    if distance < minimum_distance:
        minimum_distance = distance
        nearest_object = object

return object
```

The distance calculation is the same, but the amount of objects in the list goes from looking at the entire active game world to a small area hovering inches in front of the player's face.

## The Geometry class

The user clicks on the screen and you want to check if the point is inside some sprite's bounding-box. Here's the manual way to do it:

```gdscript
func is_point_in_rect(point, rect):
    return (
        point.x > rect.position.x and
        point.x < rect.position.x + rect.size.x and
        point.y > rect.position.y and
        point.y < rect.position.y + rect.size.y
    )
```

That's fast enough. But then you come up with sprites that have different shapes, like intricate ships or weird beasts, and checking if the user clicks on them means checking against their geometry.

For that, Godot provides the static [Geometry](https://docs.godotengine.org/en/stable/classes/class_geometry.html) class. `Geometry` has a list of functions to get information about and manipulate shapes in 2D and 3D. You can find what you need for most geometry purposes there.

```gdscript
# Fast: Check if a point is inside a polygon
var is_in_rect = Geometry.is_point_in_polygon(point, collider_shape.polygon)
```

## More helpers and functions

Godot is full of nodes that can do good work for you. The most difficult aspect of this kind of optimization is finding the features.

Get to know the nodes. Open the _Add Node_ window in Godot and go down the list, then check the [official documentation](https://docs.godotengine.org/en/stable/) to find out what it can do.

I recommend you to browse at the built-in class reference (<kbd>Shift</kbd> <kbd>F1</kbd>)  looking for class names that sound useful.

Here are some widely-used ones:

- [Tween](https://docs.godotengine.org/en/stable/classes/class_tween.html).
- [Line2D](https://docs.godotengine.org/en/stable/classes/class_line2d.html).
- [RayCast2D](https://docs.godotengine.org/en/stable/classes/class_raycast2d.html) and its 3D counterpart.
- [RayCast](https://docs.godotengine.org/en/stable/classes/class_raycast.html).
- [AnimationPlayer](https://docs.godotengine.org/en/stable/search.html?q=AnimationPlayer) .
- [Timer](https://docs.godotengine.org/en/stable/classes/class_timer.html). 

When it comes to physics, read about the four types of [physics bodies](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html#collision-objects) available in the engine.

Two noteworthy standouts for 3D are the [SurfaceTool](https://docs.godotengine.org/en/stable/classes/class_surfacetool.html) and [MeshDataTool](https://docs.godotengine.org/en/stable/classes/class_meshdatatool.html) classes. They help you create and manipulate 3D meshes.
