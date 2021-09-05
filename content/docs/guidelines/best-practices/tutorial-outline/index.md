---
aliases:
- docs/guidelines/best-practices/tutorial-outline
author: nathan
date: "2020-03-20T18:16:27-06:00"
description: This document is an example of writing tutorial outlines that capture
  the essential points of a tutorial and help get productive peer reviews early on.
title: Writing tutorial outlines
weight: 4
---

This guide will help you write useful tutorial outlines, the first step to write a great article or tutorial.

You'll learn:

- What an outline is.
- Why you should always write outlines for your tutorials.
- How to write an outline.

You will also be able to refer to an example of a complete tutorial outline.

## What's an outline

An article or tutorial outline is a rough plan that sets the document's main points and structure.

It's a preliminary step used by professional writers and teachers to plan a lesson and quickly iterate course content.

We use outlines for single lessons and videos, but also to plan series and entire projects.

Professionals follow a process similar to outlining in many fields:

- Programmers and designers prototype software and games.
- 3D artists first block in 3D models and animations.
- Entrepreneurs plan projects before executing them.

By doing so, they save countless hours of work. Writing is no different.

## Why you should always write outlines

**An outline is the basic skeleton around which you build your write-up**. Without one, it becomes much harder to shape your content and make sure it stands.

Outlines allow you to put your thoughts on paper and organize them in a short amount of time, before spending hours, if not days, developing the content.

At the outline stage, you can focus entirely on the structure of your lesson and decide your main teaching points. You can get a review and reorder, add, or delete parts in a matter of seconds. 

Reviewing and reordering a complete 2000-word tutorial can take hours of work.

In contrast, at the outline stage, it takes _at most_ a few minutes.

In short, there are _immense benefits_ to outlining:


- You can focus on the tutorial structure and nail down the main points before investing hours in writing.
- You can get reviews and constructive feedback as early as possible in the writing process.
- You can make the writing process easier and more straightforward. After review, you only have to flesh out your outline from top to bottom.


_An outline is a small but essential early investment. It saves both your time and the time of anyone reviewing and editing your work._

**My mind doesn't work this way. I feel more comfortable writing directly?**

Outlining doesn't necessarily come naturally. You can expect it to feel difficult or alien at first.

It's a skill you hone. The more you practice it, the easier it gets. Eventually, it becomes second nature to you: an automatic first step in your writing process.  

Getting straight into writing leads to poor tutorials. You end up introducing topics and new techniques in sub-par order. As a result, your students struggle to follow your logic.

## How to write an outline

To write a good outline:

1. First, start by creating and getting review on the code or project you will be referring to. This applies whenever your tutorial revolves around a piece of code or a specific project. 
1. Make a bullet list capturing **key information** about your tutorial such as: the title, the pitch, the audience and the learning points. 
1. Write [the tutorial header]({{< ref "/docs/guidelines/best-practices/tutorial-structure/index.md" >}}#header).
1. Create logical sections that each cover a main teaching point in your tutorial. Write descriptive headings and sub-headings for each section. They represent the tutorial's flow.
1. Fill each section (heading) with short notes and code snippets.

### Coding the project and getting a review

Before writing a tutorial outline, you should create the project and get a thorough code review whenever the tutorial involves code.

The outline depends entirely on your code.

To code the project and get it reviewed, check out the following guide: [Coding a Godot demo]({{< ref "/docs/guidelines/best-practices/creating-demos/index.md" >}}).

### Listing key information

At the very top of your outline, you should first and foremost write a list of key information about the tutorial.

- **Title**: your tutorial's final title. It should be descriptive and answer a problem or a need that the users have.
- **Pitch**: a description of the whole tutorial and its value proposition in one to two short sentences.
- **Audience**: one of our [target audiences]({{< ref "/docs/guidelines/best-practices/tutorial-audiences/index.md" >}}), the intended group of readers for your tutorial.
- **Teaching points**: a bullet list of the key teaching points and new techniques covered in the tutorial.

This information forces you to be clear on what you're writing about. It also gives teammates the necessary context to review your work.

### Writing the tutorial header

Next, you want to turn your key information into:
- a concrete list of things the user will learn in the tutorial
- a list or a mention of prerequisites
- an introduction to your tutorial

You can learn more about the composition of a header in our [tutorial structure guide]({{< ref "/docs/guidelines/best-practices/tutorial-structure/index.md" >}}).

### Defining sections with descriptive headings

Headings structure a document. They split it into subsections, each with a _specific teaching goal_.

**Every subheading should correspond to solving a given problem, implementing a new mechanic, or answering a broad question.**

You want to make sure your headings are as descriptive and appealing as possible: 

- Avoid using new class names and technical titles.
- Avoid one or two-word headings.
- Try to capture the problem you will be solving or the game mechanic you will be adding in the section.

For example, do not write "Player script." Instead, write "Coding the player's movement."

Another example: do not write "Area2D node." Instead, write "Detecting hits using the Area2D node."

### Adding notes and code snippets

Once you've written the heading and you're satisfied with their order, add a few lines and code snippets to start shaping the content of each section.

You want to focus on key teaching points and the order in which you'll teach.

Write down questions the readers might have and try to do some troubleshooting. You should work with a peer at this stage to ensure you do not forget anything.

---
## Example Outline
####Let's have a look at the outline of a tutorial that teaches how to draw strokes around 2D sprites.

- **Title**: Drawing outlines around 2D sprites.
- **Pitch** (or short description): Learn to create an outline shader for 2D sprites, with three variations: Inner, Outer, and both way strokes.
- **Audience**: intermediate-level, developers who might have professional experience, but no knowledge of shader programming.
- **Techniques** (teaching points):
  - Sampling textures at an offset. `texture(TEXTURE, UV + vec2(x_offset, y_offset))`
  - Computing and combining masks.
  - Using `smoothstep` to soften value transitions.

Intro: Start with examples of gameplay situations where this shader can be useful, like outlining collectibles or interactive objects on hover.

VIDEO: animated example of showing the strokes on mouse hover.

You will learn to:

- Create shaders to add dynamic strokes around and inside a sprite.
- Sample textures at an offset. `texture(TEXTURE, UV + vec2(x_offset, y_offset))`
- Compute and combine masks.
- Use `smoothstep` to soften value transitions.

### In short

Pre-requisites:

- You're comfortable with the basics of shader programming and the `fragment()` function. If not, head to our [intro to shader programming in Godot](https://www.gdquest.com/tutorial/godot/shaders/introduction/chapter/0-intro-to-shader-programming/) series.

Boil down the high-level steps to 1 or 2 paragraphs.

### Coding the stroke shader

Create a material and a canvas item shader.
Add two uniforms, `line_color` and `line_thickness`.
Calculate the size of `line_thickness` in UV space.

### Creating the outer stroke

Introduce texture sampling with a UV offset.
Calculate 4 offset samples for the stroke.
Sum them up and clamp the value to compute the stroke mask.
Mix the sprite with the `line_color` using the stroke mask.

### Refining and troubleshooting

#### Fixing clipped strokes

Use the Region section in the inspector to extend the sprite's bbox.
Use the TextureRegion editor in the bottom panel to resize the bbox interactively.
Optimization note: doing so increases the rendered area. The renderer and the shader will process every pixel, including transparent pixels. That's why, by default, the bbox fits the imported sprite and doesn't leave an extra margin.

#### Producing a smoother stroke

Our shader leaves gaps when objects have sharp angles due to the lack of samples.
Add four samples offsetting diagonally.
Update the sum and stroke mask calculations. Show the final code.

### Variations of the stroke shader

#### Inner stroke

Create the mask using a product instead of a sum.

```glsl
float product = left * right * up * down * upper_left * upper_right * bottom_left * bottom_right;
float stroke_inner = 1.0 - product;
COLOR = mix(color, line_color, stroke);
```

This causes visual artifacts when the `line_thickness` has a value below 1.0.
Introduce `smoothstep` that uses Hermite interpolation, that is to say, an interpolation between two values with ease in and out around the extremities of the range.
Use `smoothstep` to expand the stroke mask and get rid of the unwanted aliased pixels.

```glsl
float alpha = stroke * smoothstep(color.a, 0.0, 0.05);
COLOR = mix(color, line_color, alpha);
```

PICTURE: black-and-white view of the inner stroke mask.

#### Inner and outer strokes

Divide the offset's size by two.
We need to change the outer stroke calculation to avoid overlapping values and visual artifacts in the final mask.

```glsl
float stroke_outer = max(max(max(left, right), max(up, down)), max(max(upper_left, upper_right), max(bottom_right, bottom_left))) - color.a;
```

Add both the inner and outer mask to produce the final stroke.
Show the final code and result.
