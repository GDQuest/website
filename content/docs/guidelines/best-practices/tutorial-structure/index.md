+++
title = "Tutorial structure guidelines"
description = ""
author = "nathan"

date = 2021-04-09
weight = 3
+++

This guide covers our guidelines to structure tutorials well and make them as enjoyable as possible for users.
<!--- In the intro or conclusion of the current tutorial we can add a note saying: "While the same general structure can apply to every tutorial, the pace and amount of details in the guide's body will differ greatly depending on the target audience." and link to the guide dedicated to writing for different target audiences.--->

In this guide, you'll learn:

- How to structure a tutorial's header, body, and footer.
- How to include code in the main sections.
- How to keep a natural flow.

We'll first look at the structure of a good tutorial and then discuss writing tutorials for different users.

This guide doesn't cover grammar and formatting. You can find those in our [writing guidelines]({{< ref "docs/guidelines/best-practices/writing/index.md" >}}).

## Header

**The header is an introduction that sells the reader on the tutorial or lesson.**

In a condensed form, it gives them everything they need to understand what the tutorial is about. They should be able to identify at a glance if this is the material they're looking for.

The reader needs to know what they're getting in return for reading to the end. For that, you need to **help the reader visualize the result and stay motivated**.


To do so:

1. Use a _descriptive title_ with words the audience would use and search for.
2. _Explain the problem or topic_ covered in the tutorial using one or two sentences. Use this intro to develop and provide context for the tutorial's title.
3. _Show the result_. Use a screenshot or a short video clip if possible.
4. _List the things they'll learn_ in logical order.
5. _Mention or list the prerequisites_ to following the tutorial keeping the user's level in mind. Whenever possible, link to an existing series or guide that covers these prerequisites.
6. Explain _how you'll tackle the problem at hand_ and why in a sentence or a short paragraph.

In a series, you should do the above both in the project's introduction and in every lesson:

- In the project's introduction, pitch the whole project.
- In each subsequent lesson, pitch the lesson at hand.

## Tutorial body

You should split the rest of your tutorial into logical sections following the outline you gave in the introduction. <!--- This still needs a reference to the guide covering the outline --->

Avoid headings that sound like labels (_eg_: "PathFinder class"). Instead, phrase each section's heading to explain the problem you're going to solve in the section (_eg_: "Coding a class to find the optimal path between two point").

Inside each section, detail the steps to achieve the result.

### Favor appending code

- When the tutorial requires editing existing code, favor appending code at the end of existing functions; Avoid adding code at the start or in the middle of a function. It makes it harder for the user to track changes.

- If there is no elegant way around adding or substituting code in the middle of a function, find a way to highlight the change to make it easily identifiable for the user. <!--- Do we want to set a method here? for example: git's +/- in front of added/removed lines? --->

### Include code comments

Code listings should include comments that explain:

- Why you decided to write a given function or part of the function this way.

    - What are the advantages of this approach? The drawbacks of alternatives?
    - Does it prepare the terrain for upcoming lessons?

- What the code does without paraphrasing it.

    - How does the implementation affect performance?
    - How does a function works under the hood or what does it do?
    - What edge cases are you accounting for?

You can alternatively write those explanations before a short code listing.

### Craft the flow of the tutorial

**A good tutorial should use the flow that feels most natural to the reader.**

It's a balancing act that involves:

- Avoiding frequent back-and-forth between files.
- Avoiding a robotic structure. In other words:

  1. Avoid creating the whole scene structure with all nodes first.
  2. Avoid creating a bunch of empty scripts and then filling them sequentially from top to bottom.

The robotic structure is most convenient for the writer, but feels like copying mindlessly for the reader, even if you do your best to explain everything.

**The most natural flow for readers is adding game mechanics and features one after the other.**

You want to limit frequent context switches yet teach mechanics one at a time. Your role as a tutor is to arrange the order in which you cover everything to minimize friction.

Ideally, at the end of each section, the reader should be able to run their game or edited scene without errors even if not much is happening at this point.

Similarly, at the end of every lesson in a series, the game should be in a testable and working state.

## Footer

At the end of a tutorial, give the reader a summary of what they achieved and learned. Give them insights into how they can go further, and if possible, give them a related lesson they can check out next. <!-- Note: We just told them to write a footer but then didn't do it in this guide.-->

