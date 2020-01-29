+++
author = "nathan"
date = "2020-01-16T10:34:54+02:00"
description = "This guide covers some best practices to write solid GDScript code, to keep a sane code-base when developing projects of growing sizes."
title = "Best Practices: Godot GDScript - Event Bus"
menuTitle = "Event Bus"
+++

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
