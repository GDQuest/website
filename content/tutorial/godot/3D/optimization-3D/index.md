+++
title = "Optimizing a 3D scene"
description = "Improve your framerate in 3D by optimizing meshes and materials"
author = "razoric"

date = 2020-08-21T14:22:00-04:00
weight = 5
draft = true

difficulty = "beginner"
keywords = ["tutorial"]
+++

Rendering in 3D is more complex than in 2D, but some knowledge of how your rendering engine of choice renders its scenes can make it easier to know why your 3D scene is slowing down. Knowing where you can compromise to draw out more performance is important. In this tutorial, we're looking over the tools you have to know why your framerate may be low and what you can do to bring it up.

## The first step: Discount game-play suspects

[Measure your code](../../gdscript/optimization-measure) first to make sure that the reason your framerate is dropping isn't because of your game code or the engine struggling with the workload.

## The graphics Monitors

![The Godot monitors](monitors.png)

The Profiler measures functions and the Monitors measure individual systems in Godot, including the 3D renderer. Where the Profiler measures in milliseconds, the Monitors measure in number of _tasks_.

For 3D, the monitors relevant to rendering are under the _Raster_ category: objects drawn, vertices drawn, mat changes, shader changes, surface changes and draw calls. You use these statistics to figure out what, in particular, is slowing the rendering down.

Mat changes is when the CPU tells the GPU to switch to a new material, shader changes is when changing shader code, and surface changes is changing geometry. Godot tries to optimize the render order to make fewer of these changes as possible. Draw calls are the CPU telling the GPU to render something.

## Optimizing away draw calls and state changes

The GPU is an excited hunting hound held back by a harness. It's ready to go and is waiting for the grip to loosen so it can go as fast as it can. But before it goes, the CPU has to prepare it. It has to tell it what it's about to draw, what data to use, and in what order. The more work the CPU has to do, the longer the GPU waits and the lower the framerate. Communication to the GPU is a lot slower than a GPU on its own, so minimizing that prep time is vital to a low framerate.

Here are some common considerations for speeding up a 3D scene.

### Reducing draw calls by optimizing meshes

When the GPU draws something, Godot provides it with the 3D model's vertex data to draw. Ideally, it draws as much of the model in one shot as possible to reduce the amount of back-and-forth with the CPU as possible. But this dynamic batching is not a feature of Godot and is something you have to make happen. If you have a house made up of walls, windows, a roof, a floor, a door and a chimney, and each of those objects is a separate surface, you could be looking at 10 or more draw calls, repeated across all the houses. In your 3D software of choice, try to combine such meshes together into one surface, such as with Blender's `Join` command.

If you draw the same mesh, each of those is going to be a separate draw call. For meshes that look the same except for where they are and which way they are facing, consider using a MultiMeshInstance. It's a special node that takes one mesh and draws it many times in one single draw call by assigning each instance a unique 3D Transform and, optionally, some custom data. It takes some code to set up, but drawing an enormous city full of similar looking buildings is a lot easier on the framerate that way.

### Reducing draw calls with fewer lights and shadows

Lights are somewhat complex in Godot and they behave differently depending on the light type.

Local light sources, that is omni and spot lights, without shadows add zero draw calls, but an object has a max of 8 light sources and which lights it uses come in order in the scene tree and then distance. Omni and spot lights that use shadows add four draw calls per light per object whenever the light or the object updates. That means shadows are free so long as the light and objects it illuminates and that casts shadows do not change.

Directional lights add one draw call per light per object instance, though the first light replaces the one in the world environment and is free. Casting shadows with directional lights adds four draw calls per light per object. Directional shadow maps are not cached like omni or spot lights and get redrawn every frame.

One more way to have great lighting on your static scene without actually using dynamic lights is to use [Baked Lightmaps](https://docs.godotengine.org/en/stable/tutorials/3d/baked_lightmaps.html), either using Godot's system or an outside one.

### Reduce material and shader changes

While Godot does its best to sort objects to minimize state change like switching materials and shaders, it has its limits. You can help it along by giving the same material _instance_ to more objects. For example, small objects could have their UVs occupy different places but they end up sharing the same texture map. That way, they can have the same material instance.

Do not rewrite shaders with the same code. Save the shader and re-use it to reduce the number of shader changes.

## The graphics card's amount of work and fill-rates

Once the CPU gives the go-ahead, the GPU can do all the work it needs to do on its to-do list. But even though it's blazing fast at its job, it still has limits. Once you've done as much as you can to lower the amount of work the CPU has to do before the GPU can do its job, you have to look at the job the GPU has to do and see if there are any gains you can have.

### Reduce overdrawing

Godot hides what is outside the bounds of the camera (frustum culling) but it does not do tests to check whether objects are behind walls. Overdrawing means drawing objects despite them being behind other objects and, as a result, not visible. This results in effort wasted by the GPU.

You should design your levels and scene trees in such a way that you can toggle visibility on large portions of your level when you know it will be invisible. When the player steps into a closed room, automatically close the door behind them and hide the rest of the level until they open the door. Have clever wall placement so that players cannot see the level geometry outside them and hide it, which gives you a great place to put triggers going in and out that hide geometry.

### Reduce the amount of vertices to draw

You can start by removing vertices that you cannot see. If you have a house that the player will never be able to look behind, you can remove the floor and back walls. You don't need an interior if the player cannot look inside.

If the player can see the whole object but it's far away, don't be shy about lowering the amount of details. A lot of videos games have hilariously under-detailed birds but they are so far away and so small and moving so fast that the effect is convincing anyway.

Lower the amount of vertices you use on spaces that don't need the vertices. If you have a large wall, it probably does not need to have 300 edge loops running along it. Bake details down into a normal map instead of individually modeling bricks.

### Reduce the amount of pixel and texture work

GPUs have two fill rates when it comes to pixels: the pixel fill rate and the texel fill rate. The first is the pixels it's able to push to the display. Lowering the internal resolution of your game and scaling up is one possible way to lower the work needed by the GPU. Games on lower end hardware like consoles frequently downscale to maintain frame rate.

The texel fill rate is the pixels it can apply to a fragment through reading textures and sampling them along UVs. Having fewer smaller textures can let you stay within budget for even lower end hardware.

### Optimize shader code

When writing shader code, expensive calculations can happen on the vertex shader instead of the fragment shader, then interpolated across using a `varying` variable. In most cases, there are fewer vertices than there are fragments.

If you have a lot of data you can pre-calculate, consider encoding it into a texture and looking up the value with a call to `texture` instead of calculating it on the fly per fragment.

Ensuring your code runs as fast as possible and does not use dynamic branching can give you performance gains.
