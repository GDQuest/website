+++
title = "Spawning"
description = ""
author = "henrique"

date = 2020-07-24T15:27:28-03:00
weight = 5
draft = true

difficulty = "beginner"
keywords = ["instance", "spawner", "spawn object", "create object", "tutorial"]
+++

When we grind on MMORPGs is common to ask experienced players "Where is the [monster] spawn?". A monster spawn is where new enemies appear.

We call the ability to create new enemies and objects in the game's world _spawning_. The bread and butter of game development.

{{< video "demo.mp4" >}}

A spawner is an invisible position in the game's world that creates instances of an object or monster. So the first thing to do is to create a new scene with a _Position2D_ as root. We can see _Position2Ds_ in the Editor, but they are invisible in run time for players. Let's name it _Spawner2D_.

Attach a new script to the _Spawner2D_ and  export a new _PackedScene_ variable. This is the object it's going to spawn.

```
extends Position2D


export var spawn_scene: PackedScene
```

The real spawning logic comes now. We want to create new `spawn_scene`  instances at the _Spawner2D_ position, then add them as its children. There's a problem tho, if the _Spawner2D_ moves, its children would also move. To prevent that we need to `set_as_toplevel(true)` every time we instance a new `spawn`.

```
func spawn(_spawn_scene := spawn_scene) -> void:
  # Creates a new instance of the _spawn_scene
	var spawn := _spawn_scene.instance() as Node2D

	add_child(spawn)

  # Prevents the Spawner2D transform from affecting the new instance
	spawn.set_as_toplevel(true)

  # Move the new instance to the Spawner2D position
	spawn.global_position = global_position
```

That's it, but you might be thinking "Why was it called bread and butter of game development?". Allow me to explain some use cases for that mechanism.

- Guns are but a bullet spawner
- Enemy waves are but a choreographed spawner of enemies
- Particle systems are particle spawners
- Casting a spell is but spawning it

You can mix the _Spawner2D_ with other nodes to achieve many interesting systems. Especially when in combination with an _AnimationPlayer_ since you can animate the `spawn_scene`.

In our project's demo scene we used two _Spawner2Ds_ one of the player's gun and other to spawn enemies. The _EnemySpawner2D_ uses an animation to tell where and when to create new enemies. As for the Player's _BulletSpawner2D_, it triggers its `spawn()` based on players' input.
