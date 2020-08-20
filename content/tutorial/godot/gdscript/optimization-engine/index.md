+++
title = "Optimizing code by leveraging Godot's native speed"
description = "A list of tips to reduce the amount of manual work you do and use the speed of Godot's C++."
author = "razoric"
menuTitle = "Optimization 2 - Use Godot's speed"

date = 2020-08-18T11:07:59-04:00
weight = 4
draft = true

difficulty = "beginner"
tags = ["tutorial", "godot", "gdscript"]
keywords = ["gdscript optimization tutorial", "godot code optimizing", "godot optimization"]
+++

Making a game run fast means also having fast code. You can code well in GDSCript and get good performance, but there is one shortcut you can follow to have fast code without much, and sometimes _less_, effort: Making Godot do the work for you.

## Focus optimization where it counts

An **important** disclaimer, as ever whenever talking about code optimization, is to not optimize where there is little gain. Making your `_ready` function blazing fast is all well and good, but this is something that gets called once and never again. The real gains for optimization are blocks of code that run often. A slow block of code inside a large loop is a far more important target for optimization than code that runs once.

You also do _not_ want to optimize in a vacuum. Unless you have the knowledge that some part of your code is actually slow, or is slow enough to impact the enjoyment of the game, you could be making your code harder to read for almost no gain. Run the profiler and measure your code.

_Never assume anything._ [Measure](../optimization-measure).

## GDScript, Godot and C++

Godot runs on C++ and the GDScript interpreter is a go-between your code and the engine. The Godot developers program every feature that's built-in to the engine in optimal, _compiled_, native and fast C++. Every function that you did not code yourself calls C++ code. That means you can have much faster code by using Godot's built-in functions and objects instead of going through the effort of writing them yourself.

You don't recreate code that already exists, you get code that is shorter and easier to read, _and_ you get a faster game.

## Make the engine work for you

This is a list of tips for some common tasks that can be common across game projects, though by no means an exhaustive one.

### Prefer math from Godot over manual calculations

GDScript exposes a variety of math and number manipulating functions that are better than you at calculating data. [Look over the list](https://docs.godotengine.org/en/stable/classes/class_@gdscript.html) and prefer using those over manually calculating values whenever possible. Here are a few common cases in game development:

Checking if a value is negative or positive:

```gdscript
# SLOW
var result = 0
if value < 0:
    result = -1
elif value > 0:
    result = 1


# FAST
result = sign(value)
```

Bring a value down from [current_min ... current_max] to [intended_min ... intended_max] range

```gdscript
# SLOW
value = (value - current_min) / (current_max - current_min) * (intended_max - intended_min) - intended_min


# FAST
value = range_lerp(value, current_min, current_max, intended_min, intended_max)
```

Find the next power of 2

```gdscript
# SLOW
value = pow(2, ceil(log(value) / log(2)))


# FAST
value = nearest_po2(value)
```

### Prefer instancing scene files over building scene trees

It's common to manually build scene trees because you want to have a custom node set up for each entity you create. But calling each `new()` and `add_child()` one at a time, and configuring property as you go is going to be cause more code and will be a lot slower than `instance()`.

```gdscript
# SLOW: Build a script with a kinematic body 2D circle with a timer
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


# FAST: Build a script with a kinematic body 2D circle with a timer
var body = preload("res://player/TimedKinematic.tscn").instance()
add_child(body)
```

You can customize the result after instancing. Look at how you are creating node trees and try to find common elements. If they all follow the same template but have different properties, then instance it as a scene and change the properties afterwards. If they all follow the same starting template but have different nodes, create a scene that has those common elements and add the rest manually.

```gdscript
var body = preload("res://Shared/KinematicActor.tscn").instance()

var enemy_behavior = preload("res://Enemies/EnemyBehavior.gd").new()
body.add_child(enemy_behavior)

add_child(body)
```

### Use an Area node to find the nearest neighbor

Finding the nearest object is a common task for path-finding, AI targeting or interact button prompts. When you are not dealing with physics, it can be tempting to think of grabbing a list of objects in the world and checking for distances to find the nearest one.

```gdscript
# SLOW: Find the nearest interactive object out of a list
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

Depending on the number of objects in your game world, this can be adequate or it can be an utter disaster, notably when called every frame. Imagine a puzzle room where you can pick up every curios, piece of bread, spoon, plate or wheel of cheese! Instead, you could affix an Area node to the objects that you can interact with and apply a cleverly placed Area node to the player's interaction detector. Let the physics engine find objects for you and filter out the rest.

```gdscript
# FAST: Find the nearest interactive object out of a list
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

The distance calculation is the same, but the amount of objects that are in the list go from looking at the entire active game world to a small area hovering inches in front of the player's face or hand.

### The Geometry class

The user has clicked on the screen and you want to check if the point that got clicked on is inside some sprite's hitbox. You figure that the hit box is a rectangle and the click is a point, and come up with an algorithm. You put it in a function so you can call it from different places.

```gdscript
# SLOW: Check if a point is inside a rectangle
func is_point_in_rect(point, rect):
    return (
        point.x > rect.position.x and
        point.x < rect.position.x + rect.size.x and
        point.y > rect.position.y and
        point.y < rect.position.y + rect.size.y
    )
```

That's fast enough. But then you come up with sprites that have different shapes, like intricate ships or weird beasts, and checking if the user clicks on them means checking against their geometry. Internet research leads you to the Point In Polygon article on Wikipedia that uses rays and odd numbered intersection counts. With enough research and iterations you could probably come up with a decent implementation, but it's a lot of GDScript math and is going to start slow.

In comes one of the lesser known heroes of the Godot engine, the static `Geometry` class. Geometry has [a list of functions](https://docs.godotengine.org/en/stable/classes/class_geometry.html) designed around getting information about and manipulating shapes in 2D and 3D. You can find what you need for most geometry purposes in there.

```gdscript
# FAST: Check if a point is inside a rectangle
var is_in_rect = Geometry.is_point_in_polygon(get_global_mouse_position() - global_position, collider_shape.polygon)
```

## More helpers and functions

Get to know the nodes. Open the _Add Node_ window in Godot and go down the list, then check the [official documentation](https://docs.godotengine.org/en/stable/) to find out what it can do. Some well known stars include [Tween](https://docs.godotengine.org/en/stable/classes/class_tween.html), [Line2D](https://docs.godotengine.org/en/stable/classes/class_line2d.html), [RayCast2D](https://docs.godotengine.org/en/stable/classes/class_raycast2d.html) and its 3D [counterpart](https://docs.godotengine.org/en/stable/classes/class_raycast.html), [AnimationPlayer](https://docs.godotengine.org/en/stable/search.html?q=AnimationPlayer) and [Timer](https://docs.godotengine.org/en/stable/classes/class_timer.html). The GUI nodes that inherit from Control like the containers also can do a lot of work to organize your user interface.

Look at the [class reference](https://docs.godotengine.org/en/stable/classes/index.html) on the official documentation and see if any of the class names jump out at you. A couple noteworthy standouts for 3D are the [SurfaceTool](https://docs.godotengine.org/en/stable/classes/class_surfacetool.html) and [MeshDataTool](https://docs.godotengine.org/en/stable/classes/class_meshdatatool.html) classes.
