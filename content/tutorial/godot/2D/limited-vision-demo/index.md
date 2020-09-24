+++
title = "Limited Player Vision"
description = "Learn how to make limited player vision with lights and masks."
author = "azagaya"

date = 2020-09-23T17:55:55-03:00
weight = 5
draft = true

difficulty = "beginner"
keywords = ["Light Masks", "Limited Vision"]
+++

In this tutorial, you will learn how to make a player with limited vision using `Light2D` nodes. 

The limited vision mechanic consists of:

 - Enemies outside vision range should not be visible.
 - Lights and shadows should affect the environment.
 - Walls should interrupt line of sight.
 
 {{< video "final-result.mp4" "720" >}}

You can download the full project of this tutorial [here](https://github.com/GDQuest/godot-mini-tuts-demos/tree/master/2d/limited-player-vision).

We are going to use two `Light2D` nodes to implement this effect. One is going to add light and shadows to the environment, while the other is going to occlude the enemies outside the lit area.

For the first light, adding a texture and checking _Shadows->Enabled_ is enough. Also, leave only _Layer 1_ enabled in  _Range->Item Cull Mask_, and check that _Mode_ attribute is set to _Add_.

{{< note >}} There is also a _Shadow->Item Cull Mask_ property. Make sure to set the one under the _Range_ group. {{< /note >}}

![Settings of First Light](img/lightAdd-settings.png)

For the second light, besides adding a texture and enabling shadows, change the _Mode_ to _Mask_, and set _Range->Item Cull Mask_ to cull _Layer 2_. With this, the light only applies the mask to nodes with _Layer 2_ enabled in _Visibility->Light Mask_.

{{< note >}} The light in _Mask_ mode only occludes nodes within its range. So, make sure the light's texture covers the entire viewport. {{< /note >}}

![Settings of First Light](img/lightAdd-settings.png)

All nodes you want the mask to occlude, should have _Layer 2_ layer enabled in _Visibility->Light Mask_. In the demo project, the _Player_ and _TilemMap_ nodes have only _Layer 1_ enabled in _Visibility->Light Mask_, and _enemies_ have both _Layer 1_ and _Layer 2_. As a result, the mask will only occlude enemies.

![Settings of the Player](img/player-light-settings.png)

![Settings of the Enemy](img/enemy-light-settings.png)
