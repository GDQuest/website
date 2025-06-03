---
author: nathan
date: "2020-07-01T00:00:00-06:00"
description: Never format your code by hand again! Let GDFormat do it for you.
difficulty: beginner
keywords:
- godot gdformat
- gdscript toolkit
- gdscript code formatter
- godot code formatter
- gdscript code format
menuTitle: Code Formatter
tags: []
software: godot
title: Format your Code with GDFormat
type: video
videoId: eWbZCQ30vFw
---

Godot 3.2 is lacking a code formatter for GDScript. Formatting your code by hand is a time-consuming process, time you could instead use to code some more.

Thankfully, [Pawel Lampe](https://twitter.com/pawel_lampe) wrote a Python program to save the day, and that's what we're looking at in this short tutorial.

{{% note %}}
A code formatter, also called beautifier, is a program that take your source code and tidies it up for you. 
{{% /note %}}

GDFormat takes code like this:

```gd
enum States { IDLE,
			  RUN,
			  AIR,
			  LAND
			  }

onready var animation_tree  : AnimationTree = $AnimationTree
onready var _playback        : AnimationNodeStateMachinePlayback = animation_tree["parameters/playback"]



func _ready() -> void:
	animation_tree.active      = true
```

And turns it into that:

```gd
enum States { IDLE, RUN, AIR, LAND }

onready var animation_tree: AnimationTree = $AnimationTree
onready var _playback: AnimationNodeStateMachinePlayback = animation_tree["parameters/playback"]


func _ready() -> void:
	animation_tree.active = true
```


## Installing the GDScript Toolkit

GDFormat is part of the [GDScript Toolkit](https://github.com/Scony/godot-gdscript-toolkit), a set of three programs:

1. gdparser, a parser for GDScript.
1. gdlint, a code linter.
1. gdformat, a code formatter.

They all come together in one Python package that you can install via pip, Python's package manager, using your terminal:

```sh
# On Windows
pip install gdtoolkit

# On MacOS and Linux
pip3 install gdtoolkit
```

Once that's done, you can format any file by calling the command `gdformat`:

```sh
# Format a single file
gdformat path/to/file.gd

# Format all gdscript files in the current directory
gdformat *.gd

# Find all gdscript files recursively and format them
# In Bash
gdformat $(find . -name '*.gd')
# In Fish
gdformat **.gd
```

That's it!

## Known limitations

GDFormat should work great with most GDScript code. At the time of writing, there are some exotic bits of GDScript syntax it doesn't support. For example, defining variables in match patterns:

```gdscript
# Executed when entering a State in the StateMachine
func enter(msg: Dictionary = {}) -> void:
	match msg:
		{"velocity": var v, "jump_impulse": var ji}:
			_parent.velocity = v + Vector3(0, ji, 0)
```

But in general, it works well.
