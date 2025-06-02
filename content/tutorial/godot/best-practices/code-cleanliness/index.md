---
author: razoric
coAuthor:
- nathan
date: "2021-03-30T00:00:00-06:00"
description: ""
difficulty: intermediate
keywords:
- godot best practices
- godot clean code
- gdscript style
menuTitle: Clean code
software: godot
title: Keeping your Godot code clean and readable
toc: true
weight: 5
---

## Introduction

Even when you work alone on a project and code everything, you do not code for your eyes alone.

Days, weeks, months, or years into your project, you may need to track down an elusive bug or refactor an old system. You may be the one who coded it in the first place, but memory is a fickle thing; the odds of you remembering what each abbreviated, shorthanded variable name means or what a block of ambiguous logic means is low.

While it may make your code more verbose, it becomes easier to read, remember, and follow its logic by looking at variable names and functions.

On the other hand, if the code is clean and explicit, refamiliarizing yourself with it will be a lot easier. You don't code _just_ for yourself, but your future self too.

**Help your future self. You're their only hope.**

## Keep function and variable names readable and descriptive

Abbreviations, shorthand, and ambiguous names can save typing time but demand more brainpower if you forget what it meant down the line or if someone else has to read your code.

The problem becomes even more evident when you take the piece of code out of context, like when showing it to someone or asking for help on a chat server.

```gdscript
if not rcvs_p.has(c):
    rcvs_p[c] = min(apow, rpow)
else:
    rcvs_p[c] += min(apow, rpow)

apow -= rpow
```

Use actual, descriptive names where possible to make the logic more opaque and obvious. We are no longer coding on terminals of 80 characters or struggling with keeping code under 1 kilobyte of space.

```gdscript
if not receivers_already_provided.has(cell):
    receivers_already_provided[cell] = min(available_power, power_required)
else:
    receivers_already_provided[cell] += min(available_power, power_required)

available_power -= power_required
```

Some codified examples have well-understood shorthands already. When iterating through an array's indices, you do not need to rename a simple `i` to `index`, or rename mathematical constants if it does not help readability.

```gdscript
for i in vertex_indices:
    #...
```

## Wrap ambiguous conditionals inside nicely named variables

Consider the following condition for an `if` statement:

```gdscript
if _gui.blueprint and _gui.blueprint.placeable:
    if not _simulation.entity_tracker.entities.has(cellv) and get_global_mouse_position().distance_to(_player.global_position) < MAXIMUM_WORK_DISTANCE and _ground.get_cellv(cellv) == 0:
        #...
```

If you are intimate with the code base, you may know what each of those conditions implicitly means. But if you leave the project to sit for days, weeks, or months before returning to this line of code, or someone else comes in and takes a look at it, it means minutes or more tracking down what each stipulation implies.

If the condition is ambiguous about its meaning, split it up into clear, well-labeled variables.

```gdscript
var has_placeable_blueprint: bool = _gui.blueprint and _gui.blueprint.placeable

var is_close_to_player := (
    get_global_mouse_position().distance_to(_player.global_position) < MAXIMUM_WORK_DISTANCE
)

var cell_is_occupied := _simulation.entity_tracker.entities.has(cellv)
var is_on_ground := _ground.get_cellv(cellv) == 0

if has_placeable_blueprint:
    if not cell_is_occupied and is_close_to_player and is_on_ground:
        #...
```

Here are some guidelines to find readable names:

1. Use **nouns for data** and **verbs for functions**. For example, `var weapons: Array` and `func walk_along_path()`. This helps to distinguish the two at a glance and will be especially useful with first-class functions in Godot 4.0.
1. Consider using a prefix for booleans: `has_placeable_blueprint` instead of `placeable_blueprint`. This clarifies that the value is either `true` or `false` and that it couldn't reference a node or some other data.
1. Use the past tense for signals in Godot: they represent events that already occurred. For signals that represent the start or the end of a chain of events, we append "\_started" or "\_finished" to the name.
1. For classes and nodes, try to find names that instantly tell what their responsibility is. For example, in our tower defense demo, the node that places towers on the grid is named `TowerPlacer`.

## Keep indented blocks shallow

Having nested if statements or loops is inevitable in some cases, but you can keep your code looking a lot tidier by trying to keep as much of it as possible lined up with the left margin as possible.

The more indentation levels you have in a script, the more your eyes have to jump around to read and understand the code.

Limit the number of if statements inside if statements: you can rewrite certain condition chains into a single if. You can wrap `or` statements inside parentheses to maintain the logic, whereas you can chain `and` statements.

Instead of this:

```gdscript
if gui.window.fuel or available_fuel > 0.0:
	if gui.window.ore:
		if work.available_work <= 0.0:
			#...
```

You can write the condition on a single line.

```gdscript
if (gui.window.fuel or available_fuel > 0.0) and gui.window.ore and work.available_work <= 0.0:
	#...
```

When you have many conditions and the line becomes difficult to read, you can use a variable to describe it.

```gdscript
var can_build: bool = (
	(gui.window.fuel or available_fuel > 0.0) and gui.window.ore and work.available_work <= 0.0
)

if can_build:
	#...
```

You can do the same with functions. If the function only works on certain conditions, you can invert your `if` statement and return early.

Avoid the following.

```gdscript
func _unhandled_input(event: InputEvent) -> void:
	if not screen_fader.is_playing:
		if event is InputEventKey or event.is_action_pressed("thrust_forwards"):
			#...
```

Instead, you can do this.

```gdscript
func _unhandled_input(event: InputEvent) -> void:
	# Only run the function's body if the screen_fader is stopped.
	if screen_fader.is_playing:
		return

	if event is InputEventKey or event.is_action_pressed("thrust_forwards"):
		#...
```

## Prefer calls to named functions over nested logic

Try to keep functions doing more or less one job. For example, `_unhandled_input`'s job is to detect and parse user input and do something on specific inputs.

Its role is not to place an entity and update the neighboring entities.

Avoid putting a lot of code in an unrelated function like so.

```gdscript
func _unhandled_input(event: InputEvent) -> void:
    #...
    if not cell_is_occupied and is_close_to_player and is_on_ground:
        var blueprint: BlueprintEntity = _gui.blueprint
        var blueprint_name: String = Library.get_filename_from(blueprint)

        var new_entity: Node2D = Library.entities[blueprint_name].instance()
        for neighbor in Types.NEIGHBORS.keys():
        var key: Vector2 = cellv + Types.NEIGHBORS[neighbor]
            #etc...
```

Instead, extract the logic inside functions to do that job, and have the original call those functions.

Give the new functions descriptive names so that, at a glance, you can tell what happens on which input. Coupled with wrapping your conditions inside descriptive variables and you can almost read the code like English.

```gdscript
func _unhandled_input(event: InputEvent) -> void:
    #...
    if not cell_is_occupied and is_close_to_player and is_on_ground:
        _place_entity(cellv)
        _update_neighboring_flat_entities(cellv)
```

## Reduce repetition: cache values

If you have a particular conditional, value, or lookup you frequently use in a function's body, you can make your code more readable by caching it ahead of time instead of repeating it.

```gdscript
var has_placeable_blueprint: bool = blueprint and blueprint.placeable
var cell_is_occupied := _simulation.is_cell_occupied(cellv)
var is_on_ground := _ground.get_cellv(cellv) == 0

var is_close_to_player := (
	global_mouse_position.distance_to(_player.global_position)
	< MAXIMUM_WORK_DISTANCE
)

if event.is_action_pressed("left_click"):
	if has_placeable_blueprint:
		if not cell_is_occupied and is_close_to_player and is_on_ground:
			_place_entity(cellv)
			_update_neighboring_flat_entities(cellv)

	elif cell_is_occupied and is_close_to_player:
		var entity := _simulation.get_entity_at(cellv)
		if entity and entity.is_in_group(Types.GUI_ENTITIES):
			_gui.open_entity_gui(entity)
			_clear_hover_entity()
```

This also results in better performance, especially for expensive calls like `get_node()` (or its shorthand `$`).

## Add blank lines between groups of relevant lines of code

A bit of breathing room will go a long way towards improving the readability. Consider the difference between the following two blocks of code. One breathes a little more and keeps the eye from glazing over as much.

```gdscript
	if event is InputEventMouseButton:
		_abort_deconstruct()
	var global_mouse_position := get_global_mouse_position()
	var blueprint: BlueprintEntity = _gui.blueprint
	var has_placeable_blueprint: bool = blueprint and blueprint.placeable
	var is_close_to_player := (
		global_mouse_position.distance_to(_player.global_position)
		< MAXIMUM_WORK_DISTANCE
	)
	var cellv := world_to_map(global_mouse_position)
	var cell_is_occupied := _simulation.is_cell_occupied(cellv)
	var is_on_ground := _ground.get_cellv(cellv) == 0

```

By adding extra lines, we can visually group logic and read it more easily.

```gdscript
	if event is InputEventMouseButton:
		_abort_deconstruct()

	var global_mouse_position := get_global_mouse_position()
	var blueprint: BlueprintEntity = _gui.blueprint
	var has_placeable_blueprint: bool = blueprint and blueprint.placeable

	var is_close_to_player := (
		global_mouse_position.distance_to(_player.global_position)
		< MAXIMUM_WORK_DISTANCE
	)

	var cellv := world_to_map(global_mouse_position)
	var cell_is_occupied := _simulation.is_cell_occupied(cellv)
	var is_on_ground := _ground.get_cellv(cellv) == 0
```

## When commenting code, avoid obvious comments

Comments are useful, but they should be helpful and not get in the way or make your codebase more cluttered. Use them when the code is not evident and when descriptive variable or function names are not enough.

Avoid commenting lines that are obvious from reading the code, such as in the following.

```gdscript
# Converts the global mouse position from world to map coordinates.
var cellv := world_to_map(global_mouse_position)

# Places the entity at the mouse map coordinates
_place_entity(cellv)
```

The comments above paraphrase the code. Even worse, comments add maintenance work and tend to fall out of sync with the code. Over time, they can turn into _lies_.

That's why you want to avoid superfluous comments. Use them sparingly, when they help to understand the code better.

Splitting logic into functions and using descriptive names greatly reduces the need for comments as it reduces the amount of ambiguous code.

## Limit line length

Unavoidably, some lines are going to become long. While you should not be _too_ concerned about line length, a good practice is to keep lines of code below 100 characters. Going a little over is fine, but if you exceed it by a large margin, use parentheses and parameters to break up the line.

```gdscript
func _get_direction() -> Vector2:
	return Vector2(
		(Input.get_action_strength("right") - Input.get_action_strength("left")) * 2.0,
		Input.get_action_strength("down") - Input.get_action_strength("up")
	).normalized()
```

A code formatter will do that for you automatically. For GDScript code, you can use [gdformat](https://github.com/Scony/godot-gdscript-toolkit/).

