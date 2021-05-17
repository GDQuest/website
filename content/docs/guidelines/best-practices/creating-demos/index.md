+++
title = "Coding Godot demos for tutorials"
description = ""
author = "nathan"

date = 2021-04-17
weight = 4
+++

This guide details the process to create a code demo for a game development tutorial.

You will learn:

1. Our guidelines to write good educational code.
1. How to scope your projects.
1. Our recommended workflow to produce demos efficiently.
1. Why you should get teammates to review your code early.
1. How to style your GDScript code.

## Our guidelines to write good educational code

There are some guidelines we follow to code for educational purposes at GDQuest.

This is the spirit we want to teach:

1. **Good code is the simplest solution for the problem at hand**.
   - Keep your code as simple as possible in the context of your project.
   - Avoid future-proofing and making your code "flexible." That is unless you are specifically teaching this aspect.
   - There might be multiple valid solutions; just pick one.
   - Favor inlining code in functions over splitting it over many functions and files to avoid creating needless indirection.
1. **Your decisions should always be reality-based**.
   - Don't follow principles, even popular ones, when they don't give you any concrete benefits.
   - Don't cling to paradigms and ideas you've read in books if they don't have concrete benefits.
1. **Think about what every line of code you write teaches**.
   - You should be able to justify every line of code you wrote and why you chose it over an alternative. The students will ask.

## How to scope your projects

It's easy to underestimate the work involved when writing a good tutorial, one that goes the extra mile and anticipates the reader's questions.

Also, depending on the [target audience]({{< ref "/docs/guidelines/best-practices/tutorial-audiences/index.md" >}}), the size and complexity of the code changes dramatically.

Scoping your project right is essential to make the final tutorial digestible by the target audience and to be able to finish it in time.

It takes much more time to write tutorials than to code the demo in the first place.

A demo that takes you 20 to 30 hours of programming work might take 70 or more hours of writing, testing, and review.

## Our recommended workflow to produce demos efficiently

Before you start coding, ask all the questions you need to ensure everyone agrees with the project's direction and scope.

First, you want to prototype your project. Using basic geometric shapes, create the minimum amount of code to convey the intended mechanic and feel. Then, submit it for review by creating a pull request.

For projects that take two days of work or less, you can push on to completion after a positive review of the prototype. There again, submit your code for a final code review.

For projects that take more than two days of work (12-16 hours coding), you should agree on milestones beforehand with the reviewer. Use a pull request to submit your code for review at each milestone.

### Use geometric shapes for the visuals

For the visuals, stick to basic geometric shapes: rectangles, circles, triangles... your demo should work as intended with the simplest visuals possible.

Using geometric shapes forces you to get the demo's feel right, while polished assets can take your attention away and hide design problems.

A professional game artist will then take care of producing the final assets for your demo.

## Why you should get teammates to review your code early

Working with your teammates is key to making high-quality tutorials. Alone, you can only anticipate so many student questions.

When doing reviews, teammates will raise new questions and find improvements that you hadn't thought about.

This applies to code, planning, and writing.

Doing reviews and often early ensures there weren't any miscommunications or misunderstandings regarding the project's vision.

This prevents spending a lot of time on a project only to throw it away in the end.

**Frequent reviews save everyone time and improve the tutorials' quality down the line.**

## How to style your GDScript code

There are many styling and syntax rules we follow when it comes to GDScript code. They are based on the official GDScript style guide, to which we added extra rules for educational purposes.

You can find them in this dedicated guide: [GDQuest GDScript code style guide]({{< ref "/docs/guidelines/best-practices/godot-gdscript/" >}}).

### Use a code formatter

Before pushing your code for review, you should run the [GDScript code formatter](https://github.com/Scony/godot-gdscript-toolkit) on your project.
