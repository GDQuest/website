+++
title = "Tutorial outline example"
description = "This document is an example of writing tutorial outlines that capture the essential points of a tutorial and help get productive peer reviews early on."
author = "nathan"

date = 2020-03-20T18:16:27-06:00
weight = 5
+++

This document is a guide and example to help you write useful tutorial outlines. Your outline should capture the essential points of a tutorial and help get productive peer reviews early on.

The example below drafts a skeleton for a written tutorial. For videos, you can use nested bullet lists instead of headings and use common abbreviations and other shorthands.

In my experience, writing outlines first facilitates collaboration, and it can save hours of work.

It also allows you to:

- Design a sensible skeleton for your tutorial in a short amount of time.
- Get reviews and constructive feedback early on in the writing process. 
- Structure and reorder your ideas without wasting time.
- Increase the clarity and quality of your tutorials.

Getting straight to writing instead can lead to messy lessons that introduce topics and new techniques in a sub-optimal order.

## Key information

I recommend starting with a summary of your topic, target audience, and goals. Flesh it out or rework it as you prepare code examples or experiment with the subject matter.

- **Title**: Drawing outlines around 2D sprites 
- **Pitch** (or short description): Learn to create an outline shader for 2D sprites, with three variations. Inner, Outer, and both way strokes.
- **Audience** (optional, for standalone videos or tutorials): intermediate-level, developers who might have professional experience, but no knowledge of shader programming.
- **Techniques**:
    - Sampling textures at an offset. `texture(TEXTURE, UV + vec2(x_offset, y_offset))`
    - Computing and combining masks.
    - Using `smoothstep` to soften value transitions.

_These "techniques" here are the most essential or the new techniques introduced by the tutorial. They are vital points you want to nail and share with the student. This is useful to know when giving reviews, as they are areas you want to make as clear as possible. While you can go over the techniques explained previously faster._

## Notes

The more detailed outline, like the example below, should always and only come after code reviews. This is because the tutorial's content depends on the finished project. If the code needs to change after you wrote the tutorial, updating the content will waste a lot of your time that you could spend working on other projects instead.

For the outline, I directly create my document's skeleton. The headings will be the same as in the final article. I also iterate over documents when writing, starting by writing the skeleton for sub-sections and main paragraphs.

You can put code, screenshots, and anything other than text in your outlines, when relevant, if it communicates the idea well. You can leave notes about pictures to add, for example, `PICTURE: show the layers in the effect side-by-side` or `PICTURE: code graph that shows how the three classes communicate via signals`.

Below, you will find the outline for a tutorial about creating a 2D stroke shader.

## Drawing outlines around 2D sprites

Examples of gameplay situations where this shader can be useful, like outlining collectibles or interactive objects on hover.

VIDEO: animated example of showing the outlines on mouse hover.

You will learn to:

- Create shaders to add dynamic strokes around and inside a sprite.
- Sample textures at an offset. `texture(TEXTURE, UV + vec2(x_offset, y_offset))`
- Compute and combine masks.
- Use `smoothstep` to soften value transitions.

### In short

Boil down the high-level steps to 1 or 2 paragraphs.

### Coding the outline shader

Create a material and a canvas item shader.
Add two uniforms, `line_color` and `line_thickness`
Calculate the size of `line_thickness` in UV space.

### Creating the outer outline

Introduce texture sampling with a UV offset.
Calculate 4 offset samples for the outline.
Sum them up and clamp the value to compute the outline mask.
Mix the sprite with the `line_color` using the outline mask.

### Refining and troubleshooting

#### Fixing clipped outlines

Use the Region section in the inspector to extend the sprite's bbox.
Use the TextureRegion editor in the bottom panel to resize the bbox interactively.
Optimization note: doing so increases the rendered area. The renderer and the shader will process every pixel, including transparent pixels. That's why, by default, the bbox fits the imported sprite and doesn't leave an extra margin.

#### Producing a smoother outline

Our shader leaves gaps when objects have sharp angles due to the lack of samples.
Add four samples offsetting diagonally.
Update the sum and outline mask calculations. Show the final code.

### Variations of the outline shader

#### Inner outline

Create the mask using a product instead of a sum.

```glsl
float product = left * right * up * down * upper_left * upper_right * bottom_left * bottom_right;
float outline_inner = 1.0 - product;
COLOR = mix(color, line_color, outline);
```

This causes visual artifacts when the `line_thickness` has a value below 1.0.
Introduce `smoothstep` that uses Hermite interpolation, that is to say, an interpolation between two values with ease in and out around the extremities of the range.
Use `smoothstep` to expand the outline mask and get rid of the unwanted aliased pixels.

```glsl
float alpha = outline * smoothstep(color.a, 0.0, 0.05);
COLOR = mix(color, line_color, alpha);
```

PICTURE: black-and-white view of the inner outline mask.

#### Inner and outer outlines

Divide the offset's size by two.
We need to change the outer outline calculation to avoid overlapping values and visual artifacts in the final mask.

```glsl
float stroke_outer = max(max(max(left, right), max(up, down)), max(max(upper_left, upper_right), max(bottom_right, bottom_left))) - color.a;
```

Add both the inner and outer mask to produce the final stroke.
Show the final code and result.
