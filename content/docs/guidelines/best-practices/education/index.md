+++
title = "Education in online tutorials"
description = "This living document contains some notes and insights based on my experience teaching online and face-to-face, and some principles to get ideas across in online education."
author = "nathan"

date = 2019-12-11T15:52:58+01:00
weight = 5
+++

We learn our entire lives, often without realizing it. As a result, learning and teaching can seem like mysterious processes. 

There are different ways to learn, and some can be more efficient than others to develop new skills like learning through guided experimentation as opposed to rote memorization.

As tutors, to me, our role goes beyond transmitting information. We can help people to learn faster, to get over roadblocks, and to become more independent in their learning. 

This living document contains some notes and guidelines for the educational style of our tutorials. It is based on my experience teaching online and face-to-face.

<!-- Add a summary and a list of broad principles that serve as a foundation for our teaching style. -->

## We learn when we're engaged in an activity ##

Practice is essential to learning. Putting what you learned in your own words, and applying what you're learning, as you're learning it. So is getting sufficient feedback for every step that we take learning a given discipline.

I believe that to learn as fast as we can, we need to:

- **Feel like we're part of the group we strive to be part of**. I think that's why Jesse Shell's "The Art of Game Design" starts by asking the readers to view and call themselves game designers. Just like playing as an avatar in a game, the virtual identity helps us take steps towards becoming a designer, a developer, an artist... and thinking like one of them.
- **Get feedback for our input**. This is an idea we always apply to UX and game design. Feedback, feeling like our actions are meaningful and produce a tangible result, helps us understand, memorize techniques, and stay engaged and motivated.
- **Practice, and do so at the edge of our abilities**. Learning is incomplete without practice. Theory alone is insufficient to develop skills. Critical thinking, writing, actual programming, and design work are necessary to strengthen our abilities. We also need some challenge to stay engaged. If you've ever been in a state of [flow](//www.jenovachen.com/flowingames/foundation.htm), there's nothing like it to make fast progress in a given domain.

And more.

The points above are hard to achieve with video lessons. We learn through practice, and when we're critically engaged in an activity. Our videos should push the viewers towards that. We need to go past sharing raw information and facts and help people to want to learn, to practice, and to enjoy the process.

We can do so by multiplying the opportunities for the viewer to engage in learning. **Asking the viewer questions**, by offering **exercises**, **challenges**, and by creating **community projects and events**.

<!-- TODO: write more on viewer questions and quizzes, exercises, challenges, and getting people to take part in community projects. We can take a look at FreeCodeCamp as an example. -->

## Going past step-by-step ##

Step-by-step tutorials are easy to produce, and they can ease designers who aren't comfortable with programming into the daunting process of creating software. But as soon as we try to cover the reality of development, step-by-step videos tend to dumb it down into a seemingly linear process while design and programming are both nonlinear, creative problem-solving activities.

That is because step-by-step videos are long. The majority of the content shows typing individual lines of code, which shifts the focus towards the implementation details. As we have to write a lot, we end up focusing on writing the code without typos instead of thinking hard about the big picture. Yet, I believe the big picture and general techniques is the part we should teach.

### Code overviews ###

Commenting on a finished project's structure can be useful to explain high-level abstractions and a program's flow, especially if the lesson is short and to the point. It can help experienced developers or students to expand their library of patterns and solutions that they can apply to their projects.

### A middle-ground: pasting code snippets ###

To replace code overviews, we could shift towards an approach that's half-way through step-by-step and just commenting on the final code. We can achieve that creating start Godot project with only the files required for the tutorial, extracted from a larger project. But more than the assets.

The projects would include:

- Anything that's not relevant to the tutorial but required pre-built and encapsulated. Assets, scenes, and scripts.
- Some empty API in place for the scripts that are relevant to the tutorial: properties, the methods' signature, docstrings, all that based on the guidelines, but no individual instructions.

With the API in place, you can quickly explain the class's responsibility and how the interface will help you to solve the problem at hand. It allows you to focus on code structure.

Then paste blocks of code one by one to show a way to implement the solution and flesh out the details.

The tutorials don't have to cover every single line. We can also have pre-built methods or extra objects done and hidden from the viewer. Anything that's not relevant to the tutorial, but required for the demo to work.

## We should teach techniques and concepts over recipes ##

> Give a man a fish and you feed him for a day; teach a man to fish, and you feed him for a lifetime.

Although we learn from practice and examples, as tutors, we can help the learners go one step further: learn the general, reusable technique or concept behind the examples.

We're here to teach more than a series of steps to solve a specific problem. We're here to help people learn to solve problems on their own, regardless of the situation they are facing. To help them become independent, not reliant on step-by-step guides. Our videos should help people understand that game creation isn't a linear process and that independent creators don't have strict recipes to follow.

The idea applies to game programming as well: the principles we use and the way we structure our code are more important than the exact implementation we choose.

When you create a tutorial on a given topic, try to offer more than a description of what each line of code does. You can explain the thought process that led you to structure your project in a certain way, mention other potential solutions you could try, their advantages and drawbacks. If you decide to teach a pattern, explain its general form. You can also indicate the limits of your example or the tutorial compared to a real-world scenario. Game code can get complicated and messy once you start to connect systems.

## Keep the language simple ##

To me, the ability to explain complex topics in simple terms is a sign of mastery and maturity. Mastery because it takes a great deal of experience to boil down a technique or a concept to its essence. Maturity as pride or one's ego can prevent us from making hard-learned knowledge accessible to everyone else.

The domains we teach are hard to learn. Our role as tutors is to ease the students into learning. There are terms we can't work around: a developer must learn about variables, functions, loops, classes, objects, and more.

However, there's no need for unending sentences, academic terms, or rare vocabulary in our tutorials. We should make each tutorial as accessible as we can to its target audience.

Depending on the intended audience for a given series, we can assume that the student has a certain amount of experience. The viewer should already be comfortable with all necessary programming concepts to follow a video about pathfinding in 3d, or about a programming pattern like State.

It's a balancing act. The idea isn't to dumb down lessons, but to keep the form as clean and as fluid as possible. That way, the learner can focus their attention on the content.
