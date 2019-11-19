---
title: Contributing to Learn to Make Games with Godot
description: Do you want to contribute to our Learn to Make Games with Godot guides? This document will get you started on that.
author: razvan

type: post

date: 2019-11-19 09:21:59+0200
aliases:
  - /open-source/contributing-learn-godot
---

If you want to contribute to our Learn to Make Games with Godot [Beginner Edtition]({{< ref "open-source/guides/learn-godot/beginner/index.md" >}}) and/or [Developer Edtition]({{< ref "open-source/guides/learn-godot/developer/index.md" >}}) documents this is the guide to get you started.

These documents are living documents specifically about learning how to create games with [Godot](https://godotengine.org/) using only **free educational resources**. We welcome all contributors, but given we want to have high quality educational resources instead of endless lists that confuse people, we require a mutual understanding on how to contribute to this project.

## Our Philosophy

It takes a great deal of care to research and select high quality grade educational resources. The internet today has empowered everyone to contribute to our collective knowledge, but there are no filters in place. Which means that even if people have good intentions the quality of their material can vary a lot from low-grade non-professional to exceptionally well made.

At GDQuest we're interested in the top of the top. This is especially important for beginners who get overwhelmed by the amount of information out there and makes finding good quality resources much more than a chore.

The idea behind these documents is to have you, the interested reader, contribute in order to keep them up to date and up to a great quality.

## Quality Assurance

Our primary concern here is quality of the educational resources. They need to be easily understood by the target people (eg. beginners or developers) which means they must:

- have good English
- present the content in a way which is digestible by the respective audience. Beginner presentations usually go through all the necessary steps in order to finish a project. Developers who are experienced already are looking for fast tips and tricks on how to tackle specific tasks or on how to learn a specific tool that they never used before. These are generally the guidelines
- if possible be appealing. This is more so needed for the beginner track as they are also looking for ways to stay motivated while learning

## Learn to Make Games with Godot: Beginner Edition

The Beginner Edition of the documents is meant for total beginners, people starting off possibly with no programming skills at all, let alone make games. This is a path to get you from zero to your first complete projects using Godot.

The first curated list in this document is *How to Get Into Game Development*. Here we present the basics of game making from a high level point of view. Just talking mostly about philosophy, pitfalls, myths and differences between game engines. Keep that in mind if you want to expand or improve this section.

The next part, *Creating Your First Game with Godot*, is a list of complete beginner-friendly tutorials that go through the process of finishing up a full project. Anything matching this criteria goes in here. Extra guides on GDScript and Godot can also go in here, needed to expand the basic knowledge used to make games with Godot.

*Become a More Independent Developer* is going beyond the initial beginner-phase tutorials. It's a list that goes into more details on what making games means in the long run and once you reach a point as an established developer. It's a glimpse into the future of a beginner game designer and developer.

*Going Further* is exploring more tools and knowledge that a developer needs under his/her belt. This section isn't necessarily Godot specific, but more technical skills related to game development in general. This is a good place to reference Python-related content for programmers that want to learn more skills as GDScript is indeed influenced by Python at its core. But don't let that fool anyone, Python is a completely different beast entirely, it is only useful as a conduit to further explore GDScript programming through a different lens.

Only very well documented and small demo projects are welcomed in this part of the guide.

## Learn to Make Games with Godot: Developer Edition

The Developer Edition is geared towards the active game maker, the developer that doesn't need his or her hand held during the process. These developers need short, directed and to-the-point resources that explore specific parts of Godot or perhaps specific techniques useful in Godot.

*From X to Godot* is a list, as the name implies, that takes the developer from another game engine, that they might have experience with, to Godot. This is the place for resources specific to differences between game engines and how to transition to Godot.

The next part, *Godot UI, Themes and Much More* is a collection of links to educational resources that explore creating game UIs, using Godot themes and even creating regular programs using Godot. The Godot engine is itself built using the modules and nodes provided by Godot and this is a perfect example of a non-game project built with Godot, which means that possibilities are limitless. Exploring non-game projects with Godot gives a good reason to learn UI and theming.

*Shaders in Godot* is very straightforward, a list of resources pointing to working on how to use the Godot shader language and the Visual Shader Editor.

*Extending Godot* is all about making addons and plugins for the Godot editor. Extending Godot with new tools that run inside the editor is one of its greatest strengths.

The list, *Multiplayer in Godot*, takes the developer thorough all the information regarding low-level and high-level networking using Godot. A guide to making multiplayer games as well as any peer-to-peer or client-server interaction.

*Going Advanced* is a list with very advanced tutorials, not necessarily beginner-friendly and not necessarily complete either.

*Getting (un)stuck* points out places where the developer can ask and interact with the Godot community in order to solve specific problems that aren't easily found online.

The last chapter, *Where to From Here?*, lists some great places online, all free resources that are meant to go beyond the interaction with Godot. Here we explore AI, GPU, coding patterns, philosophy, shaders, design, art and much more, not specific necessarily to Godot.

Well documented demo projects of all levels of complexity are welcomed in this part of the guide.

## Technical Detail

Learn to Make Games with Godot are documents part of the GDQuest website. As of this writing, the website is built using [Hugo](https://gohugo.io/), a static website generator.

In order to contribute to these particular documents you'll have to fork the [GDQuest website project](https://github.com/GDquest/GDquest-website). You can then find the respective documents in the `content/open-source/guides/learn-godot` folder, under `beginner/index.md` and `developer/index.md`.

After you made your changes which can range from updating links to reviewing the text to including new material, you're then ready to open a PR. For further details on how to be a great contributor please refer to [Contributing to GDQuest's Projects]({{< ref "open-source/guidelines/contributing-to-gdquest-projects/index.md" >}}) document. 

