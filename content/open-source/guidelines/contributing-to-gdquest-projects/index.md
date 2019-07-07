---
title: Contributing to GDquest's projects
description: Do you want to become a Free Software contributor? This guide is here to help you learn everything you need!
author: nathan

date: 2018-11-05T09:30:19+09:00
aliases:
  - /open-source/contributing-guidelines
---

If you want to **become a Free Software contributor** to and be part of our projects, this is the place to get started! 

This guide will tell you everything you need to know to get your improvements integrated into the projects as fast as possible.

We use these guidelines at GDquest as well to **work efficiently together**.

To make it as smooth and as pleasant as possible for everyone to work together, we'll ask you to:

1. **Communicate**. Let people know what you're working on, join discussion on the issues, and open your own!
1. **Be and mindful of the contributors' and the maintainers' time**. Everyone here is providing their expertise benevolently. As much as we are thankful for detailed suggestions and reports, we may not be able to get to every one of them in a timely fashion.
1. **Be respectful**. We consider that respect is essential for fullfilling and productive human relationships. We want to keep our projects welcoming for everyone.

Also be sure to check our [Communication Guidelines]({{< ref "/open-source/guidelines/kind-communication-guidelines/index.md" >}})!

## In short ##

We ask everyone to follow 3 steps to work smoothly and productively together:

1.  **Communicate beforehand**
    -   Open an issue on GitHub before you code a new feature or make a big change.
    -   Reply to issues you'd like to tackle. Ask any info you need to make it work with the project's design and scope.
2.  **Follow the code style guide**
    -   We designed it to keep the code clean, easy to read, and consistent
3.  **Create neat Pull Requests**
    -   Writing a clear title and grouping relevant changes together takes no extra time, but it saves everyone else quite a lot!

/Every one of us is responsible for making work smooth for everyone else. Let's keep in touch with one another, be kind to one another, write great code, keep the project's scope and design targets in mind, and create clean pull request./

## How to communicate well ##

The community is friendly and we intend to keep it this way. We use our
own version of the Free Software Kind Communication Guidelines to be
great to one another.

Review work can be time-consuming and of 10 it takes me more time to
review someone's contribution then it would take me to codes the
feature myself. This is why I need you to follow these guidelines.

Explain the problem that you are trying to solve and the way you intend
to solve it. We likely have some code in place already and ideas to save
you a lot of work.

You can also join our Discord server to get in touch directly on the
chat.

We are here to help if you have any trouble with the git workflow or if
you get stuck along the way.

If you want to work on an existing issue make sure that you understand
it well by asking for all the information you need to tackle it.

## Code style ##

This is important that we follow a few rules so our code stays readable,
accessible to other contributors, and consistent. That is because there
are many ways to structure your code and many ways to solve a given
problem. Fe favor the ones that are maintainable but also accessible to
other developers.

Read other classes in the project to see our coding style. We write
docstrings in our code to help you understand the purpose of different
files and the code structure.

## How to create great Pull Requests ##

### Create meaningful commits

**Squash your commits**!

when you are working locally, you may use as many comments as you want
so that you can jump back in your code's history. but once you publish
your own changes and you submit your pull request, you should squash
your commits so that the project's history stays easy to browse.

A new feature can be a single commit. A bug fix or an improvement can be
one commit. A commit can range from a small change to hundreds of lines
of code. it should just be a coherent unit in the project's history.

## How to write great bug reports and requests

When you report a bug or request a new feature or an improvement, we need information to fix it.


### Writing a great bug report

Finding and fixing bugs can be time-consuming. if you help us spot it and reproduce it faster than we could on our own, we can in turn respond and solve it quickly:

1. Provide a **list of actionable steps** to reproduce the bug
1. Mention the version of the project, of the program, e.g. Godot 3.1, and the operating system you are working with
1. If the program prints an **error in the console**, copy it as text or take a screenshot
1. Tell us what result you expect to get instead

On GitHub, you can surround code or error messages with triple backticks: \`\`\` to create a code block:

```
Three backticks surround this line of text
```

Here is an example of a great bug report: 

{{% note example %}}
Title: Trimming video gives an error error if time cursor doesn't overlap any sequence

**Program version**:

- Power Sequencer 1.3
- Blender 2.80 RC1

**Steps to reproduce**:

1. Place the time cursor so that it doesn't overlap any sequence
2. Press T to use the trim feature

**Expected result**: 

No error

**Traceback**:

```
File "/home/gdquest/.config/blender/2.80/scripts/addons/power-sequencer/operators/trim_left_or_right_handles.py", line 63, in execute
ripple_start_frame = min(sequences, key=attrgetter('frame_final_start')).frame_final_start
ValueError: min() arg is an empty sequence
```
{{% / note %}}

1. **The title describes the problem clearly**
1. The body includes **all the steps to reproduce the error**
1. There is a traceback to help track down the bug faster
1. (optional) The issue includes a minimal example project to quickly reproduce the error
    - If there are multiple steps to produce the bug, or it happens with a particular setup, a demo is more than welcome! It will allow us to fix the bug faster.
1. (optional) Include a screenshot or a short video recording
    - Very useful if the issue is visual in nature, if it doesn't produce a crash, or an error message

{{% note %}}
A traceback or backtrace is a tool for developers to spot bugs. You will see it as a text message that starts with `Traceback`, followed by a list of lines that may include computer code, and an error message.


```bash
Traceback (most recent call last):
  File "/home/gdquest/Repositories/build_linux/bin/2.80/scripts/startup/bl_operators/sequencer.py", line 230, in execute
    fade_animation_clear(context, fade_fcurve, fades)
  File "/home/gdquest/Repositories/build_linux/bin/2.80/scripts/startup/bl_operators/sequencer.py", line 295, in fade_animation_clear
    if fade.start.x < keyframe.co[0] < fade.end.x:
ReferenceError: StructRNA of type Keyframe has been removed
```

This traceback is important as it gives us a precise starting point to investigate and fix the bug.
{{% / note %}}

<!-- TODO -->
<!-- ### How to write a great feature request -->

<!-- When you make a request for improvements on your features, please always describe the problem that you are facing and your needs. to produce a great design, we need to understand your problem and to explore different solutions: -->

<!-- 1. We need to understand the problem to figure out the details of the design and how to best structure our code -->
<!-- 1. To produce a coherent and efficient design for a game or a tool, you don't want to just copy what other programs do. -->
<!-- 2. The solution you envision may be too time consuming or too hard to do. We might have a simpler solution -->

<!-- Here is an example of a great feature request: -->

<!-- 1. The title sums up the request well -->
<!-- 1. The body describes the problem or the need the request intends to solve -->
<!-- 1. It provides examples of when the feature Improvement is useful,  and optionally examples of the feature in the context of other applications  -->

### Taking screenshots

If you are on Windows, I highly recommend [ShareX](https://getsharex.com/), an amazing open source program. It lets you take annotated screenshots, animated GIFs, and video clips. On Linux, you can use the built-in tool in your distribution: screenshot on Ubuntu, Spectacle on KDE...

