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

This guide covers some best practices to write solid GDScript code. It's the style we use to keep our code clean and maintainable, working on growing Godot games.

The ideas below draw inspiration from good practices from different paradigms and languages. Especially from the work of the Python community, some functional programming principles, and the official GDScript documentation:

1. [GDScript Style Guide](//docs.godotengine.org/en/latest/getting_started/scripting/gdscript/gdscript_styleguide.html)
1. [Static typing in GDScript](//docs.godotengine.org/en/latest/getting_started/scripting/gdscript/static_typing.html)
1. [Docs writing guidelines](//docs.godotengine.org/en/latest/community/contributing/docs_writing_guidelines.html)
1. [Boundaries - A talk by Gary Bernhardt from SCNA 2012](//www.destroyallsoftware.com/talks/boundaries) & [Functional Core, Imperative Shell](//www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
1. [The Clean Architecture in Python](//www.youtube.com/watch?v=DJtef410XaM)
1. [Onion Architecture Without the Tears - Brendan Richards](//www.youtube.com/watch?v=R2pW09tMCnE&t=1095s)
1. [Domain Driven Design Through Onion Architecture](//www.youtube.com/watch?v=pL9XeNjy_z4)

Godot is mostly object-oriented and offers its own tools to make objects communicate together, like signals, and the node tree. As a result, it's not always easy to apply principles and techniques from other programming languages to it.

We keep experimenting to improve the code we write, with a few goals in mind:

- Avoiding coupling, having system depend on and break one another
- Managing boundaries, the places where different game systems interact with one another
- Keeping the code readable working as a team, as we developers spend more time reading than writing code

## Code Writing Style

{{< youtube FB2sqJgfqXI >}}

We use the same code style so that you can find the information you need fast.

### In Short

We organize the code this way to make it easy to read:

```
01. tool
02. class_name
03. extends
04. """docstring"""

05. signals
06. enums
07. constants
08. exported variables
09. public variables
10. private variables
11. onready variables

12. optional built-in virtual _init method
14. built-in virtual _ready method
15. remaining built-in virtual methods
16. public methods
17. private methods
```

This code order shows you the code need to understand how the class works and how to use it in priority, and keeps the project organized and easy to read.

Here is a complete example that follows all the guidelines below:

{{< highlight gdscript >}}
class_name StateMachine
extends Node
# Hierarchical State machine for the player.
# Initializes states and delegates engine callbacks (_physics_process, _unhandled_input) to the state.


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


func transition_to(target_state_path: String, msg: Dictionary = {}) -> void:
    if not has_node(target_state_path):
        return

    var target_state := get_node(target_state_path)
    assert target_state.is_composite == false

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

Start with the `class_name`, but only if necessary. For example, if you need to check for this type in other classes, or to be able to create the node in the create node dialogue.

Then, add the `extends` keyword if the class extends a built-in type.

Following that, you should have the class's docstring:

{{< highlight gdscript >}}
extends Node
class_name MyNode
# A brief description of the class's role and functionality
# 
# A longer description if needed, possibly of multiple paragraphs. Properties and method names should be in backticks like so: `_process`, `x` etc.
# 
# Notes
# ~~~~~
# Specific things that don't fit the class's description above.
# 
# Keep lines under 100 characters long
{{< / highlight >}}

Signals go first and don't use parentheses unless they pass function parameters. Use the past tense to name signals. Append `_started` or `_finished` if the signal corresponds to the beginning or the end of an action.

{{< highlight gdscript >}}
signal moved
signal talk_started(parameter_name)
signal talk_finished
{{< / highlight >}}

Place `onready` variables after signals, because we mostly use them to keep track of child nodes this class accesses. Having them at the top of the file makes it easier to keep track of dependencies.

You should always include an explicit type for them: in some cases, Godot can't infer the type directly, and it gives us limited autocompletion when we use onready variables.

{{< highlight gdscript >}}
onready var timer: Timer = $HungerCheckTimer
onready var ysort: YSort = $YSort
{{< / highlight >}}

After that enums, constants, exported, public (regular name), and pseudo-private (starting with `_`) variables, in this order. 

Enum type names should be in `CamelCase` while the enum values themselves should be in `ALL_CAPS_SNAKE_CASE`. The reason for this order is that exported variables might depend on previously defined enums and constants while the enums might also depend on constants.

{{< highlight gdscript >}}
enum TileTypes { EMPTY=-1, WALL, DOOR }

const MAX_TRIALS := 3
const TARGET_POSITION := Vector2(2, 56)

export var number := 0
export var is_active := true
{{< / highlight >}}

_Note: for booleans, always include a name prefix like `is_`, `can_`, or `has_`.

Following are public and pseudo-private member variables. Their names should use `snake_case`, `_snake_case_with_leading_underscore` respectively.

Define setters and getters when properties alter the object's state or if changing the property triggers methods. When doing this care needs to be taken because we can easily loose track of this hidden alterations and behaviors. Include a docstring in the setters/getters if they modify the node/class state in complex ways.

When writing setters or getters for private variables, start with a leading underscore, just like in the case of the variable.

{{< highlight gdscript >}}
var animation_length := 1.5
var tile_size := 40
var side_length := 5 setget set_side_length, get_side_length

var _count := 0 setget _set_count, _get_count
var _state := Idle.new()
{{< / highlight >}}

Next define virtual methods from Godot (those starting with a leading `_`, e.g. `_ready`). Always leave 2 blanks lines between methods to visually distinguish them and other code blocks.

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

If the object connects to itself though, you should remove `NodeName`:

{{< highlight gdscript >}}
extends Area2D
class_name HitBox


func _ready() -> void:
  connect("area_entered", self, "_on_area_entered")
{{< / highlight >}}

Then define public methods. Include type hints for variables and the return type.

You can use a brief docstring, if need be, to describe what the function does and what it returns. To describe the return value in the docstring, start the sentence with `Returns`. Use the present tense and direct voice. See Godot's [documentation writing guidelines](//docs.godotengine.org/en/latest/community/contributing/docs_writing_guidelines.html) for more information.

{{< highlight gdscript >}}
func can_move(cell_coordinates: Vector2) -> bool:
  return grid[cell_coordinates] != TileTypes.WALL
{{< / highlight >}}

Use `return` only at the beginning and end of functions. At the beginning of the function we use `return` as a guard mechanism if the conditions for executing the function aren't met.

**Don't** return in the middle of the method. It makes it harder to track returned values. Here's an example of a **clean** and readable method:

{{< highlight gdscript >}}
func _set_elements(elements: int) -> bool:
  """
  Sets up the shadow scale, number of visual elements and instantiates as needed.
  Returns true if the operation succeeds, else false
  """
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

### Avoid `null` like the plague

**Use `null` only if you're forced to**. Instead, think about alternatives to implement the same functionality with other types.

`None`, `null`, `NULL`, etc. references could be the biggest mistake in the history of computing. Here's an explanation from the man who invented it himself: [Null References: The Billion Dollar Mistake](//www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare).

For programming languages that rely on `null`, such as GDScript, it's impossible to get rid of it completely: a lot of functionality relies on built-in functions that work with and return `null` values.

`null` can behave like any other value in any context, so the compiler can't find errors caused by `null` at compile time. `null` exceptions are only visible at runtime. This makes it more likely to write code that will fail when someone plays the game and it should be avoided like the plague.

You can use other values to initialize variables of certain types. For example, if a function returns a positive `int` number, if it is not able to calculate the desired return value, the function could return `-1` to suggest there was an error.

### Use static types

We use optional static typing with GDscript.

At the time of writing, static GDScript typing doesn't provide any performance boosts or any other compiler features. But it does bring better code completion and better error reporting and warnings, which are good improvements over dynamically typed GDScript. In the future, it should bring performance improvements as well.

Be sure to check [Static typing in GDScript](//docs.godotengine.org/en/latest/getting_started/scripting/gdscript/static_typing.html) to get started with this language feature.

Normally, you define typed variables like this:

{{< highlight gdscript >}}
var x: Vector2 = some_function_returning_Vector2(param1, param2)
{{< / highlight >}}

But if `some_function_returning_Vector2` is also annotated with a return type, Godot can infer the type for us so we only need to add a colon after the variable's name:

{{< highlight gdscript >}}
func some_function_returning_Vector2(param1: int, param2: int) -> Vector2:
  # do some work
  return Vector2.ZERO

var v := some_function_returning_Vector2(param1, param2) # The type is Vector2
{{< / highlight >}}

_Note_ how we still use the colon in the assignment: ` :=`. It isn't just `=`. Without the colon, the variable's type would be dynamic.

Use ` :=` with a space between the colon and the equal sign, **not** `:=`. ` :=` is easier to spot compared to `=`, in case someone forgets to use the colon.

**Let Godot infer the type whenever you can**. It's less error prone because the system keeps better track of types than we humanly can. It also pushes us to have proper return values for all the functions and methods that we write.

Since the static type system mostly brings better warnings and it isn't enforced, sometimes we have to help it out. The following snippet will make the problem clear:

{{< highlight gdscript >}}
var arr := [1, 'test']
var s: String = arr.pop_back()
var i: int = arr.pop_back()
{{< / highlight >}}

The `Array` type is a container for multiple different types. In the example above, we have both an `int` and a `String` stored in the array. If you only wrote `var s := arr.pop_back()`, Godot would complain because it doesn't know what type the `pop_back` method returns. You will get the same issue with all built-in methods that return the engine's `Variant` type. Open the code reference with <kbd>Shift+F1</kbd> and search for the methods to see that:

```
Variant pop_back()
  Remove the last element of the array.
```

`Variant` is a generic type that can hold any type Godot supports. That's why we have to explicitly write variable types when dealing with these functions: `var s: String = arr.pop_back()`.

In these cases, you must be careful as the following is also valid:

{{< highlight gdscript >}}
var arr := [1, 'test']
var s: int = arr.pop_back()
var i: String = arr.pop_back()
{{< / highlight >}}

You will not get any error with this code. At runtime, `s` will surprisingly still contain a `String`, and `i` will contain an `int`. But a type check like `s is String` or `i is int` will return `false`. That's a weakness of the current type system that we should keep in mind.

### Write self-documenting code and use comments sparingly

If you need comments to explain most of what your code does, you can most likely rewrite it to make it more transparent for everyone. When working together for an extended period, code readability is essential for everyone to stay productive.

Use clear variable names in plain English, and write full words. E.g. `character_position` and not `char_pos`. Same for method names.

**Do not** repeat the same word in the method's name and its arguments. E.g. write `Inventory.add(item)`, not `Inventory.add_item(item)`. The same goes for signals. Don't repeat the class's name in signals, use plain verbs instead:

{{< highlight gdscript >}}
Extends Node
class_name Event

signal started
signal completed
{{< / highlight >}}

You _may_ use short variable names inside of your methods, for local variables, to avoid repeating a type hint for instance. In the example below, the variable `e`, an instance of `Element`, only appears in 4 consecutive lines, so the code stays readable:

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

Your code should be **self-explanatory whenever possible**. But sometimes it's not: you may have a long block of code that you can't change, or have some strange code to work around an engine bug. In these cases, writing a short comment above the corresponding block can save everyone a lot of time, including your future self.

In this example, the code involves transforming and multiplying matrices to calculate some position in Godot's 2d viewport. A one-line comment can capture what it does and avoid having to make sense of the calculations:

{{< highlight gdscript >}}
func drag_to(event_position: Vector2) -> void:
  # Calculate the position of the mouse cursor relative to the RectExtents' center
  var viewport_transform_inverse:= rect_extents.get_viewport().get_global_canvas_transform().affine_inverse()
  var viewport_position: Vector2 = viewport_transform_inv.xform(event_position)
  var transform_inverse:= rect_extents.get_global_transform().affine_inverse()
  var target_position: Vector2 = transform_inv.xform(viewport_position.round())
{{< / highlight >}}

Here's a comment that explains why a seemingly strange line of code is necessary so another developer doesn't remove it inadvertently, thinking it's a mistake:

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
  - `src`, the source code of the game. It includes all scenes and GDScript files, which are all part of the source.

![naming-conventions-folders](./img/naming-conventions-folders.png)

#### General naming conventions ####

**Never include spaces in the filenames**. Spaces can [cause issues with command line tools](//superuser.com/questions/29111/what-technical-reasons-exist-for-not-using-space-characters-in-file-names), which we use to automate tasks.

#### Naming in the src folder ####

Use `PascalCase` for folder names in the `src` folder as they represent game systems or groups of systems. Scenes and script files also use `PascalCase` as they represent classes.

#### Naming in the assets folder ####

Name assets using `snake_case`, that is to say lowercase with the underscore `_` as a delimiter. We also use lowercase for the folder names to distinguish them from the source code.

## How to create decoupled and reusable game systems in Godot

One of the difficult tasks of a developer is to design and manage systems that interact with one another. This is especially true in the game development world, where we push the hardware to the limit, using parallel calculations and concurrency, asynchronous operations, and using every trick at our disposal to breathe life to complex virtual worlds.

{{< youtube CGg3LAo91pY >}}

_Dynamic, Imperative, and Object-Oriented_ programming languages like GDScript are fast to prototype ideas with. But this freedom comes at a cost: it's easy to create tightly **coupled** or **fragile** code. That is to say, code that will likely break.

The ease of use of GDScript can make game systems hard to debug. That is why we use some general guidelines to produce **decoupled systems**.

Decoupled systems:

1. **Can be tested on their own**.
1. Are **black boxes** that are fed data and produce some output. They don't care where they get the data from.
1. **Don't know anything about the outside world**.

This makes them **independent** and **reusable** across game projects. This also makes them **composable**. We can create complex systems using **aggregation**: by adding several decoupled nodes to a scene and and using them from a parent node.

See the Player in our Godot Metroidvania project. It's an aggregate of scenes: you can remove any of the nodes in the screenshot below and the player will still work without errors.

![Player scene tree example in Godot](./img/aggregation-player-scene-tree.png)

{{< note >}}
**Aggregation**

In Object-Oriented Programming, aggregation is a type of **association** between objects. Aggregation means that one object, our `Player` in the example above, uses others, like the `Hook` or the `CameraRig`. The `Hook` and the `CameraRig` can keep working even if we remove the association with the `Player` node.
{{< / note >}}

### Every building-block scene should run by itself without errors

**If you save a branch as an independent scene, it should run without any errors on its own**, this is the golden rule.

Godot relies on its node tree, a recursive data structure: if we pick any node in the tree, this node, together with all of its children, is a tree itself. You can consider each branch of the scene tree as an independent scene.

{{< figure
    src="./img/scene_tree.png"
    caption="Screenshot of a real system scene tree layout from [OpenRPG](//github.com/GDQuest/godot-open-rpg)"
    alt="./img/scene_tree.png" >}}

In the example above, you can view each node as a separate scene, be it `Board` or `QuestSystem`.

If we save `QuestSystem` using `Save Branch as Scene`, we should be able to run this scene locally, by pressing <kbd>F6</kbd>, without any error. In this case, we can't expect to have the same behavior as when we play the main `Game` scene, as it could depend on external data. It should just run without any errors.

{{< youtube WLYCgar9fyQ >}}

You should **never have direct references to specific objects from another system**. Instead, you should rely on a parent node to route information and let the systems interconnect via signals.

In the example above, the `Game` node has a script attached to it. This script sends some information from one system to another, while e.g. `QuestSystem` or `DialogSystem` have no knowledge about any other system other than themselves.

<!-- TODO: add code snippets from Game and QuestSystem -->

### Use signals to coordinate time-dependent interactions

Godot's signals are the [Observer pattern](//gameprogrammingpatterns.com/observer.html), a very useful tool that allows one node to react to a change in another, without storing it or having a direct reference to it.

Godot comes with many systems like physics, rendering or input, that run in parallel threads to squeeze every bit of hardware resource available. Oftentimes direct function calls aren't the right way to interact with objects.

Also, we can't always predict when an event will occur. Say we have an animation with a random or a varying duration. Sometimes it ends after 1 second, sometimes after 1.2 seconds. Signals allow us to react to the animation right when it finishes, regardless of its duration.

In practice, it can be difficult to know exactly when to use direct function calls and when to use signals. But with time and practice, managing information gets easier.

So **rely on signals when orchestrating time-dependent interactions.**


### Reinforcing good habit

Through GDScript, Godot prefers a coding style that is loose and free of any burden. This can quickly lead to spaghetti code since there's no mechanism by which Godot enforces nodes and scenes to be isolated. So it's up to us to keep track and implement this isolation.

{{< figure
    src="./img/node_closeup.png"
    caption="Fig. 3: A Node/Scene is composed of state and behavior"
    alt="./img/node_closeup.png" >}}


Fig. 3 depicts a typical node or scene in Godot. It bundles up state and behavior that can access the state at any time and alter it. But even more so, the lines coming in from the outside depict here other types of interactions that could happen from the external world (other systems):

- access to state directly, potentially changing it
- access to behavior, i.e. methods
- connections to methods via signals

Even a simple scene tree like the one in Fig. 4 can quickly become unmaintainable if all the flexibility Godot offers us isn't managed. Thus we need a way to maintain the number of potential connections as depicted in Fig. 3.

{{< figure
src="./img/scene_tree_overview.png"
caption="A relatively simple depiction of a Godot scene tree. The highlighted part represents a completely independent scene"
alt="./img/scene_tree_overview.png" >}}

#### More tips about independent scenes ####

We already went through this, but just to reinforce it even more - ideally, scenes should be independent and at any moment in our game development, if we choose to save a part of the node tree as a scene, **it should run by itself without any errors** - <kbd>F6</kbd>

<!-- TODO: talk about a contract type of method for creating complex scenes that break the idea of working independently at every level. For example the Player cene might be easier to manage by inner nodes accessing directly the `owner` property. This breaks the idea of having scenes work at every level at each time, but it creates instead the idea of having a "contract" within a building-block scene. The Player scene itself works and can be tested independently, but not necessarily all child nodes of Player-->

<!-- TODO: show a concrete example -->
Minimize changing the state of child nodes/scenes from parent nodes, unless the scene we're working with is logically built that way. For example, in [Fig. 4], in the highlighted node tree we see that the children nodes hold just data, but no custom behaviors that alters their state. The parent node in this case can access and potentially change the state of its children. In this case, the entire scene can be viewed from the outside like a black-box. All changes go through the parent node, with no direct access to the child nodes.

The idea of the black-box node/scene is more general. We should always strive to enforce it whenever possible. It's more strict than the simple idea of having independent scenes that can always run on their own. Scenes that are decoupled in this way, can still have their inner state be accessed by parent nodes and changed at run-time.

With the black-box, we extend this rule and strive not to change the state of child nodes/scenes from parent nodes or other systems except through signals.

The black-box scene is solely responsible for it's own behavior.

As an additional rule, the other way is true as well: _never_ change state of parent nodes from child nodes, unless through signals.

_Note_ that these are still just guidelines, they're not rules. Certain systems have to be built in other ways that can't uphold these ideas. The `AnimationPlayer` node is a good example. We can set the `root_node` property of the `AnimationPlayer` to point to any node in our node hierarchy and by default it operates relative to its parent. That's because it's awkward, impractical and hard to reason about to have a scene hierarchy where the `AnimationPlayer` node is the parent node.

Here are a few ideas that could improve code maintainability and overall structure:

1. Break up complex functions into smaller functions (ideally up to 10-15 lines of code and no more) and give them descriptive names

{{< figure
    src="./img/openrpg_scene_tree.png"
    caption="[OpenRPG](//github.com/GDQuest/godot-open-rpg) experimental branch scene tree."
    alt="./img/openrpg_scene_tree.png" >}}

Note how `Board` with its `PathFinder` algorithm is at the same level as `Party`. They're independent systems in this implementation. The `Party` node/scene can be viewed as the player object.

{{< highlight gdscript >}}
"""Game.gd file"""

...

func _unhandled_input(event: InputEvent) -> void:
  var move_direction := Utils.get_direction(event)
  if event.is_action_pressed("tap"):
    party_command({tap_position = board.get_global_mouse_position()})
  elif not dialog_system.is_open and move_direction != Vector2():
    party_command({move_direction = move_direction})


func party_command(msg: Dictionary = {}) -> void:
  var leader := party.get_member(0)
  if leader == null:
    return

  var path := prepare_path(leader, msg)
  party_walk(leader, path)

  var destination := get_party_destination(path)
  if destination != Vector2():
    emit_signal("party_walk_started", {"to": destination})


func prepare_path(leader: Actor, msg: Dictionary = {}) -> Array:
  var path := []
  match msg:
    {"tap_position": var tap_position}:
      path = board.get_point_path(leader.position, tap_position)
    {"move_direction": var move_direction}:
      if move_direction in board.path_finder.possible_directions:
        var from: Vector2 = leader.position
        var to := from + Utils.to_px(move_direction, board.path_finder.map.cell_size)
        if not board.path_finder.map.world_to_map(to) in board.path_finder.map.obstacles:
          path.push_back(from)
          path.push_back(to)
  return path


func party_walk(leader: Actor, path: Array) -> void:
  if leader.is_walking:
    return

  for member in party.get_members():
    if member != leader:
      path = [member.position] + path
      path.pop_back()
    member.walk(path)


func get_party_destination(path: Array) -> Vector2:
  var destination: Vector2 = path[path.size() - 1] if not path.empty() else Vector2()
  return destination
{{< / highlight >}}

In the example above, reading through `party_command` without looking at the implementation of other functions we already have a pretty good idea about what it does. That's because we divided up the implementation into smaller functions and giving expressive names to these functions.

{{< note >}}
Here, we are careful to not alter any state of other nodes. We only access the state in order to perform validations. This is important! All state changes that happen, happen within the respective **black-boxes**.
{{< / note >}}

The implementation for checking if the walk command can be issued is within a parent node, in this case the `Game.gd` script. That's because the verification depends on the `PathFinder` algorithm which is part of the separate `Board` system, while the player object (the `Party` here) is independent, it's a sibling relationship. The validation step depends on both `Party` and `Board` and that's why it's taken care of in the level of the top `Game` node [Fig. 5]. Otherwise we'd have to introduce an interdependence between `Party` & `Board` and that would tightly couple these systems.

Which leads us to:

2. Don't store references to systems within other systems.

For example, in the above, we could have had `Party` set up in such a way as to store a reference to `Board` and do all the validation checks on `path` inside of `Party`, but this would mean that it is tightly coupled with `Board`. Whenever possible we should avoid this.

3. Never alter state from a function that returns a concrete type (i.e. functions that don't return `-> void`).

Again, referring to the code above, we can see that `prepare_path` and `get_party_destination` each return a concrete type: `-> Array`, respectively`-> Vector2`. They have no other purpose than to calculate the promised return type and nothing more. They don't have any hidden agenda, don't alter anything, don't give commands to other functions that change state. They have a very precise "pure" job to do.

We could have for example called `party_walk` from within `get_party_destination` and rewrite the code a bit to make that work, but we would essentially hide a behavior that doesn't have anything to do with returning or calculating a `Vector2`. This means that if we wouldn't follow along the implementation we wouldn't know what's happening. This entanglement of concerns is a potential error generator.

Now, like before, this isn't a hard rule even though we say _never_. For example, there's a lot of times when we want to return a check, a `bool` value from within a function upon the successful execution of a behavior. The above `party_walk` function could be rewritten like this:

{{< highlight gdscript >}}
func party_command(msg: Dictionary = {}) -> void:
  var leader := party.get_member(0)
  if leader == null:
    return

  var path := prepare_path(leader, msg)
  if party_walk(leader, path):
    var destination := get_party_destination(path)
    emit_signal("party_walk_started", {"to": destination})

...

func party_walk(leader: Actor, path: Array) -> bool:
  if leader.is_walking:
    return false

  for member in party.get_members():
    if member != leader:
      path = [member.position] + path
      path.pop_back()
    member.walk(path)
  return true
{{< / highlight >}}

Typically, returning `bool` values like this in order to validate a successful execution is a decent idea. _So keep in mind once more, these are just guidelines!_


## Events bus: Observer pattern for Godot

*Thanks to Ombarus for sharing this design pattern. He presented it in [a devlog video](//www.youtube.com/watch?v=fyh2ZjAFMZM) on his YouTube channel.*

Maintaining signal connections isn't the easiest, especially when declaring connections via code. Godot 3.1 doesn't offer any visual cues for signals connected through code as opposed to signals connected with the editor.
There are different advantages to connecting signals through the editor or via code.

### Connecting signals through the editor's node tab

- You can see an icon next to nodes that are connected to another node in the scene tree
- The code doesn't get cluttered with connection declarations

### Connecting signals via code

- You can connect any node, including those you create at runtime and those that aren't present in the current scene
- You can search calls to the `connect()` method globally in the project.
- Contrary to the editor, you're not limited to using `Node` only: any `Object` can define, emit, and connect signals. See the [Object class's docs](//docs.godotengine.org/en/latest/classes/class_object.html).

### Using an Event singleton to avoid spaghetti code

With these guidelines and in our work, we're trying to decouple code to create independent, reusable, and scalable systems. This comes at a cost: we lose the ability to easily connect signals across independent systems and it tend so lead to spaghetti code. The Event singleton is a pattern to reduce this effect at the expense of introducing a global dependency.

Referring back to [Fig. 1], we couldn't directly connect a signal in a deeply nested node from `DialogSystem` to a nested node in the `Board` tree branch while following the decoupling guidelines.

One solution is to declare the signal connection between those systems in a script attached to the `Game` node. The problem is that we can lose track of connections since they're not declared in the scripts attached to the nodes that need these connections themselves.

In a complex system, you might have hundreds of signals emitted and connected all over the place. To manage this we can use dedicated `Events` [singletons (autoloaded scripts)](//docs.godotengine.org/en/latest/getting_started/step_by_step/singletons_autoload.html):

*Note: the name of the script doesn't matter.*

Here's an example `Events.gd`:

{{< highlight gdscript >}}
signal party_walk_started(msg)
signal party_walk_finished(msg)

...

signal dialog_system_proceed_pressed(msg)
signal dialog_system_cancel_pressed(msg)

...

signal battle_started(msg)
signal battle_finished(msg)
{{< / highlight >}}

This singleton only lists signals that can be emitted and connected to, that's it. A "deeply" nested node like `$Game/Party/Godette/Walk` could then emit the appropriate signal directly using the global `Events` node: `Events.emit_signal("party_walk_started", {destination = destination})`, `Events.emit_signal("party_walk_finished", {})`. Other nested nodes could connect to these signals: `Events.connect("party_walk_started", self, "_on_Party_walk_started")` etc.

This way, we can encapsulate signal connections in the related nodes instead of managing them in the code of some parent script, like `Game`.
