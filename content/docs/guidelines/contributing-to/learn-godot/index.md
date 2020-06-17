+++
title = "Contributing to: Make Games with Godot Guides"
menuTitle = "Make Games with Godot Guides"
description = "Do you want to contribute to our Learn to Make Games with Godot guides? This document will get you started on that."
author = "razvan"
date = "2019-11-19 09:21:59+0200"
weight = 2
aliases = [
  "/open-source/contributing-learn-godot/",
  "/open-source/guidelines/contributing-to-learn-godot/"
]

+++

If you want to contribute to our _Learn to Make Games with Godot_ [Beginner Edition]({{< ref "tutorial/godot/learning-paths/beginner/index.md" >}}) or [Developer Edition]({{< ref "tutorial/godot/learning-paths/developer/index.md" >}}) documents this is the guide to get you started.

These guides are living documents about learning game creation with [Godot](//godotengine.org/) using only **free resources**.
We welcome all contributors but we want to provide curated learning paths rather than long and confusing lists of mixed tutorials.

This guide is here to explain the philosophy of the learning paths and how to make your contributions as productive as possible.

## Our Philosophy

We put a lot of care into researching and selecting high-quality educational resources.

The internet empowered everyone to contribute to our collective knowledge, whout filters. Which means that even if people have good intentions, some tutorials can teach poor practices and give learners bad habits regardless.

We want to list only quality material that helps you teach yourself game creation well. This is especially important for beginners, who are overwhelmed by the amount of information out there.

## Quality guidelines

Our main concern here is quality of the educational resources. They need to be easily understood by the target audience (eg. beginners or developers) which means they must:

1. Have good English
1. Present the content in a way that is accessible to the target audience.
   - Beginner-friendly guides usually slowly run you through all the necessary steps to finish a project.
   - Experienced developers are looking for overviews, examples, tips, and tricks to tackle specific tasks or to learn a tool they never used before.
1. Be appealing, if possible. This is more important for beginners compared to developers to help them stay motivated while learning.

## How to contribute

The **Learn to Make Games with Godot** guides are part of the GDQuest website and written in markdown. At the time of writing, the website relies on the static website generator [Hugo](//gohugo.io/).

You can contribute to these documents by editing them on GitHub.

To contribute to these particular documents you'll have to fork the [GDQuest website project](//github.com/GDQuest/GDQuest-website). You can then find the respective documents in the `content/tutorial/godot/learning-paths/` folder, under `beginner/index.md` and `developer/index.md`.

After you made your changes which can range from updating links to reviewing the text to including new material, you're then ready to open a PR. For further details on how to be a great contributor please refer to [Contributing to GDQuest's Projects]({{< ref "docs/guidelines/contributing-to/gdquest-projects/index.md" >}}) document.

## Beginner Edition

The [Beginner Edition]({{< ref "tutorial/godot/learning-paths/beginner/index.md" >}}) is meant for absolute beginners, people starting off with little to no programming experience. This is a path to get you from zero to your first complete projects using Godot.

The first section, **How to Get Into Game Development** introduces game creation with a high-level perspective. We're giving a general intro to game engines, but also the pitfalls and myths around game creation.

**Creating Your First Game with Godot** is a list of complete beginner-friendly and project-based tutorials. The goal is to get people making games fast and to help them enjoy the learning process.

**Become a More Independent Developer** is here to help students grow past step-by-step tutorials. The resources there go into more details on what making games means in the long run. Tutorials or guides in this section should help steer the learner towards a path that will help them become independent in their learning and their creative abilities.

**Going Further** presents domains and knowledge that a game developer needs to explore. This section isn't Godot-specific. It's about general game development skills. This is a good place to put Python-related content for programmers that want to learn more aboutprogramming, data structures, paradigms, etc.

## Learn to Make Games with Godot: Developer Edition

The [Developer Edition]({{< ref "tutorial/godot/learning-paths/developer/index.md" >}}) is for creators who already have programming experience, who might be coming from another engine, and who want to get up to speed with Godot. For this guide, we're mostly looking for short and focused resources that explore specific parts of the engine or that are especially useful to developers.

The first section, **From X to Godot**, includes resources that help people transition from other engines. This is the place for resources specific to differences between game engines.

The next part, **Godot UI, Themes and Much More** is a collection of links to educational resources that explore creating game UIs, using Godot themes and even creating regular programs using Godot. The Godot engine is itself built using the modules and nodes provided by Godot. This is a perfect example of a non-game project built with Godot, which means that possibilities are endless. Exploring non-game projects with Godot gives a good reason to learn UI and theming.

**Shaders in Godot** is all about working with shaders in Godot either using the GLSL-like shader language or the Visual Shader Editor. Materials can go there as well.

**Extending Godot** is all about making addons and plugins for the Godot editor. Extending Godot with new tools that run inside the editor is one of the engine's greatest strengths.

The list, **Multiplayer in Godot**, takes the developer thorough all the information regarding low-level and high-level networking using Godot. A guide to making multiplayer games as well as any peer-to-peer or client-server interaction.

**Going Advanced** is a list with very advanced tutorials, not necessarily beginner-friendly and not necessarily complete either.

**Getting (un)stuck** points out places where the developer can ask and interact with the Godot community in order to solve specific problems that aren't easily found online.

The last chapter, **Where to From Here?**, lists some great places online, all free resources that are meant to go beyond the interaction with Godot. Here we explore AI, GPU, coding patterns, philosophy, shaders, design, art and much more, not specific necessarily to Godot.

Well documented demo projects of all levels of complexity are welcomed in this part of the guide.
