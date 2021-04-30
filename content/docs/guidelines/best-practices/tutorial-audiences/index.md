+++
title = "Writing for different audiences"
description = ""
author = "nathan"

date = 2021-04-09
weight = 5
+++

How to write tutorials for different audiences.

In this guide, you'll learn:

- The different audiences we write for.
- How to adapt your writing to different audiences.

## The different audiences we write for

While the same general structure can apply to every tutorial, the pace and amount of details in the guide's body will differ greatly depending on the target audience.

- _Beginners_ are not comfortable reading code on their own and struggle to understand it.

  - They haven't mastered most of what you show them, so steps that are simple for you can have a high cognitive load for them.
  - They need a lot of information regarding how things work.
  - They also want to know why you do things one way or another. They don't only want steps.

- _Intermediate-level_ users are comfortable reading and writing code on their own.

  - They can read longer code listings with fewer comments.
  - You can assume they are comfortable with the Godot editor. They know where to find the main docs and main screens.

- _Advanced_ users have written sizeable programs and have years of experience doing so.

  - They can read code directly without comment and understand programming jargon.
  - They are looking for solutions to tough and large problems, like how to architecture entire systems, or really niche ones.

There's a gradient between these levels, especially between beginners and intermediate-level developers. While "beginner plus" users aren't fully independent yet when it comes to reading and writing code, they don't want too much handholding either.

## Writing for beginners

- Keep code listings short.
- Write detailed code comments.
- Include spatial indications like the side of the screen on which they'll find a given button.
- Use many pictures to help them visualize the steps.
- Use minimum jargon.
- Do your best to anticipate and answer their questions.
- Troubleshoot common mistakes and errors.

## Writing for intermediate-level

- You may use longer code listings.
- You can assume they know where to find the most common docks and buttons in Godot.
- You don't have to explain every function, especially if the feature in question is part of your prerequisites.

  - For example, common built-in functions like `_process()`, `_ready()`, common vector operations, and everything that someone should learn at the beginner stage.
  - You don't have to explain how beginner-level features like signals and input handling work either, at least at the basic level.

## Writing for advanced users

- If possible, discuss the topic thoroughly with users in the target audience. Ensure you understand the problem well.
- Get in touch with experts or specialists of the problem at hand. In Godot's case, this means you may want to ask core developers for insight on how a specific part of the engine works.
- Only touch on topics you are very comfortable with.
- You may use technical jargon when it makes the content clearer.
