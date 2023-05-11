---
author: nathan
categories:
- news
date: "2022-12-24"
description: "We're happy to release our first free and open-source demo for **Godot 4**! This demo contains a 3D character controller inspired by games like Ratchet and Clank or Jak and Daxter."
resources:
- name: banner
  src: banner.jpg
title: "Introducing Our Free Third-Person Character Controller (Godot 4)"
weight: 5
---

We're happy to release our first free and open-source demo for **Godot 4**! This demo contains a 3D character controller inspired by games like Ratchet and Clank or Jak and Daxter. You can copy the character to your project as a plug-and-play asset to prototype 3D games with and build upon.

It features a character that can run, jump, make a melee attack, aim, shoot, and throw grenades.

{{< video "shooting.mp4" >}}

There are two kinds of enemies: flying wasps that fire bullets and beetles that attack you on the ground. The environment comes with breakable crates, jumping pads, and coins that move to the player's character.

{{< calltoaction url="https://gdquest-demos.github.io/godot-4-3d-third-person-controller/" text="Get the Godot 4 project" >}}

*This project requires at least Godot 4 beta 7 to work. There are some [known issues](https://github.com/gdquest-demos/godot-4-3d-third-person-controller/issues) in various beta releases.*

### How do I use the player character in my game?

Copy the following folders into the root of your project:

- `Player`: contains the main Player assets and scenes.
- `shared`: contains shaders used by the player asset.

The following `Input Map` actions are needed for the `Player.tscn` to work:

- `move_left, move_right, move_up, move_down`: move the character according to the camera's orientation.
- `camera_right, camera_left, camera_up, camera_down`: rotate the camera around the character.
- `jump, attack, aim, swap_weapons`: Action buttons for the character.

The `Player.tscn` scene works as a standalone scene and doesn't need other cameras to work. You can change the player UI by changing the `Control` node inside `Player.tscn`.

## License:

All code is MIT-licensed, and assets are CC-By 4.0 GDQuest (https://www.gdquest.com/).

You can find the source code on the [GitHub repository](https://github.com/gdquest-demos/godot-4-3d-third-person-controller/).
