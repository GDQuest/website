---
title: "Learn to Make Games with Godot: Developer Edition"
description: This learning path and free guide is a curated list of free resources to transition to and advance with the Free and Open Source engine Godot
author: razvan

type: post

date: 2019-11-11 09:47:26+0200
---

<!-- TODO: link to main contributors guidelines -->

_For a gentler introduction to the concept of game development using the [Godot game engine](https://godotengine.org/) please refer to our previous guide: [Learn to Make Games with Godot: Beginner Edition]({{< ref "open-source/guides/learn-godot/beginner/index.md" >}})._

If you are a game developer or advanced hobbyist and you want to explore or learn Godot, we have gathered and curated a list of resources to make your life easier while transitioning and/or starting out with Godot.

## Making games with Godot

The Free and Open Source Software, Godot, although having had modest beginnings - founded by Juan Linietsky ([@reduzio](https://twitter.com/reduzio)) & Ariel Manzur (punto), it now grows exponentially aiming to be a real competitor against the state-of-the-art game engines out there.

**Godot offers interconnected 2D and 3D** engines under the same editor, with a wide range of features, covering the spectrum for both hobbyists and professional game developers alike.

We believe the following curated list of educational resources will help you transition and learn Godot with ease. It is aimed at game developers with some experience and/or coming from a different game engine.

### From X to Godot

At the time of this writing, there are a few places where you can learn about the differences between other game engines and Godot helping out smoothing the transition:

- [coming from Unity](http://docs.godotengine.org/en/3.1/getting_started/editor/unity_to_godot.html) - the official Godot documentation caters to Unity users covering the conceptual differences between these editors
- [coming from GameMaker: Studio](https://www.youtube.com/playlist?list=PLQsiR7DILTcxma-doUnpoALIX001NvcP_) - Emilio's YouTube series covers the basics of transitioning from GameMaker: Studio v1.4

### Godot UI, themes & much more

One of the more confusing parts of Godot, due to conceptual differences in how the engine treats UI-related objects compared to play-related objects, is the use of themes and how to create user interfaces. Godot has quite a powerful theming mechanism, but it's not exactly the friendliest developer experience.

To get you started with UI, themes and much more we have gathered the following educational resources:

1. GDQuest's [Godot User Interface Tutorials](https://www.youtube.com/playlist?list=PLhqJJNjsQ7KGXNbfsUHJbb5-s2Tujtjt4) - Godot has some peculiarities when it comes to making UIs that could trip up even the advanced users. This YouTube series covers, in depth this topic, with plenty of examples
1. Emilio's [Making Programs with Godot](https://www.youtube.com/playlist?list=PLQsiR7DILTczMLsN8qmMym7pYfJXynzK0) - a bit of trivia: the Godot editor is built using the Godot engine itself. So there's no surprise Godot can likewise be used to create programs and tool, not just games. This series covers UI and themes in an applied manner, by developing applications instead of games

### Shaders in Godot

Sharders are probably one of the parts Godot truly shines. It offers a simplified OpenGL-like scripting language (for coders) and a visual node editor (for designers) that are ridiculously easy to use. Apart from these, it comes with simplified models for creating materials directly in the options panel - the inspector.

Godot is very flexible when it comes to VFX driven by shaders. The following resources introduce you to shaders in Godot, starting slow and ramping it up in the second entry of the list with examples to get you going in both 2D and 3D:
1. GDQuest's [Intro to Shaders in Godot: 2D and 3D Water Tutorials](https://www.youtube.com/playlist?list=PLhqJJNjsQ7KHqNMYmTwtsYTeTrqrRP_fP) - this is a good start to get your feet wet and see how easy it is to write Godot shaders. They are in essence much simpler than Unity's. It goes mostly through 2D shaders, but this list includes BAasitan's 3D examples as well
1. GDQuest's [Visual Shader Editor in Godot 3.1: Dissolve Shader](https://youtu.be/sf_Dc4ew3eM) - this tutorial goes through a practical 3D dissolve shader effect with the use of the Visual Shader Editor which was brought back in Godot 3.1
1. Gonkee's [Godot Shaders playlist](https://www.youtube.com/playlist?list=PL9NDikg3iIaXtGQY6HIgzUxfuMTkybzyx) - a playlist with fairly advanced 2D shader usage. It goes through specific examples such as: procedural fog, cartoon fire, simple water, paper burn, Mandelbrot fractal, lava as well as an overview of Visual Shader Editor in Godot 3.1 and its limitations
1. Bastiaan Olij's [Godot Grass shader tutorial](https://youtu.be/uMB3-g8v1B0) - this is an advanced 3D tutorial/overview for adding grass on terrain using shaders. It has a GitHub project that goes along with the video, which can be found in the description

### Extending Godot

One of the great aspects of Godot is that it can radically be customized to fit anyone's needs, having a very powerful editor plugin system. Editor tools can be built that run real-time during the development of the game phase, directly within the editor, extending it with new panels and functionality.

In this list we start with the official documentation, which goes through the necessary steps to building plugins of different sorts, then we have an actual real-case example:

1. [Godot editor plugins official documentation](https://docs.godotengine.org/en/3.1/tutorials/plugins/editor/index.html) - the official Godot documentation goes mostly through the conceptual and theoretical basis for extending the game engine editor. It's a good starting point for learning what this entails
1. GDQuest's [Smart Moving Platforms in Godot: waypoint system and Tool mode tutorial](https://youtu.be/ZWO2WiH9p9s) - this is an example on how to build game development tools in the Godot editor to ease the game creation workflow. As the title suggests, it is about creating a waypoint system that works in the editor which can be modified in real time and have a 2D platform follow the path. This is just a simple example that goes through all that's necessary in order to start working in tool mode in Godot

### Multiplayer in Godot

Godot offers both high-level and low-level multiplayer protocols and APIs for both simple and advanced coordination between clients and servers. RPCs (remote procedure calls) are what Godot uses in order to call and sync peers.

At the time of this writing there aren't that many educational resources on handling multiplayer systems in Godot. We hope that the following list is enough to put you on the right track:

1. GDQuest's [Intro to Multiplayer](https://www.youtube.com/playlist?list=PLhqJJNjsQ7KHohKIdqyTHRr96zYreZMC7) in Godot - this is one of the few educational resources that goes through multiplayer game creation in Godot. It's an introduction to networking via a 2D shooter example where two players can create a server and interact through it in a deathmatch
1. [Godot Networking](http://docs.godotengine.org/en/3.1/tutorials/networking/index.html) - the official documentation explains the concepts of high-level and low-level networking capabilities in Godot

### Going advanced

Bastiaan Olij has kindly created a fairly advanced tutorial series on how to make a car simulation in Godot. While the official Godot demos include a truck handling simulator which, this tutorial series is one step above in terms of quality.

- Bastiaan Olij's [Godot Vehicle Tutorial](https://www.youtube.com/playlist?list=PLe63S5Eft1KapdW0-o824gCbG8LPvzxSA) - kindly putting together this tutorial series of a vehicle simulation on a track, this is one of the best tutorials out there showing advanced usage of Godot. It goes through importing the meshes in Godot, building a track and creating a car controller

### Getting (un)stuck

While the above resources are enough to explore a significant part of Godot, it isn't an exhaustive list and there are many holes left to be filled. Here are some great places to start looking for answerers when you get stuck:

- GDQuest's [New Features in Godot 3.1](https://www.youtube.com/playlist?list=PLhqJJNjsQ7KEN1pQVRD4an4Ykd1i9t3t9) - this is a good overview of the tools provided by Godot 3.1. It might just get you unstuck if you don't know what can be done with it
- KidsCanCode [Godot recipes](http://kidscancode.org/godot_recipes/) - this site pulls together a series of recipes just like the name suggests. It goes all the way from the very basics to math, physics, AI, and more. It's a to-bookmark educational resource that will no doubt help you get unstuck on specific issues
- [Godot reddit list](https://www.reddit.com/r/godot/comments/an0iq5/godot_tutorials_list_of_video_and_written/) - we are at a point in the list where exploring further topics by yourself is something you might like to do. Keep in mind though, that this hasn't been curated, it's a list of topics to be explored with a varying amount of quality in between
- [Godot community page](https://godotengine.org/community) - it's a good idea to start interacting with the community through the official channels. This place gathers all of the official ways you can interact with other game developers and much more. Sometimes getting unstuck is about asking the right question and getting back a good answer

The following section includes links to demos on a wide range of topics. At the time of this writing there is still a wide range of quality in between these examples, but for specific problem-solving ideas it's a good resource to bookmark.

- GDQuest [Demos](https://github.com/GDquest/Godot-engine-tutorial-demos) - this GitHub repository is one of the most complete out there when it comes to Godot demo projects. Some of the demos are outdated, being built for Godot 2, but there are plenty of recent examples to get you unstuck on specific topics
- Official [Godot Demos](https://github.com/godotengine/godot-demo-projects) - the main GitHub Godot repository with a lot of demos featuring most of the topics you might be interested in: 2D, 3D, shaders, networking, UI, etc. examples. The GDQuest team is working actively at improving the source code quality of the official demos

## Where to from here?

For further game development topics, that aren't specific to Godot, but nonetheless are a valuable educational resource we have gathered the following curated list.

Generic game development resources:

- [The Book of Shaders](https://thebookofshaders.com/) - one of our top picks because it's a fun visually engaging resource. It explores, in an easy to follow way, the idea behind fragment shaders and what can be done with them. _At the point of this writing this book is incomplete_
- [Game Programming Patterns](http://gameprogrammingpatterns.com/) - this online free book is a must resource for understanding different OOP patterns used specifically in game development
- Amit Patel's [Red Blob Games](https://www.redblobgames.com/) blog - is an online resource that explores topics in great detail with lots of interactive examples. It is one of the best resources out there
- [The Nature of Code](https://natureofcode.com/) - this online free book is about understanding how the mathematical principles behind our physical world can help us create compelling digital worlds. It is an interactive book exploring a wide variety of topics
- [Game AI Pro](http://www.gameaipro.com/) - free online book series that gathers together multiple recipes in AI/behavior topics. These are very advanced overviews that don't often provide complete code, but rather explore high-level ideas leaving the developer do the hard work of implementing them
- [Procedural Content Generation in Games](http://pcgbook.com/) - is an online free book exploring high-level concepts on creating content using procedural generation algorithms. It doesn't go into code so, like the book above, it leaves the heavy lifting to game developers that want to explore advanced ideas
- [GPU Gems](https://developer.nvidia.com/gpugems/GPUGems/) - free online book series by NVidia that goes through very advanced GPU topics. Some of these ideas are low-level to the point that they could very well be implemented at the game engine development stage

(Non)Conferences useful for gathering further game development ideas:

- [NotGDC](http://www.notgdc.fun/) - "a game development non-conference, for everyone". Game developers without the possibility of going to the highly-sought-after Game Developers Conference now have a place to interact with one another through [NotGDC](http://www.notgdc.fun/). Just like [GDC](https://gdcvault.com/free), [NotGDC](http://www.notgdc.fun/) explores a wide variety of topics and inspirational talks and methodologies for game development
- [GDC Vault](https://gdcvault.com/free) - the [Game Developers Conference Vault](https://gdcvault.com/free) gatheres an in-depth design, technical and inspirational talks and slides from the game development industry. It's a must resource for exploring further topics in the game creation process

Non-gamedev related:

- [Paul's Online Math Notes](http://tutorial.math.lamar.edu/) - is one of the best resources for exploring math topics going from plain and simple algebra & calculus to advanced topics such as vector calculus and differential equations. This is a good place to start learning advanced mathematics with applications in physics and game development especially for those of you who want to get into creating physics models
- [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds/index.html) - Godot's programing language is heavily inspired by [Python](https://www.python.org/) and so **we recommend you explore** core programming algorithms and data structures using it

The [previous part]({{< ref "open-source/guides/learn-godot/beginner/index.md" >}}) in this series [Learn to Make Games with Godot: Beginner Edition]({{< ref "open-source/guides/learn-godot/beginner/index.md" >}}) is exploring basic resources for the enthusiasts out there that want to make a transition to Godot and understand how to use this game engine, starting from the very beginning.

