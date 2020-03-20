+++
author = "nathan"
date = "2019-07-16T08:34:54+09:00"
description = "This guide covers some best practices to write solid GDScript code, to keep a sane code-base when developing projects of growing sizes."
title = "Best Practices: Godot GDScript"
menuTitle = "Godot GDScript"
weight = 2
aliases = ["/open-source/guidelines/godot-gdscript/"]

[[resources]]
  name = "banner"
  src = "banner.jpg"

+++

This guide covers best practices when writing GDScript code. We use it to keep our code clean and maintainable. It's meant as a complementary resource to the [oficial GDScript guidelines](http://docs.godotengine.org/en/3.2/getting_started/scripting/gdscript/gdscript_styleguide.html).

The ideas in this article are inspired by best practices from a variety of languages. We draw from the work of the Python community, some functional programming principles, and the official GDScript documentation:

1. [GDScript Style Guide](//docs.godotengine.org/en/latest/getting_started/scripting/gdscript/gdscript_styleguide.html)
1. [Static typing in GDScript](//docs.godotengine.org/en/latest/getting_started/scripting/gdscript/static_typing.html)
1. [Docs writing guidelines](//docs.godotengine.org/en/latest/community/contributing/docs_writing_guidelines.html)
1. [Boundaries - A talk by Gary Bernhardt from SCNA 2012](//www.destroyallsoftware.com/talks/boundaries) & [Functional Core, Imperative Shell](//www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
1. [The Clean Architecture in Python](//www.youtube.com/watch?v=DJtef410XaM)
1. [Onion Architecture Without the Tears - Brendan Richards](//www.youtube.com/watch?v=R2pW09tMCnE&t=1095s)
1. [Domain Driven Design Through Onion Architecture](//www.youtube.com/watch?v=pL9XeNjy_z4)

Godot is mostly object-oriented and offers its own tools such as signals and the node tree to make objects communicate. As a result, it's not always easy to apply principles and techniques from other programming languages to it.

## Code Writing Style

We wrote these GDScript programming guidelines with a few goals in mind:

- Avoid coupling and having systems depend on (or break!) one another.
- Manage boundaries, that is to say, the places where different systems interact with one another.
- Keep the code readable while working as a team. As developers, we spend more time reading code than writing it.

### In Short

We follow the same [code order](http://docs.godotengine.org/en/3.2/getting_started/scripting/gdscript/gdscript_styleguide.html#code-order) from the official GDScript style guide. Here is a complete example that follows these guidelines:

{{< highlight gdscript >}}
# Hierarchical State machine for the player.
# Initializes states and delegates engine callbacks (_physics_process, _unhandled_input) to the state.
class_name StateMachine
extends Node


signal state_changed(previous, new)

export var initial_state := NodePath()

onready var state: State = get_node(initial_state) setget set_state
onready var _state_name := state.name


func _init() -> void:
    add_to_group("state_machine")


func _ready() -> void:
    connect("state_changed", self, "_on_state_changed")
    state.enter()


func _unhandled_input(event: InputEvent) -> void:
    state.unhandled_input(event)


func _physics_process(delta: float) -> void:
    state.physics_process(delta)


# Replaces the current state with the state at `target_state_path` if the path
# is valid. Passes the `msg` dictionary to the new state's `enter` function.
func transition_to(target_state_path: String, msg: Dictionary = {}) -> void:
    if not has_node(target_state_path):
        return

    var target_state := get_node(target_state_path)
    assert(target_state.is_composite == false)

    state.exit()
    self.state = target_state
    state.enter(msg)
    Events.emit_signal("player_state_changed", state.name)


func set_state(value: State) -> void:
    state = value
    _state_name = state.name


func _on_state_changed(previous: Node, new: Node) -> void:
    print("state changed")
    emit_signal("state_changed")
{{< / highlight >}}

### Code style ###

Start with the optional `class_name` if needed. Then add the `extends` keyword if the class extends a built-in type. Following that, you should have the class's docstring:

{{< highlight gdscript >}}
# A brief description of the class's role and functionality.
#
# A longer description if needed, possibly of multiple paragraphs. Properties and method names
# should be in backticks like so: `_process`, `x` etc.
#
# You can use *markdown* in the docstrings.
#
# Keep lines under 100 characters long.
class_name MyNode
extends Node
{{< / highlight >}}

Signals go first and don't use parentheses unless they pass function parameters. Use the past tense to name signals. Append `_started` or `_finished` if the signal corresponds to the beginning or the end of an action.

{{< highlight gdscript >}}
signal moved
signal talk_started(parameter_name)
signal talk_finished
{{< / highlight >}}


{{% notice note %}}
From Godot 3.2, you can write docstrings above any property, signal, or function as a series of comments above their definition, and the GDScript language server will show them in the docs completion. You can also use that to create a code reference with our tool [GDScript Docs Maker](https://github.com/GDQuest/gdscript-docs-maker).
{{% / notice %}}

After that enums, constants, exported, public (regular name), and pseudo-private (starting with `_`) variables, in this order.

Enum type names should be in `CamelCase` while the enum values themselves should be in `ALL_CAPS_SNAKE_CASE`. This order is important because exported variables might depend on previously defined enums and constants.

{{< highlight gdscript >}}
enum TileTypes { EMPTY=-1, WALL, DOOR }

const MAX_TRIALS := 3
const TARGET_POSITION := Vector2(2, 56)

export var number := 0
export var is_active := true
{{< / highlight >}}

_Note:_ for booleans, always include a name prefix like `is_`, `can_`, or `has_`.

After this are public and pseudo-private member variables. Their names should use `snake_case` and `_snake_case_with_leading_underscore` respectively.

Define setters and getters when properties alter the object's state or if changing the property triggers methods. Care needs to be taken when doing this because we can easily loose track of hidden alterations and behaviors.

Include a docstring in the setters/getters if they modify the node/class state in complex ways.

Start with a leading underscore when writing setters or getters for private variables just like the variable.

{{< highlight gdscript >}}
var animation_length := 1.5
var tile_size := 40
var side_length := 5 setget set_side_length, get_side_length

var _count := 0 setget _set_count, _get_count
var _state := Idle.new()
{{< / highlight >}}

Place `onready` variables right before `_init` and/or `_ready` functions to visually connect these with their usage inside the `_ready` function.

{{< highlight gdscript >}}
onready var timer := $HungerCheckTimer
onready var ysort := $YSort
{{< / highlight >}}


Next define virtual methods from Godot (those starting with a leading `_`, e.g. `_ready`). Always leave 2 blanks lines between methods to visually distinguish them from other code blocks.

{{< highlight gdscript >}}
func _init() -> void:
  pass


func _process(delta: float) -> void:
  pass
{{< / highlight >}}

For signal callbacks, we use Godot's convention,  `_on_NodeName_signal_name`:

{{< highlight gdscript >}}
func _on_Quest_started(which: Quest) -> void:
  ...
{{< / highlight >}}

You should remove `NodeName` if the object connects to itself:

{{< highlight gdscript >}}
class_name HitBox
extends Area2D


func _ready() -> void:
  connect("area_entered", self, "_on_area_entered")
{{< / highlight >}}

Then define public methods. Include type hints for variables and the return type. You can use a brief comment to describe what the function does and what it returns.

Start the sentence with `Returns` when describing the return value. Use the present tense and direct voice. See Godot's [documentation writing guidelines](//docs.godotengine.org/en/latest/community/contributing/docs_writing_guidelines.html) for more information.

{{< highlight gdscript >}}
func can_move(cell_coordinates: Vector2) -> bool:
  return grid[cell_coordinates] != TileTypes.WALL
{{< / highlight >}}

Use `return` only at the beginning and end of functions. At the beginning of the function we use `return` as a guard mechanism if the conditions for executing the function aren't met.

**Don't** return in the middle of the method. It makes it harder to track returned values.

Here's an example of a **clean** and readable method:

{{< highlight gdscript >}}
func _set_elements(elements: int) -> bool:
  # Sets up the shadow scale, number of visual elements and instantiates as needed.
  # Returns true if the operation succeeds, else false
  if (not has_node("SkinViewport") or
      elements > ELEMENTS_MAX or
      not has_node("Shadow")):
    return false

  # If the check succeeds, proceed with the changes
  var skin_viewport := $SkinViewport
  var skin_viewport_staticbody := $SkinViewport/StaticBody2D
  for node in skin_viewport.get_children():
    if node != skin_viewport_staticbbody:
      node.queue_free()

  var interval := INTERVAL
  var r := RandomNumberGenerator.new()
  r.randomize()
  for i in range(elements):
    var e := Element.new()
    e.node_a = "../StaticBody2D"
    e.position = skin_viewport_staticbody.position
    e.position.x += r.randf_range(interval.x, interval.y)
    interval = interval.rotated(PI/2)
    skin_viewport.add_child(e)

  $Shadow.scale = SHADOW.scale * (1.0 + elements/6.0)
  return true
{{< / highlight >}}

### Use static types

We use static types to help write more insightful code and help avoid errors.

At the time of writing, static typing doesn't provide any performance boosts in GDScript. But it gives you better code completion and error reporting. In the future, it should give you major performance improvements over dynamic code as well.

To get started with GDScript's type hints, read [Static typing in GDScript](//docs.godotengine.org/en/latest/getting_started/scripting/gdscript/static_typing.html) in the official manual.

#### Use type inference when possible

Normally, you define typed variables like this:

{{< highlight gdscript >}}
var direction: Vector2 = get_move_direction()
{{< / highlight >}}

But if `get_move_direction` has a return type annotation, Godot can infer the type of the variable for us. In that case, we only need to add a colon after the variable's name:

{{< highlight gdscript >}}
func get_move_direction() -> Vector2:
  var direction := Vector2(
      ...
  )
  return direction

var direction := get_move_direction() # The variable's type is Vector2
{{< / highlight >}}

**Let Godot infer the type whenever you can**. It's less error prone because the system keeps better track of types than we humanly can. It also pushes us to have proper return values for all the functions and methods that we write.

Since the compiler doesn't enforce static types, sometimes we have to help it out. Take the following example:

{{< highlight gdscript >}}
var array := [1, "Some text"]
var text: String = array.pop_back()
{{< / highlight >}}

The `Array` can contain values with different types. In the example above, we have both an `int` and a `String` stored in the array. If you only wrote `var text := array.pop_back()`, Godot would complain because it doesn't know what type the `pop_back` method should return.

If we open the code reference with <kbd>Shift+F1</kbd> and search for the method, we see that:

```
Variant pop_back()
  Remove the last element of the array.
```

`Variant` is a generic type that can hold any type Godot supports. That's why we have to explicitly write variable types when dealing with these functions: `var text: String = arr.pop_back()`.

You'll get this issue with all built-in methods that return the engine's `Variant` type.

### Avoid `null` references

**Use `null` only when you have to**. Instead, think about alternatives to implement the same functionality with other types.

Using `null` is often a lost opportunity to have a value that makes sense instead, like `Vector2.ZERO`, or to simplify code, removing unnecessary state checks, i.e.:

{{< highlight gdscript >}}
if not variable:
    return
{{< / highlight >}}

With type hints and type inference you will naturally avoid `null` though:

{{< highlight gdscript >}}
var speed := Vector2.ZERO
var path := TrajectorySpline.new()
{{< / highlight >}}

It's impossible to get rid of `null` completely because GDScript relies on built-in functions that work with `null` values.

{{% notice note %}}
`None`, `null`, `NULL`, and similar references could be the biggest mistake in the history of computing. Here's a detailed explanation from the man who invented it himself: [Null References: The Billion Dollar Mistake](//www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare).
{{% /notice %}}

### Write self-documenting code and use comments sparingly

If you need comments to explain most of what your code does, you can most likely rewrite it to make it more transparent for everyone. When working together for an extended period, code readability is essential for everyone to stay productive.

Use clear variable names in plain English and write full words. E.g. `character_position` and not `char_pos`. The same goes for method names.

**Do not** repeat words in the method's name and its arguments. E.g. write `Inventory.add(item)`, not `Inventory.add_item(item)`. The same goes for signals.

Use plain verbs instead of repeating the class's name in signals:

{{< highlight gdscript >}}
class_name Event
extends Node

signal started
signal completed
{{< / highlight >}}

You _may_ use short variable names inside of your methods, for local variables, to avoid repeating a type hint for instance.

In the example below, the variable `e`, an instance of `Element`, only appears in 4 consecutive lines so the code stays readable:

{{< highlight gdscript >}}
func _set_elements(elements: int) -> bool:
...
  for i in range(elements):
    var e := Element.new()
    e.node_a = "../StaticBody2D"
    e.position = skin_viewport_staticbody.position
...
{{< / highlight >}}

#### Use comments if they save time or add key explanations

Your code should be **self-explanatory whenever possible**. Sometimes you may have a long block of code that you can't change, or have some strange code to work around an engine bug.

In these cases, writing a short comment above the corresponding block can save everyone a lot of time including your future self.

In this example, the code involves transforming and multiplying matrices to calculate a position in Godot's 2D viewport. A one-line comment can capture what it does and avoid having to make sense of the calculations:

{{< highlight gdscript >}}
func drag_to(event_position: Vector2) -> void:
  # Calculate the position of the mouse cursor relative to the RectExtents' center
  var viewport_transform_inverse:= rect_extents.get_viewport().get_global_canvas_transform().affine_inverse()
  var viewport_position: Vector2 = viewport_transform_inv.xform(event_position)
  var transform_inverse:= rect_extents.get_global_transform().affine_inverse()
  var target_position: Vector2 = transform_inv.xform(viewport_position.round())
{{< / highlight >}}

Here's a comment that explains why a seemingly strange line of code is necessary so another developer doesn't remove it accidentally:

{{< highlight gdscript >}}
extends BattlerAI

func choose_action(actor: Battler, targets: Array = []):
    # We use yield even though the action is instantaneous
    # because the combat system expects this method to use a coroutine
    yield(get_tree(), "idle_frame")
    ...
{{< / highlight >}}


### Naming conventions ###

We follow some guidelines to keep the name of our files meaningful and consistent.

The top-level folders include:

  - `assets`, shared files like images, sounds, music, text produced outside Godot.
  - `src`, the source code of the game. It includes all scenes and GDScript files which are all part of the source.

{{< figure src="./img/naming-conventions-folders.png">}}

#### General naming conventions ####

**Never include spaces in the filenames**. Spaces can [cause issues with command line tools](//superuser.com/questions/29111/what-technical-reasons-exist-for-not-using-space-characters-in-file-names), which we use to automate tasks.

We generally name files, variables, and classes starting with keywords that help group and distinguish similar elements.

For example, instead of:

```
var walk_speed
var run_speed
var sprint_speed
var max_speed
```

We favor:

```
var speed_walk
var speed_run
var speed_sprint
var speed_max
```

This helps to group and find related variables through autocompletion. In this case, if you type `sp`, all four speed-related variables will appear in the completion menu.

#### Naming in the src folder ####

Use `PascalCase` for folder names in the `src` folder as they represent game systems or groups of systems.

Scenes and script files also use `PascalCase` as they represent classes. This is also how Godot names them by default:

```
Quests/
  Quest.gd
  Journal.gd
  QuestDirector.gd
```

#### Naming in the assets folder ####

Use lowercase for the folder names to distinguish them from the source code.

Name the assets using `snake_case`:

```
body.png
arm_right.png
sword_hit.ogg
theme.tres
```
