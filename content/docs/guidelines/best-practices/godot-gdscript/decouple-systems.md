+++
author = "nathan"
date = "2020-01-29T08:11:34+02:00"
description = "This guide covers some best practices to write solid GDScript code, to keep a sane code-base when developing projects of growing sizes."
title = "Best Practices: Godot GDScript - Decouple Systems"
menuTitle = "Decouple Systems"
+++

Decoupled systems:

1. **Can be tested on their own**.
1. Are **black boxes** that are fed data and produce some output. They don't care where they get the data from.
1. **Don't know anything about the outside world**.

This makes them **independent** and **reusable** across game projects. This also makes them **composable**. We can create complex systems using **aggregation**: by adding several decoupled nodes to a scene and and using them from a parent node.

See the Player in our Godot Metroidvania project. It's an aggregate of scenes: you can remove any of the nodes in the screenshot below and the player will still work without errors.

![Player scene tree example in Godot](../img/aggregation-player-scene-tree.png)

{{< note >}}
**Aggregation**

In Object-Oriented Programming, aggregation is a type of **association** between objects. Aggregation means that one object, our `Player` in the example above, uses others, like the `Hook` or the `CameraRig`. The `Hook` and the `CameraRig` can keep working even if we remove the association with the `Player` node.
{{< / note >}}

### Every building-block scene should run by itself without errors

**If you save a branch as an independent scene, it should run without any errors on its own**, this is the golden rule.

Godot relies on its node tree, a recursive data structure: if we pick any node in the tree, this node, together with all of its children, is a tree itself. You can consider each branch of the scene tree as an independent scene.

{{< figure
    src="../img/scene_tree.png"
    caption="Screenshot of a real system scene tree layout from [OpenRPG](//github.com/GDQuest/godot-open-rpg)"
    alt="../img/scene_tree.png" >}}

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
    src="../img/node_closeup.png"
    caption="Fig. 3: A Node/Scene is composed of state and behavior"
    alt="../img/node_closeup.png" >}}


Fig. 3 depicts a typical node or scene in Godot. It bundles up state and behavior that can access the state at any time and alter it. But even more so, the lines coming in from the outside depict here other types of interactions that could happen from the external world (other systems):

- access to state directly, potentially changing it
- access to behavior, i.e. methods
- connections to methods via signals

Even a simple scene tree like the one in Fig. 4 can quickly become unmaintainable if all the flexibility Godot offers us isn't managed. Thus we need a way to maintain the number of potential connections as depicted in Fig. 3.

{{< figure
src="../img/scene_tree_overview.png"
caption="A relatively simple depiction of a Godot scene tree. The highlighted part represents a completely independent scene"
alt="../img/scene_tree_overview.png" >}}

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
    src="../img/openrpg_scene_tree.png"
    caption="[OpenRPG](//github.com/GDQuest/godot-open-rpg) experimental branch scene tree."
    alt="../img/openrpg_scene_tree.png" >}}

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
This way, we can encapsulate signal connections in the related nodes instead of managing them in the code of some parent script, like `Game`.

