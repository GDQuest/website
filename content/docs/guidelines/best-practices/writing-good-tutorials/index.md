---
author: nathan
date: "2021-01-03T00:00:00-06:00"
description: Our guidelines to writing good tutorials that serve the needs of our
  users.
title: 5 habits to write good tutorials
weight: 2
---

This guide covers the 5 essential habits of good tutorial writing:

1. Mind the structure
2. Mind the audience
3. Mind the style
4. Support and comment (visuals, examples, code)
5. Review, get feedback and edit

**In this guide you will learn:**

- How to organize your content
- How to simplify your writing and favor clarity
- How to keep your audience in mind
- How to use visuals and examples
- How to stage your workflow like a professional writer
- How to edit your work and what tools and resources can help you improve your tutorials.

**Prerequisites and Related Material:**

- [Tutorial structure guidelines]({{< ref "/docs/guidelines/best-practices/tutorial-structure/index.md" >}})
- [Tutorial outline example]({{< ref "content/docs/guidelines/best-practices/tutorial-outline/index.md" >}})
- [Our writing style guide]({{< ref "/docs/guidelines/best-practices/writing/index.md" >}})

## 1. Mind the structure

Start by explaining what the reader will get out of your guide and what the prerequisites are. Use this to remind yourself of your teaching goals: you are making a promise to the reader, and your tutorial should fulfill it.

Explain the problem or set of issues  you will address and give the user the background or context they need to follow along. It not only helps the reader see the value they can get in reading to the end; it also tells them upfront if this is the content they were looking for, saving them precious time.

Give a brief overview of how you will solve the problems and why you picked this approach over others. You can use a bullet list, pseudocode, a picture (diagram, illustration), a video clip, whichever is most straightforward for the user.

Break down the lesson into sections, each with a descriptive heading that presents a specific problem. For example, write `Snapping to the center of grid cells` instead of `The Grid`, or `Using signals to decouple objects` over `Signals`. Reorder the sections to provide the reader with the most natural or accessible learning flow.

{{< note >}}Writing good headings goes a long way towards helping you frame what you will write and stick to it. Always keep the problem at hand and your heading in mind while writing.{{< /note >}}

Finish with a short recap that emphasizes the key takeaways and provides further resources. This helps the reader get a sense of what's most important to memorize. If you are writing a series, hint at what the next part will cover. This helps them stay motivated to keep reading.

### Focus on one thing at a time

The reader is learning from you, meaning they have to take in new information. To make this easier on them, deliver information one bit at a time, repeating terms and ideas and linking them to new ones progressively.

Covering one concept at a time is a principle you should apply at different levels in your writings.

For example, within a series, each lesson should focus on a given problem, theme, or technique. You want to avoid bloating a lesson with irrelevant content. If necessary, you can split the topic into two lessons.

Similarly, inside a tutorial, each section should focus on a specific problem described by its **heading**. For example, "animating a sword swing," "understanding the different kinds of noise," or "implementing an inventory."

### Write in stages 

To write efficiently, **a professional writer works in three stages**:

1. Outlining.
2. Writing.
3. Editing. We cover it later in this document, in [5. Seek feedback and edit](#5.-seek-feedback-and-edit)

{{< note >}}Before getting started, you should have your code or demo ready for the tutorial. And, of course, you should have gotten peer-review on the final product.{{< /note >}}

The outline allows you to build a skeleton of the article. Write down the teaching goals, the problems you solve for the user, and the headings. It should be easy to spot organization issues at this stage and reorder the headings to provide the best flow possible to the user.

Then comes the writing process, where you write the content from start to finish without continually stopping to modify or tweak your sentences. The outline gives you the foundations you need to be able to write the content sequentially and productively.

## 2. Mind the audience

### Put yourself in the reader's shoes

**Start where the reader is**. Help them solve _their_ problems, write with the vocabulary _they_ have.

To do so, try to remember what it was like when _you_ were learning this concept for the first time. What was it you struggled with the most? Which terms or ideas did you not understand?

Ensure that you explain those terms and concepts to the reader or provide them with the necessary resources to learn.

### Always explain "why"

You always want your content to explain or at least hint at:

1. Why you chose a solution or an approach over another.
1. Why the problem you are trying to solve or the technique you are teaching matters to the reader.

The scope of the answer to the question "why" varies from user to user. Some users will feel like you did not answer this question if your guide does not explain well the context or the background for the problem at hand. Some will expect you to read their mind and answer questions that could arise from the guide.

To address that, once again, you need to try to understand the readers' psychology, their situation, and anticipate the questions they might have.

This comes with experience, practice, and the following principle: seeking critical feedback from your target audience.

## 3. Mind the Style

4. Favor explicit language; avoid long and indirect sentences.
5. **Repeat keywords** to reinforce the reader's understanding of new concepts.
6. Favor common words over literary terms. Always remember we write for both native and non-native speakers.
7. Use consistent formatting rules: _Italics_ when referring to labels in the user interface, `inline code` for any reference to a symbol, expression, or value, and **bold** to **emphasize** an important concept, keyword, or takeaway.

Our goal is to help students follow along and learn as much as possible from our content. We always strive to **help others**, **empathize** with them, and **lower the cognitive load** involved in learning something as complicated as game development.

To achieve this goal, **clarity**, writing plainly and explicitly, is critical.
### Repeat keywords

Repeat keywords. Avoid using synonyms for important terms, labels, and code, as it makes it harder to link elements together.

Avoid varying technical terms for style:

> Godot has a feature to send data without coupling two objects: _signals_. [...] _Send_ a _message_ to have the other node react to the change. [...] Notify the child node with `update_finished`.

Favor repeating the terms and verbs to help the user follow along:

> Godot has a feature to send data without coupling two objects: _signals_. [...] _Emit_ a _signal_ to have the other node react to the change. [...] Notify the child node by _emitting_ the `update_finished` _signal_.

## 4. Support and comment

1. Use **concrete examples** that are relevant to the problem at hand.
1. Keep images simple and as close as possible to the relevant text.

### Use many pictures

Images should illustrate or show the result of an action. 

They should be as close as possible to the relevant text or instruction and should be labeled for easy reference.  

Avoid grouping multiple instructions followed by a picture that illustrates only one of them. It confuses the reader.

## 5. Seek feedback and edit

### Seek critical feedback

Always put the content in the hands of your teammates and users.

It does not matter if you think a lesson is clear if it is not clear to your students.

If a student in the target audience does not understand something, do not blame them or assume anything about them. Do your best to understand the source of confusion and the actions you can take to clarify and improve the content.

The best way to achieve this goal is to ask them questions, especially if they did not provide enough information in their feedback or request.

In turn, when giving feedback to a teammate, play the role of a student and ask questions whenever something is unclear, is not covered, or lacks details. It's a great way to guide the writer into fleshing out their content.

### Edit your work 

Finally, you want to edit your text. Reread it from start to finish and do your best to simplify the writing and clarify the content. If you're making the tutorial, follow all the steps and ensure that they lead to the expected result.

Be diligent when you check and refine your writing. If you don't do it carefully, you'll have to return to it and end up with more work later.

You don't have to iterate over it; instead, send your work to a peer reviewer who will do a second editing pass.

### Use tools to check your writing

A prose linter like [writegood](https://github.com/btford/write-good) can help you highlight the use of the passive voice, adverbs, and other unnecessarily complicated terms. You should also use a spell checker.

Running your text through an online tool like the [Hemingway app](http://www.hemingwayapp.com/) or [Grammarly](https://grammarly.com) (if you have a premium account) gives you more insights regarding sentence length and style.

You don't need to _constantly_ check and make corrections as you type. Instead, run the tools _after_ you finish writing and use them only during the editing phase.

