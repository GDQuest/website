---
title: "Godot course: available content"
date: 2018-04-02
author: nathan

category: Godot
tags:
  - Godot 3
  - Godot course
  - Video list
  - Course content

banner:
  src: banner.png
  alt: Screenshot from a level in the course, with the player in the center

layout: single
---

*Last update: April 30*

The course is still in early access, with currently six out of twelve chapters available in the Pro version.

The course comes in 3 versions. Each builds on top of the previous one and adds extra content:

1. [ Hobby ](https://gum.co/vmPA) (*€ 14.95*)
1. [ Indie ](https://gum.co/XEULZ) (*€ 29.95*)
1. [ Pro ](https://gum.co/godot-tutorial-make-professional-2d-games) (*€ 59.95*)

You'll find some **free tutorial samples** below. I also released the [ Finite State Machine ](http://bit.ly/godot-3-fsm-demo) demo open source, for the official Godot documentation.

<p class="note">
All versions come with source Godot projects so you can read the source code, learn from them and even reuse them in your own work! Want to skip ahead in a chapter? There are multiple checkpoint projects with `start` and `end` folders so you can pick up from a different video.
</p>

## Videos list

### {{< tag "hobby" >}} Chapter 1: The character controller

0. Project Structure Overview
1. [ Create the Base Character Scene ](https://www.youtube.com/watch?v=PKGOWGw3blw)
2. Input Map
3. Input Direction
4. Player Walk And Run
5. Character Walk Anim
6. Simple State Machine
7. Bump State Collisions
8. Bump State Animation
9. Jump
10. Jump Part 2
11. Jump Bug Fix And Height Refactoring


### {{< tag "hobby" >}} Chapter 2: Combat mechanics: life, attacks and death

0. Intro
1. [ Basic Attack Animation ](https://www.youtube.com/watch?v=TPJqJDCnxyg)
2. Simple Attack Sword Code
3. Simple Attack Connect With Player
4. Health
5. Health Improving Code Structure
6. Stagger
7. Death
8. Combo Animation
9. Combo Code Setup
10. Combo Input


### {{< tag "hobby" >}} Chapter 3: AI 1: Design 2 simple monsters

1. The Porcupine's States Overview
1. Spawn And Target
1. Follow
1. Arrive
1. Roam
1. Avoid
1. Spot And Attack
1. Refactor To Reuse Steering Code (Part 1)
1. Refactor To Reuse Steering Code (Part 2)
1. When Should You Refactor?
1. Coding The Flying Enemy
1. Coding The Nest That Spawns Flying Enemies


### {{< tag "hobby" >}} Chapter 4: AI 2: Add a pattern-based boss

This chapter covers the state programming pattern. It shows how to separate the monster's behaviors in code

01. First look at the state interface
02. Create the spawn state
03. Create the roam state
04. Create the state machine
05. Code a state sequence
06. The roam sequence
07. Code the charge sequence
08. Make the boss charge
09  Make the boss die!
10. Using the builtin owner feature
11. Dealing and taking damage
12. Simpler attack and hitbox demo
13. Boss phases

### {{< tag "hobby" >}} Chapter 5: Build levels with Tiled map editor

1. [ Intro To Tile-sets ](https://www.youtube.com/watch?v=TdPgIagt9Yo)
2. Create A Tile-set
3. Auto-tiles
4. Working With Tile-maps
5. Auto-tile With 3 By 3 Bit mask
6. Intro To Tiled Map Editing

### {{< tag "hobby" >}} Chapter 6: Breathe life to the game: world animation and particles

Upcoming

### {{< tag "indie" >}} Chapter 7: Design and code the game's User Interface

Upcoming

### {{< tag "indie" >}} Chapter 8: Learn the Game Design Workflow

*The first 3 lessons are text-based*

1. You are a designer
1. A game is made of 4 elements that support a theme
1. Dan the Rabbit: game concept example
4. Why And How To Analyze Games
5. Cross Code Analysis
6. Designer Insights Emmanuel
7. Designer Insights Fibretigre
8. Designer Insights Ed Atomic Racoon

### {{< tag "pro" >}} Chapter 9: Build a Shop and an Inventory

Upcoming

### {{< tag "pro" >}} Chapter 10: Design pattern: implement Finite State Machines in Godot

1. Presentation: Introduction To Finite State Machines
1. Create The Base State Interface
1. Idle And Move State Examples
1. Jump State Class Overview
1. Code The State Machine
1. Hierarchical State Machine
1. Presentation: Going Further With Pushdown Automata
1. Pushdown Automaton
1. Pushdown Stagger State

### {{< tag "pro" >}} Chapter 11: Juicing the game

Upcoming

### {{< tag "hobby" >}} Final chapter: Putting a game demo together

Upcoming

### Extras: Bonus content

These are free tutorials available to everyone on Youtube, funded by the project. They're designed to complement the course.

1. [ Attack Tutorial 1: How To Animate The Sword ](https://www.youtube.com/watch?v=S7jBSs5j4-c)
2. [ Attack Tutorial 2: Code the Sword Attack ](https://www.youtube.com/watch?v=JBczf8qt04c)
3. [ Tool Mode: Draw In the editor's viewport ](https://www.youtube.com/watch?v=XPs-HGzElTg)
4. [ Camera 2d And Grid Snapping ](https://www.youtube.com/watch?v=lNNO-Gh5j78)

### Extras: contributions to the official Godot docs

Thanks to this project, I could dedicate time to Godot's official documentation. I became a reviewer on GitHub and organized 8 documentation writing events that took the built-in code reference from 33% to 70% complete, thanks to the hard work of a few dedicated contributors. We collaborated with [KidsCanCode](https://www.youtube.com/channel/UCNaPQ5uLX5iIEHUCLmfAgKg) to build a much better [Step by Step guide](http://docs.godotengine.org/en/latest/getting_started/step_by_step/index.html) in the official manual.

You'll find some of the work I did bundled with the course.

#### New pages in the docs

Step by step guide:

1. [ Introduction to Godot’s editor ](http://docs.godotengine.org/en/latest/getting_started/step_by_step/intro_to_the_editor_interface.html)
1. [ Godot’s design philosophy ](http://docs.godotengine.org/en/latest/getting_started/step_by_step/godot_design_philosophy.html)
1. [Design interfaces with the Control nodes](http://docs.godotengine.org/en/latest/getting_started/step_by_step/ui_introduction_to_the_ui_system.html)
1. [Design a title screen](http://docs.godotengine.org/en/latest/getting_started/step_by_step/ui_main_menu.html)
1. [Design the GUI](http://docs.godotengine.org/en/latest/getting_started/step_by_step/ui_game_user_interface.html)
1. [Control the game’s UI with code](http://docs.godotengine.org/en/latest/getting_started/step_by_step/ui_code_a_life_bar.html)

Contributing:

1. [Docs writing guidelines](http://docs.godotengine.org/en/latest/community/contributing/docs_writing_guidelines.html)
1. [Contribute to the Class Reference](http://docs.godotengine.org/en/latest/community/contributing/updating_the_class_reference.htm) (rewrite)

#### Demo projects

1. [AStar pathfinding on a 2d grid](https://github.com/GDquest/Godot-engine-tutorial-demos/tree/master/2018/03-30-astar-pathfinding)
1. [Navigation2D](https://github.com/godotengine/godot-demo-projects/tree/master/2d/navigation) (rewrite)
