+++
title = "Tutorial structure guidelines"
description = ""
author = "nathan"

date = 2021-04-09
weight = 5
+++

This guide covers our guidelines to structure tutorials well and make them as enjoyable as possible for the users.

In this guide, you'll learn:

- How to structure a tutorial's header, body, and footer.
- How to write good code comments for a tutorial.
- The flow of your tutorial's main sections should follow.
- The differences in writing tutorials for different audiences.

We'll first look at the structure of a good tutorial and then discuss writing tutorials for different users.

This guide doesn't cover grammar and formatting. You can find those in our [writing guidelines]({{< ref "docs/guidelines/best-practices/writing/index.md" >}}).

## Header

**The introduction or header sells the reader on the tutorial or lesson.**

It gives them everything they need to understand what they're stepping into in a condensed format.

You need to **help the reader visualize the result and stay motivated**: they need to know what they'll get for reading to the end.

To do so:

1. Use a _descriptive title_ with words the audience would use and search for.
2. _Explain the problem or topic_ this tutorial covers in one or two sentences. Use this intro to develop and contextualize the tutorial's title.
3. _Show the result_. Use a screenshot or a short video clip if possible.
4. _List the things they'll learn_.
5. _Mention or list the prerequisites_ to follow the tutorial. If possible, link to an existing series or guide to learn these prerequisites.
6. Explain _how you'll tackle the problem at hand_ and why in a sentence or a short paragraph.

In a series, you should do the above both in the project's introduction and in every lesson:

- In the project's introduction, pitch the whole project.
- In each subsequent lesson, pitch the lesson at hand.

## Tutorial body

You should split the rest of your tutorial into logical sections following the outline you gave in the introduction.

Phrase each section's heading to explain the problem you're going to solve.

For example, don't write "PathFinder class." Instead, write "Coding a class to find the optimal path between 2 points."

Inside each section, you want to detail the steps to achieve the result.

### Favor appending code

When the tutorial requires editing existing code, favor appending code at the end of existing functions; avoid adding code at the start or in the middle of a function as it's hard to track for the user to track.

### Code comments

Code listings should include comments that explain:

- Why you decided to write a given function or part of the function this way.

    - What are the advantages of this approach? The drawbacks of alternatives?
    - Does it prepare the terrain for upcoming lessons?

- What the code does without paraphrasing it.

    - How the implementation affects performance
    - How a function works under the hood or what it does.
    - Edge cases you're accounting for.

You can alternatively write those explanations before a short code listing.

### Flow of a good tutorial body

**A good tutorial should use the flow that feels most natural to the reader.**

It's a balancing act that involves:

- Avoiding frequent back-and-forth between files.
- Avoiding a robotic structure:

  1. Creating the whole scene structure with all nodes first.
  2. Creating a bunch of empty scripts.
  3. Then, filling scripts from top to bottom sequentially.

The robotic structure is most convenient for the writer, but feels like copying mindlessly for the reader, even if you do your best to explain everything.

**The most natural flow for readers is adding game mechanics and features one after the other.**

You want to limit frequent context switches yet teach mechanics one at a time. Your role as a tutor is to arrange the order in which you cover everything to minimize friction.

Ideally, the reader should be able to run their game or edited scene without errors at the end of each section. And that, even if not much is happening at this point.

At the end of every lesson in a series, the game should be in a testable and working state.

## Footer

At the end of a tutorial, give the reader a summary of what they achieved and learned. Give them insights about how they can go further, and, if possible, give them a related lesson they can check out next.

## Writing tutorials for different audiences

While the same general structure can apply to every tutorial, the pace and amount of details in the guide's body will differ greatly depending on the target audience.

- _Beginners_ are not comfortable reading code on their own and struggle to understand it.

  - They haven't mastered most of what you show them, so steps that are simple for you can have a high cognitive load for them.
  - They need a lot of information regarding how things work.
  - They also want to know why you do things one way or another. They don't only want steps.

- _Intermediate-level_ users are comfortable reading and writing code on their own.

  - They can read longer code listings with fewer comments.
  - You can assume they are comfortable with the Godot editor. They know where to find the main docs and main screens.

- _Advanced_ users have written sizeable programs and have years of experience behind that.

  - They can read code directly without comment and understand programming jargon.
  - They are looking for solutions to tough and large problems, like how to architecture entire systems, or really niche ones.

There's a gradient between these users, especially between beginners and intermediate-level developers. These "beginner plus" users aren't independent in reading and writing code yet, but they don't want handholding all the way either.

### Guidelines for each audience

For beginners:

- Keep code listings short.
- Write detailed code comments.
- Include spatial indications like the side of the screen on which they'll find a given button.
- Use many pictures to help them visualize the steps.
- Use minimum jargon.
- Do your best to anticipate and answer their questions.
- Troubleshoot common mistakes and errors.

For intermediate-level users:

- You may use longer code listings.
- You can assume they know where to find the most common docks and buttons in Godot.
- You don't have to explain every function, especially if the feature in question is part of your prerequisites.

  - For example, common built-in functions like `_process()`, `_ready()`, common vector operations, and everything that someone should learn at the beginner stage.
  - You don't have to explain how beginner-level features like signals and input handling work either, at least at the basic level.

For advanced users:

- If possible, discuss the topic thoroughly with users in the target audience. Ensure you understand the problem well.
- Get in touch with experts or specialists of the problem at hand. In Godot's case, this means you may want to ask core developers for insight on how a specific part of the engine works.
- Only touch on topics you are very comfortable with.
- You may use technical jargon when it makes the content clearer.
