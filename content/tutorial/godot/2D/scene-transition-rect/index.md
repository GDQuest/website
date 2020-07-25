+++
title = "Scene Transitions"
description = "Learn how to make smooth scene transitions in Godot"
author = "henrique"

date = 2020-07-22T16:10:18-03:00
weight = 5

difficulty = "beginner"
keywords = ["transition", "scene change", "load scene", "tutorial"]
+++

_Scenes_ are the building blocks of game development with Godot Engine. They can be simple props, whole levels, or even the entire game world. It's common to have each level or screen saved as an individual _PackedScene_ and use the [`SceneTree.change_to`](https://docs.godotengine.org/en/stable/classes/class_scenetree.html#class-scenetree-method-change-scene) method to transition between them. Here's a quick tip to prevent breaking immersion when transitioning between scenes: make transitions!

{{< video "demo.mp4" >}}

The idea is to locate a _PackedScene_ in the project and perform a smooth fading transition. To make transitions, we need to cover the whole screen and animate the transparency to create a fade effect. We can use a [_ColorRect_](https://docs.godotengine.org/en/stable/classes/class_colorrect.html) node for this. The _ColorRect_ should also fade in only when the new scene is ready to prevent the new scene from displaying too soon.

## Fading Animation

Create a new scene and add a _ColorRect_ as the root. Rename it as _SceneTransitionRect_. On the Layout menu, select the "Full Rect" option.

![Full Rect Layout option](01.full-rect-layout.png)

This layout ensures the _SceneTransitionRect_ covers the whole screen. You can change the _Color_ property to any color you like, but for fading purposes, _Black_ goes well.

For the fade animation, add an [_AnimationPlayer_](https://docs.godotengine.org/en/stable/classes/class_animationplayer.html) as a child of the _SceneTransitionRect_ and create a new animation. Let's name it _Fade_ and set its duration to `0.5`. Since the _SceneTransitionRect_ fades in and out, it takes twice as long, so the total duration is `1.0` second.

In this animation, the _SceneTransitionRect_ starts completely transparent, then becomes opaque at the end. Set the alpha value of the _Modulate_ property's color to `0.0` and add a keyframe. Move the animation's cursor to the end at `0.5` seconds and set the _SceneTransitionRect > Modulate_ alpha back to `255` and add a new keyframe.

![Fading animation keyframes](02.fading-animaiton.png)

## Fixing mouse click issues

If your game doesn't have mouse events, you can skip this section. Otherwise, we need to stop the _SceneTransitionRect_ consuming mouse events. Since it covers the screen and is on top of every other node in the scene hierarchy, it consumes mouse inputs by default.

In the _SceneTransitionRect > Mouse_ category, change the _Filter_ property to "Ignore" to fix this issue. Now let's move on to the actual transition.

## Transition

It's time to code! Attach a new script to the _SceneTransitionRect_. Export a _String_ variable with hints to allow us to browse the file system and search for _PackedScene_ files. We also set up a reference for the _AnimationPlayer_.

```gd
extends ColorRect

# Path to the next scene to transition to
export(String, FILE, "*.tscn") var next_scene_path

# Reference to the _AnimationPlayer_ node
onready var _anim_player := $AnimationPlayer
```

Since we want the _SceneTransitionRect_ to fade in when it's ready, we can perform the _Fade_ animation in the `_ready()` callback and play it backward to start opaque then become transparent.

```gd
func _ready() -> void:
	# Plays the animation backward to fade in
	_anim_player.play_backwards("Fade")
```

Now it's time to code the actual transition. We want the _SceneTransitionRect_ to fade out completely and load the next scene. By default, it should transition to the `next_scene_path`, but we can also pass a different _PackedScene_ path as an argument.

```gd
func transition_to(_next_scene := next_scene_path) -> void:
	# Plays the Fade animation and wait until it finishes
	_anim_player.play("Fade")
	yield(_anim_player, "animation_finished")
	# Changes the scene
	get_tree().change_scene(to)
```

## Using the SceneTransitionRect

There are many use cases for this node. Let's say you have a main menu with three buttons that load different scenes:

- Start
- Options
- Credits

You can attach a script to the topmost node and connect each button `pressed` signal to a callback:

```gd
onready var _transition_rect := $SceneTransitionRect

func _on_StartButton_pressed() -> void:
  _transition_rect.transition_to("res://path/to/Play.tscn")


func _on_OptionsButton_pressed() -> void:
  _transition_rect.transition_to("res://path/to/Options.tscn")


func _on_CreditsButton_pressed() -> void:
  _transition_rect.transition_to("res://path/to/Credits.tscn")
```

### Demo scene

In our project demo scene, we used a _SceneButton_. It's a simple button that also exports a variable so we can browse to a _PackedScene_ path in the file system. It has a custom signal called `scene_prompted`. This is connected to the `SceneTransitionRect.transition_to()` method. When the _Scenebutton_ is pressed, it passes the `scene_path` to the `SceneTransitionRect.transition_to()` method so the transition can start.