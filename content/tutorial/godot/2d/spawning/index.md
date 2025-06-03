---
author: henrique
coAuthors:
- johnny
date: "2020-07-24T15:27:28-03:00"
description: ""
difficulty: beginner
keywords:
- instance
- spawner
- spawn object
- create object
- tutorial
software: godot
title: Spawning
weight: 5
---

When we play games such as MMORPGs, it's common to ask experienced players, "Where does this monster spawn?".

We call the ability to create new enemies and objects in the game's world _spawning_. A spawner is an invisible position in the game's world that creates instances of an object or monster. Spawning is the bread and butter of game development.

Here are some common uses:

- Spawning bullets from a gun
- Creating choreographed enemy waves
- Spawning particles
- Casting a spell from a specific point

{{< video "demo.mp4" >}}

The first thing to do is create a new scene with a _Position2D_ as the root. We can see _Position2Ds_ in the Editor, but they're invisible for players. Let's name it _Spawner2D_.

Attach a new script to the _Spawner2D_ and export a new _PackedScene_ variable. This variable will hold the object scene that will spawn.

```gd
extends Position2D

export var spawn_scene: PackedScene
```

Let's work on the spawning logic. We want to create new `spawn_scene` instances at the _Spawner2D_ position, then add them as its children. There's a problem, though; when the _Spawner2D_ moves, its children also move. To prevent this, we need to `set_as_toplevel(true)` every time we instance a new `spawn`.

```gd
func spawn(_spawn_scene := spawn_scene) -> void:
  # Creates a new instance of the _spawn_scene
	var spawn := _spawn_scene.instance() as Node2D

	add_child(spawn)

  # Prevents the Spawner2D transform from affecting the new instance
	spawn.set_as_toplevel(true)

  # Move the new instance to the Spawner2D position
	spawn.global_position = global_position
```

And that's it!

You can mix the _Spawner2D_ with other nodes to achieve many exciting systems—especially when combined with an _AnimationPlayer_ since you can animate the `spawn_scene`.

In our project's demo scene, we used two _Spawner2Ds_. One spawns bullets from the player's gun, and the other spawns enemies. The _EnemySpawner2D_ uses an animation to dictate where and when to create new enemies. The Player's _BulletSpawner2D_ triggers its `spawn()` based on the player's input.
