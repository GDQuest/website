+++
title = "Writing guidelines"
description = "This page contains our writing guidelines for tutorials and, in general, accessible writing."
author = "nathan"

date = 2019-12-14T21:49:21+01:00
weight = 5
+++

This page explains our writing style and the guidelines we follow to write clearly.

Our style aims at being accessible, clear, and informative, with a touch of personality. It supports our mission and goals:

1. **Bringing people together**. Making them feel welcome and fostering collaboration.
1. **Sharing openly**. We share our knowledge and tools, giving back to the community.

## Our Tone

The tone of an article helps to keep readers interested and engaged. It also shows our personality.

Our tone is **kind**, **genuine**, **clear**, **accessible**, **inclusive**, and **professional**.

To achieve that, avoid exaggerations, unnecessary jargon, but also colloquial expressions.

Write as if you were addressing a fellow professional or an adult student directly in a one-on-one setting. Aim for a welcoming feel without being overly close.

Address the reader directly with "you." When talking about yourself or the team, you can use "I" or "we." When talking about third parties, favor pronouns like "they" or "them."

Also, while we should keep the style of documents like these consistent and formal, you're encouraged to show your personality in news posts and devlogs.

## The writing workflow

Here is the tutorial writing workflow we should always follow. In short:

1. Prepare the final code for the tutorial.
2. Code review.
3. Write an outline for each lesson or tutorial series.
   - Show the result and list what the person will learn at the start.
   - Use sub-headings to structure your content.
   - Focus on the general techniques, principles, problems to solve, or reasons for a given code structure. Skim over the steps or implementation details.
   - Write the start of paragraphs, paste code snippets, or use pictures over bullet-lists. That is to say, content from which you can directly build your tutorial.
4. Outline review.
5. Write the tutorial, building from the outline.

Working with an editor is essential to get the perspective of someone who hasn't researched the subject matter as much as you did. Also, we cannot pick up all the mistakes we do alone.

### Focus on what matters most

Explain where you are going or why you design your code or nodes in a certain way in the introduction, before giving step-by-step instructions. This background is a vital part of the tutorial to me.

Depending on the topic, focus on:

- The problems to solve.
- The challenges involved.
- Breaking down an effect or reference visually (game art, game design).
- The design principles that apply to the task at hand.
- How other persons may have solved that problem.

Explaining underlying causes or concepts helps the reader to follow along and to stress the most important aspects to learn: problem-solving, transferable knowledge and techniques.

Then, you can break down the steps to reach the tutorial's goal. You can also add general explanations or background to the rest of the tutorial.

## Dos and don'ts

Below, you will find specific guidelines that help to communicate ideas clearly to a broad audience, including non-native English speakers.

For technical writing, that is to say, manuals and code references, we also follow the [Godot technical writing guidelines](//docs.godotengine.org/en/latest/community/contributing/docs_writing_guidelines.html).

To start with, use American English. It is the standard in technical writing and for many free software projects.

### Write for the least experienced reader

Write with learners in your audience who understand the topic the least in mind. Doing so makes your articles more accessible, it shows your mastery, and it saves the readers' time.

Here are some tips to achieve that goal:

1. Avoid technical jargon and complicated concepts.
1. Use fundamental concepts to break down complex or abstract ideas.
1. Use plain language rather than uncommon words.
1. Be as clear and as precise as you can.

For reference, check out the US government's [list of simple word alternatives](//plainlanguage.gov/guidelines/words/use-simple-words-phrases/).

### Use the direct voice

Using the direct voice leads to shorter sentences compared to the passive voice. It makes the action clear from the first few words.

Avoid the passive voice:

> The update_items function is used by the inventory system.

Favor the direct voice:

> The inventory system uses the update_items function.

### Keep sentences short

**Keep sentences under 25 words**. Favor short sentences, that each communicates one idea.

Use paragraphs to group sentences related to a broader idea together. Whenever you change the topic or move on to another concept, add a new paragraph.

### Break up paragraphs

Long paragraphs, like long sentences, make the text harder to follow. Give the reader a breathing room and structure your articles in a way that supports your story.

Use headings, lists, and short paragraphs to structure your writings.

### Ensure pronouns have a clear antecedent

Do not start a sentence with pronouns like "this" or "that" alone. Too often, these pronouns are ambiguous.

Avoid ambiguous pronouns:

> Update the `velocity` and call `move_and_slide()`. This makes the character move.

In the sentence above, "This" could refer to updating the velocity, calling `move_and_slide()`, or both.

Instead, specify what the pronoun refers to:

> Update the `velocity` and call `move_and_slide()`. This function makes the character move.

## Technical writing and tutorials

The following guidelines are more specific to writing code documentation and tutorials. We share some conventions between the two for consistency.

### Avoid using the future tense

In technical writing, we almost always use the present tense. Depending on the case, you can replace "will" with the present tense, "let's," or "be + going to."

Lastly, in cases where you cannot avoid the future tense, consider using "should" instead of "will" to suggest that something is likely to happen, rather than certain.

### Spell out numbers, except in code

Write numbers in words when counting objects, except if the numbers in question refer to a value in the code.

For example:

> Create two `Control` nodes as siblings. Resize the first node to take two-thirds of the viewport's width.

Here is an example with code:

> Set the `max_health` to `5`.

### Use italics to refer to keywords in the interface

Write keywords or expressions as they appear in the interface or for the user in italics. Doing so differentiates the words from inline code.

For example, Godot capitalizes property names and settings by default. For example:

> In the _Initial Velocity_ category, change the _Velocity_'s `x` to `-100`.

### Use plain English over symbols

Avoid replacing words like "and" with "&," or using the slash "/" instead of "or."

## Structure

This section focuses on the structure of tutorials, articles, and <abbr title="HyperText Markup Language">HTML</abbr> elements.

### Headings

Use Title Case for document titles: "Getting Started with Godot." For other headings, only capitalize the first word: "Coding the character."

Always write a paragraph after a heading, including an introduction following a page's title.

On the web, only the document's title should use an H1 heading. Use H2 for sections, and H3 for sub-sections. Avoid nesting sub-sections past the H4 level.

### Create meaningful links

For links, write a label that describes the action the user is taking, or the page they are going to arrive on. For example, instead of [official Twitter account](//twitter.com/NathanGDQuest), use [follow GDQuest on Twitter](https://twitter.com/NathanGDQuest).

Some more tips:

- Explain where the links lead and why through their label.
- Links should help the user scan the page for essential information and related resources.

## Resources

Our guidelines are inspired by:

1. The [Harvard writing guide](https://library.harvard.edu/writing-guide).
1. The US government's [plain language guidelines](https://plainlanguage.gov/guidelines/).
1. Write the Docs's [style guides section](https://www.writethedocs.org/guide/writing/style-guides/) for technical writers.
