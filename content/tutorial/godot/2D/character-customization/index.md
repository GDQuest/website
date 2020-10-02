+++
title = "Character Customization"
description = "Learn how to customize your character in-game."
author = "azagaya"

date = 2020-09-30T19:22:42-03:00
weight = 5
draft = true

difficulty = "beginner"
keywords = ["customization"]
+++

In this tutorial, you will learn how to customize a character through a GUI and see the results in real-time. In the end, you will be able to customize the __hat__, the __head__ and the __sunglasses__ of the character.

{{< video "final-result.mp4" "720" >}}

You can download the full project of this tutorial [here](https://github.com/GDQuest/godot-mini-tuts-demos/tree/master/2d/character-customization).

For selecting the desired textures for each part of the character, we will make a GUI that lets the user choose between the different options. As the code for changing any of the parts is the same, we are going to make a single scene with the functions to cycle between the available textures. Then we are going to use three instances of that scene to build the final GUI.

## Sprite Selector Scene

Start by creating a new scene, with a `Control` node as root, and name it _UISpriteSelector_. Add to the scene two `Button` nodes, and a `TextureRec`. Name the buttons _PreviousButton_ and _Next Button_. They will be used to cycle between the possible textures, and the `TextureRect` will display the currently selected one. Arrange the scene so it looks like this:

![Sprite Selector scene](img/sprite-selector-scene.png)

Attach a 
new script to the _UISpriteSelector_, and give it a class name, so you can create variables of this class later.

```gd
class_name UISpriteSelector
extends Control
```

We want the _UISpriteSelector_ to be able to notify when the user changed the texture. So, declare a signal called `sprite_changed`. This signal must have a parameter, so you can pass the newly selected texture.

```gd
signal sprite_changed(texture)
```

We need an array to hold all the possible textures the user can choose. We also need an integer to hold the index of the currently selected texture in the array. Let's declare an empty array called `_sprites`, and an integer called `_index`. Every time we change the `_index` value, we also want to update the texture. In other words, the index and the texture are tied to one another. Using a setter function makes it explicit that the process is tied to the property.

```gd
var _sprites := []
var _index := 0 setget _set_index
```
Also, let's declare a variable that holds the reference to the `TextureRect`, so we can access it easily later.

```gd
onready var texture_rect: TextureRect = $TextureRect
```
Note that the `onready` keyword will make this assignment happen after the scene is ready, so we are sure that the referenced node already exists and it is in the tree.

Let's code the _setter_ function above. The function should modify the `_index` value, pick the texture corresponding to that index, assign it to the `texture_rect->texture` property, and emit the signal to notify about these changes.

```gd
func _set_index(value: int) -> void:
	_index = wrapi(value, 0, _sprites.size())
	var texture: StreamTexture = _sprites[_index]
	texture_rect.texture = texture
	emit_signal("sprite_changed", texture)
```

The `wrapi` function "wraps" an integer value between a minimum and maximum value, passed as parameters. In the code snippet above, the value to wrap is `value`, the minimum is `0`, and the maximum is `_sprites.size()`. With this function, when the `_index` variable exceeds the index of the last sprite, it will return to zero. Also, when the index takes the value `-1` it will become the maximum minus one (`_sprites.size()-1` in this case). With this function, we can cycle through all the available sprites in the `_sprites` array, in both directions.

Now we need to code the function that will be called when the user presses the buttons. When pressing the `PreviousButton`, we want the `_index` to decrease by `1`. Similarly, when pressing the `NextButton`, `_index` should increase by `1`. So let's make two functions for that:

```gd
func _on_PreviousButton_pressed() -> void:
	_set_index(_index - 1)


func _on_NextButton_pressed() -> void:

	_set_index(_index + 1)
```

Calling the `_set_index` setter function will both update the value of the `_index` variable, and select the corresponding texture. 

Connect the `pressed` signal of _PreviousButton_ and _NextButton_ to the corresponding functions above. With this, the functions will run when pressing the buttons.

Finally, 
let's make a `setup` function. We will use this function to pass the sprites this scene should contain on its `_sprites` array.

```gd
func setup(sprite_textures: Array) -> void:
	_sprites = sprite_textures
	_set_index(0)
```

After assigning the corresponding textures to the `_sprites` array, we call `_set_index(0)` to select the first texture in the array.

## Character Customizer Scene

We can use the _UISpriteSelector_ scene created previously to build a GUI that allows the user to customize the character. Create a new scene with a `Control` as a root node. Name it _UICharacterCustomizer_. After that, add a `Panel` node to the scene. We are going to use it as a background for the GUI. Add also a `VBoxContainer` as a child of the `Panel`. We will add the _UISpriteSelector_ instances as children of this container, so they automatically arrange as rows. Your scene should look like this:

![Character Customizer scene](img/character-customizer-scene.png)

In the image above, we placed the scene in the top-left corner, because we want to have the customization controls there.

Let's attach a new script to this scene. We need signals to notify the character that a texture was changed by the user:

```gd
extends Control

signal hat_changed(texture)
signal head_changed(texture)
signal glasses_changed(texture)

```

We are going to use a dictionary to hold all the available textures for the customizable parts of the character.

```gd
const DATA := {
	"hat" :
	[
		preload("Sprites/hat1.png"),
		preload("Sprites/hat2.png"),
		preload("Sprites/hat3.png")
		],
	"glasses" : [
		preload("Sprites/sun-glasses1.png"),
		preload("Sprites/sun-glasses2.png"),
		preload("Sprites/sun-glasses3.png")
		],
	"head": [
		preload("Sprites/head1.png"),
		preload("Sprites/head2.png"),
		preload("Sprites/head3.png") ]
	}
```

Note that each key of the dictionary refers to a customizable part of the character. Each entry of the dictionary contains an array with all the possible textures for each part.

When the scene is ready, we should populate the GUI. Add a loop in the `_ready()` function that adds an instance o _UISpriteSelector_ for each part of the character. In there, we will call the `setup()` function of the sprite selector with the corresponding textures. Also, we are going to connect the `sprite_changed` signal of the sprite selector with a function called `_on_SpriteSelector_sprite_changed()`. We are going to define that last function later.

```gd
func _ready() -> void:
	for key in DATA:
		var textures: Array = DATA[key]
		var sprite_selector: UISpriteSelector = sprite_selector_scene.instance()
		vbox_container.add_child(sprite_selector)
		sprite_selector.setup(textures)
		sprite_selector.connect("sprite_changed", self, "_on_SpriteSelector_sprite_changed", [key])
```
Note that we added an extra `key` parameter to the signal connection. In each iteration of the loop, the `key` variable takes a string value corresponding to one of the customizable parts of the character. Passing this value in the signal connection lets us know what part of the character changed.

Finally, let's declare the remaining function. On it, we are going to emit the signal corresponding to the changed part.

```gd
func _on_SpriteSelector_sprite_changed(texture: StreamTexture, key: String) -> void:
	emit_signal(key + "_changed", texture)
```

When calling the `emit_signal()` function, we use `key+"_changed` because `key` contains the name of the part that was changed. For instance, if a __hat__ changes, `key` should be equal to `"hat"`, and thus, `hat_changed` would be emitted. The `texture` parameter of this function comes from the signal defined in the _UISpriteSelector_.

## Character

The only remaining task is making a character to customize. Create a new scene, with a `KinematicBody2D` node as root, and name it _Player_. This character should have a sprite for each customizable part. In this case, we are going to have three sprites, named _Head_, _Glasses_, and _Hat_. Build the scene like in the following image.

![Player scene](img/player-scene.png)

We placed all `Sprite` nodes as children of a `Node2D` called _Body_. With this, we can flip them all at once by flipping _Body_.

Attach a script to the _Player_ scene.

```gd
extends KinematicBody2D

export var speed := 300.0

onready var body := $Body
onready var hat := $Body/Hat
onready var glasses := $Body/Glasses
onready var head := $Body/Head
```

Let's add some movement code to it, for demonstrations purposes only.

```gd
func _physics_process(_delta) -> void:
	var direction := Vector2(
		Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left"),
		Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	).normalized()

	move_and_slide(direction * speed)

	if direction.x != 0:
		body.scale.x = sign(direction.x)
```

In this script, we have to update the textures of each sprite when the user selects a new texture from the GUI. So, add the following three functions.

```gd
func _on_CharacterCustomizer_glasses_changed(texture) -> void:
	glasses.texture = texture


func _on_CharacterCustomizer_hat_changed(texture) -> void:
	hat.texture = texture


func _on_CharacterCustomizer_head_changed(texture) -> void:
	head.texture = texture
```

In the main scene, we are going to connect the signals emitted from the _UICharacterCustomizer_ scene to the three functions defined above.

## Main Scene

Make a new scene from a `Node2D`, and name it _Main_. Add the _Player_ and a `CanvasLayer` to it. Then, add the _UICharacterCustomizer_ scene to the `CanvasLayer` node. This will make the GUI stay fixed in relation to the screen. Remember to connect the `hat_changed`, `head_changed` and `glasses_changed` signals from the _UICharacterCustomizer_, to the matching functions defined in the _Player_ script. This way, when the user changes some texture from the GUI, the character sprite will be updated as well.
