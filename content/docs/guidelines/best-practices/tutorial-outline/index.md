+++
title = "Writing tutorial outlines"
description = "This document is an example of writing tutorial outlines that capture the essential points of a tutorial and help get productive peer reviews early on."
author = "nathan"

date = 2020-03-20T18:16:27-06:00
weight = 5
aliases = ["docs/guidelines/best-practices/tutorial-outline"]
+++

This guide will help you write useful tutorial outlines, the first step to write a great article or tutorial.

You'll learn:

- What's an outline.
- Why you should always write outlines for your tutorials.
- How to write an outline.

Then, you'll get an example of a complete tutorial outline.

## What's an outline

An article or tutorial outline is a rough plan that conveys the document's main points and structure.

It's a preliminary step professional writers and teachers use to iterate on a lesson or a course's content quickly.

We use them for individual lessons, videos, but also to plan series and entire projects.

Professionals follow a process similar to outlining in many fields:

- Programmers and designers prototype software and games.
- 3D artists first block in 3D models and animations.
- Entrepreneurs plan projects before executing them.

Every time, they save countless hours of work doing so. Writing is no different.

## Why you should always write outlines

**Outlines are short and condensed writeups**.

They allow you to put your thoughts on paper and organize them in a short amount of time, before spending hours, if not days developing the content.

At the outline stage, you can focus entirely on your lessons' structure and main teaching points. You can get a review and reorder, add, or delete parts in a matter of seconds.

There are _immense benefits_ to outlining:

- You'll get reviews and constructive feedback as early as possible in the writing process.
- You'll focus on the tutorial's structure and main points and nail them before investing hours into writing.
- It makes the writing process straightforward. After review, you only have to fill your outline from top to bottom.

Reviewing and reordering a complete 2000-word tutorial can take hours of work.

In contrast, at the outline stage, it takes _at most_ several minutes.

Thanks to all the above, you'll save a lot of time both to yourself and the person reviewing and editing your work.

**My mind doesn't work like that. I feel more comfortable writing straight away?**

If outlining feels difficult at first, that's completely normal.

It's a skill; you need to practice creating outlines for the process to become natural.

Getting straight to writing leads to poor tutorials. You end up introducing topics and new techniques in a sub-par order. Students struggle to follow your logic.

## How to write an outline

To write a good outline:

1. If your tutorial revolves around any code or project, create and get review on it first.
1. Write down a bullet list capturing **key information** about your tutorial.
1. Write [the tutorial's header]({{< ref "/docs/guidelines/best-practices/tutorial-structure/index.md" >}}#header).
1. Write descriptive headings and sub-headings. They represent the tutorial's flow.
1. Fill each section (heading) with short notes and code snippets.

### Coding the project and getting a review

Before writing a tutorial outline, you should create the project and get a thorough code review if it involves code.

The outline depends entirely on your code.

To code the project and get review on it, check out the following guide: [Coding a Godot demo]({{< ref "/docs/guidelines/best-practices/creating-demos/index.md" >}}).

### Key information

You should first write down key information about your tutorial and have it at the top of your outline:

- **Title**: your tutorial's final title. It should be descriptive and answer a problem or a need from the users.
- **Pitch**: a description of the whole tutorial and its value proposition in one to two short sentences.
- **Audience**: one of our [target audiences]({{< ref "/docs/guidelines/best-practices/tutorial-audiences/index.md" >}}), the intended group of readers for your tutorial.
- **Teaching points**: a bullet list of the key teaching points and new techniques covered in the tutorial.

This information forces you to be clear about what you're writing about. It also gives teammates the necessary context to review your work.

### Writing the tutorial's header

Next, you want to turn your key information into a concrete list of things the user will learn in the tutorial, prerequisites, and your tutorial's introduction.

You can learn more in our [tutorial structure guide]({{< ref "/docs/guidelines/best-practices/tutorial-structure/index.md" >}}).

### Write descriptive headings

Headings structure a document. They split it into subsections, each with a _specific teaching goal_.

**Every subheading should correspond to solving a given problem, implementing a new mechanic, or answering a broad question.**

Also, you want to write the headings to be as descriptive and appealing as possible: 

- Avoid using new class names and technical titles.
- Avoid one or two-word headings.
- Try to capture the problem you'll solve or game mechanic you'll add in the heading.

For example, do not write "Player script." Instead, write "Coding the player's movement."

Another example: do not write "Area2D node." Instead, write "Detecting hits using the Area2D node."

### Add notes and code snippets

After writing the headings, once you are satisfied with the order, add a few lines and code snippets to start to sketch the content of each.

You want to focus on key teaching points and the order in which you'll teach.

Write down questions the readers might have and try to do some troubleshooting. You should work with a peer at this stage to ensure you do not forget anything.

## Outline example: Drawing strokes around 2D sprites

- **Title**: Drawing outlines around 2D sprites.
- **Pitch** (or short description): Learn to create an outline shader for 2D sprites, with three variations. Inner, Outer, and both way strokes.
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

Boil down the high-level steps to 1 or 2 paragraphs.

### Coding the stroke shader

Create a material and a canvas item shader.
Add two uniforms, `line_color` and `line_thickness`
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
