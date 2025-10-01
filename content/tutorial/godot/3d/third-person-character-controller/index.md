---
author: nathan
date: "2024-10-03"
description: Code your first 3D third-person character controller in Godot 4, step-by-step, for free!
difficulty: beginner
keywords:
- godot 4 3d tutorial
- godot 4 beginner tutorial
- godot 4 third person controller
- 3D character controller godot 4
menuTitle: Third Person Character
programVersion: "4.3"
resources:
- name: banner
  src: thumbnail_3d_character_controller.webp
software: godot
sort: 50
title: Create a 3D Character Controller in Godot 4
weight: 1
type: video
videoId: JlgZtOFMdfc
type: redirect
redirect: https://gdquest.com/library/character_movement_3d_platformer
---

## Download the Godot template

In this tutorial, you will learn to code a 3D, third-person character controller in Godot 4.

This tutorial assumes that you have:

- Godot foundations
- Programming foundations
- Godot 3D basics knowledge

Click the button below to download the Godot project.

{{< calltoaction
url="https://github.com/gdquest-demos/godot-4-3d-character-controller-tutorial/archive/refs/tags/1.0.0.zip"
text="Download The Godot Files"
class="-large -tall" >}}

This project is for **Godot 4.3** and above and comes with everything you need to focus on learning about coding a character controller:

- A game level
- Predefined input maps
- Sophia, our 3D animated mascot
- In the `lesson_reference/` folder, you'll find code checkpoints for different chapters of the video

Import the project in Godot 4.3 to get started.

If you want to go further and support our open-source work, check out [Learn Gamedev From Zero with Godot](https://school.gdquest.com/products/godot-4-early-access). It's a complete curriculum we're building to learn game development with Godot, starting from zero, available in early access.

## Bonus code snippets

You can go a lot further with this character controller. After completing the tutorial, the snippets below will help you improve the character's feel.

### Sharper stop

The character slides a bit when the player releases the movement keys. To make the character stop more abruptly, you can add a stopping speed. When the character's velocity is below this threshold and the player is not moving, set the velocity to zero:

```gdscript
@export var stopping_speed := 1.0


func _physics_process(delta: float) -> void:
	# ...
	if is_equal_approx(move_direction.length(), 0.0) and velocity.length() < stopping_speed:
		velocity = Vector3.ZERO
	# ...
```
