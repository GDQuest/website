---
author: nathan
date: "2021-04-13"
description: ""
menuTitle: Your first 2D game
publishDate: "2021-04-15"
title: Code your first complete 2D game with godot
type: video
videoDuration: 4296
videoId: WEt2JHEe-do
weight: 10
---

In this lesson, you will get to create a complete 2D game from scratch and step-by-step.

This video is based on an open-source game by [KidsCanCode](http://kidscancode.org/godot_recipes/).

We go over a lot of code, so I don't have the time to explain how every single node works or other features it offers; it would make the video extremely long and tedious.

Here, you will be learning by example.

The goal is for you to create a complete game to see the entire process in one hour.

You will learn to:

1. Create a complete game from start to finish.
1. Code a player with simple animations.
1. Use code to spawn enemies around the screen randomly.
1. Design and code interface to start and replay the game.
1. Count and display the player's score.
1. Code a game over condition and restart the game.

You can download the starter project here: [Dodge the Creeps starter assets](https://github.com/GDQuest/godot-getting-started-2021/releases/tag/0.3.0)

Below, I give you a few more insights regarding the yield keyword we use in the tutorial. You can read on after watching the video.

## The yield keyword and coroutines

When you use yield in a function, it causes it to stop execution. The function then waits for a signal and resumes at a later time.

Here's how it works under the hood.

When you call a function, the GDScript compiler creates an object in memory to represent its current state.

This object keeps track of:

- The current line of code being executed. In case there is an error, Godot can tell you on which line it happened.
- Any variable (and value) local to the function. These variables are created with the function and deleted once the call ends.

The object representing the function gets freed from memory as soon as the function returns.

When you use `yield`, Godot keeps the function's state in memory for longer.

These functions that you pause and resume later are called **coroutines**.

We call them that way because they allow functions to delegate work to one another and wait for the result.

You have to be careful with these functions' asynchronous nature. If they don't get the signal back, they never complete and keep piling up in your memory.

You should always test that they are working as expected early, as we did in the course when writing the start game sequence.

In any case, coroutines are a really powerful feature that helps you keep code grouped in one place.

That's it for your first 2D game. In the next lesson, you'll get to create a complete 3D game, from scratch.
