+++
title = "Drawing a character's silhouette"
description = "Display the silhouette of a character hidden behind a wall."
author = "azagaya"

date = 2021-01-23T13:26:00-03:00
weight = 5

difficulty = "beginner"
keywords = ["godot silhouette tutorial", "godot xray", "godot see through walls", "godot character outline"]
+++

In this tutorial, you will learn how to use viewports and shaders to display a silhouette when a wall hides a character in Godot.

{{< video "videos/silhouette-final-result.mp4" "720" >}}

To achieve that, we'll use a viewport and two small shaders to draw the hidden part of a sprite as a silhouette and the rest normally. We'll use a trick that consists of rendering a specific color value to the screen texture and use that to detect when a wall occludes a character.

_You can find the open-source demo for this tutorial on our [Godot mini tuts repository](https://github.com/GDQuest/godot-mini-tuts-demos/tree/master/shaders/silhouette2D)._

## Setting up the Character scene

Start by creating a new scene with a `KinematicBody2D` as the root node.

Add a `Viewport` node to the scene and an `AnimatedSprite` as a child of the viewport.

We will use the viewport to render the character's animations to a texture, then we'll use the image .

Add two `Sprite` nodes to the scene, and name the first one as _Mask_ and the second as _Sprite_.

Select the _Sprite_ and, in the _Inspector_, set its _Z Index -> Z Index_ to a high value like `100`. We'll use it to display the silhouette, which we want to render above walls and other objects. That's why we want to set the z-index so high.

Also, as we will use this in a top-down oblique example, set the offset of both sprites to `(0, -16)` to align the guard's feet with the scene's origin.

Also, add a `CollisionShape2D` as a child of the `KinematicBody2D` and in the _Inspector_, give it a `RectangleShape2D`. 

Your scene should look like this:

![Character Scene](images/character-scene.png)

Next, let's configure the viewport. Select the _Viewport_ node and set both its _Width_ and _Height_ to `32`. 

Make sure to check the _Transparent Bg_ option. Without this, the rendered texture will have a solid background color.

{{< note >}}
You should adapt those values to the size of the sprite(s) you want to render inside the viewport.
{{< /note >}}

Under the _Render_ category in the inspector, disable _HDR_ and change the node's _Usage_ to _2D_. Also, check the option _Render Target -> V Flip_, as, by default, the texture will render upside-down.

Lastly, change the _Update Mode_ property to _Always_. Your viewport's settings in the inspector should look like this:

![Settings of Viewport](images/viewport-config.png)

As the viewport's top-left corner corresponds to the scene's origin, we need to offset the _AnimatedSprite_ node or it'll get cropped. Set its _Transform -> Position_ to `16` in both `x` and `y`.

{{< note >}} Remember to set an animation to the `AnimatedSprite` using the provided assets. Configuring an animated sprite is beyond the scope of this tutorial. {{< /note >}}

You won't see anything yet, because we need to set what the viewport is rendering as the texture for both sprites. So, for both _Mask_ and _Sprite_, in the _Inspector_, set their _Texture_ to a _New ViewportTexture_ and assign the viewport node to that viewport texture. Once you've done that, you should see the animation.

For testing purposes, I added the following script to the `KinematicBody2D` node to move it:

```gd
extends KinematicBody2D

export var speed := 100.0

onready var animated_sprite := $Viewport/AnimatedSprite


func _physics_process(_delta) -> void:
	var direction := Vector2(
		Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left"),
		Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	).normalized()

	move_and_slide(direction * speed)

	if direction.x != 0:
		animated_sprite.scale.x = sign(direction.x)
```

Save this scene as `Character.tscn`
	
## Shaders

We are going to use two shaders to accomplish this effect. Add a shader to the sprite called "Mask" with the following code:

```glsl
shader_type canvas_item;

void fragment() {
	float a = texture(TEXTURE, UV).a;
	COLOR = vec4(10.0) * a;
}
```

This simple shader will set 10 to all three RGB channels of the texture while keeping the transparent area. We will use that color because it is a color that we shouldn't have in any other rendered texture, as normally color channels take values from 0 to 1. So, whenever we sample a color with 10 in one of the RGB channels, we know we are sampling the mask.

Let's add another shader to the second sprite, with the following code:

```glsl
shader_type canvas_item;
uniform vec4 silhouette_color : hint_color;

void fragment() {
	vec4 screen_color = texture(SCREEN_TEXTURE, SCREEN_UV);
	vec4 tex_color = texture(TEXTURE, UV);
	COLOR = tex_color;
	if (screen_color.r < 10.0){
		COLOR.rgb = silhouette_color.rgb;
	}
}
```

We declare a uniform for the silhouette color so that you can change it according to your game. In this shader, we sample the screen's texture and the sprite's texture. We then assign the sprite's texture color to the `COLOR` out built-in parameter. 

If the sampled screen color is less than 10, it means that some other object hides the mask. In that case, we need to show the silhouette color. Otherwise, we should use the texture's color.
	
## Level scene

Let's create a level with a top-down oblique perspective for testing purposes. Create a scene with a `Node2D` as root, and add a `TileMap` and name it "FloorTileMap". Add an `YSort` node, with a `TileMap` child named "WallsTileMap". Also, add an instance of the character scene as a child of the `YSort`. Explaining what the `YSort` node does is out of the scope of this tutorial, but you can check the official documentation [here](https://docs.godotengine.org/en/stable/classes/class_ysort.html).

The `TileMap` inside the `YSort` is for the level's walls, and the one outside is for the floor. The reason for this setup is that we need the walls sometimes to render behind the player and other times in front of the player. So we need them to be in a tilemap affected by the `YSort`. As the floor is always to be rendered behind, we set it in a separated `TileMap` outside the `YSort` and above it in the scene tree.

For the "WallsTileMap" to be rendered as we expect, check the "Cell -> Y Sort" option in the inspector, and change the "Cell -> Tile Origin" to "Bottom Left". As the Guard's feet are placed at the character's scene origin, with the tile origin set to the bottom left corner, we ensure that as soon as the character's foot surpasses the wall tile's bottom left corner, it will be rendered behind it.

Set up the tilemaps using the provided assets, and create a level like this:

![Level scene](images/level-scene.png)

When setting up the wall tilemap, make sure to set the collision polygon at the bottom of each wall tile. This is needed for this example to work in this perspective. For example, these are the collisions used in the example project:

![TileMap collisions](images/tilemap-collisions.png)

Finally, execute the level scene, and check that the silhouette appears when a wall hides the character.

## Final Exercise

Modify the silhouette shader to show an outline instead of a silhouette when the Character is hidden behind a wall. The final result should look like this:


{{< video "videos/outline-final-result.mp4" "720" >}}
