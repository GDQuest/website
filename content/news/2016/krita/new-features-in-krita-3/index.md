+++
aliases = [
  "/post/2016/krita/new-features-in-krita-3/",
  "/post/krita/new-in-krita-3/",
  "/new-in-krita-3/"
]
anchors = ["major-new-features", "smaller-features", "krita-3-review"]
author = "nathan"
category = ["Krita"]
date = "2016-05-09T17:49:09+02:00"
description = "Krita 3.0 is a major update to an already powerful application. New rendering engine, animation toolset, grid, guides, snapping... there's a long list of new tools to discover. Let's explore them together in this article!"
nav = true
keywords = ["krita review", "krita 3"]
title = "What’s New in Krita 3.0? Krita Review"
type = "post"

[[resources]]
  name = "banner"
  src = "banner.jpg"
  [resources.params]
    alt = "The Krita brushes"

+++

<span class="text-muted">Never heard of Krita? It is a free, open source digital painting program that used to be Linux-only. Since 2 years though, there's a Windows version, and the program is now being ported to Mac.</span>

Krita 3 is a major update to an already powerful application. It brings it to a whole new level. It ships with a new rendering engine, a traditional animation toolset, an overhauled layers docker, rulers, grid, guides, snapping support, and a brand-new tablet code, which supports more Wacom alternatives.

{{< youtube k51OK2PlTz4 >}}

That's not all. There's a long list of smaller, yet welcome changes. The pop-up palette looks better and the icons now scale to accommodate for more than 10 brushes. The layer picking and move tools are more flexible. There is a new gradient mapping filter for color grading, as well as an original blending mode for smooth painting with transparent pixel brushes. The keyboard shortcut editor has been redesigned and moved to Krita's preference window.

The list could go on, and on. You get it: there is a lot to talk about. That's why I wrote this overview of Krita 3. In this article, I'll introduce you to the most important new features one at a time. At the end of the post, I'll give you my thoughts on the program and the updates for 2D game artists.

**Do you want to learn all of the new features? I'm working on a free <a href="/tutorial/art/krita-tutorial-for-game-artists/">Krita tutorial series</a> that will help you to become a faster artist with Krita 3.0.**

{{< figure src="/img/page/game-art-quest/krita-tutorial-banner.jpg" alt="Krita tutorial series: Become a better Game Artist with Krita" >}}

<!-- Part 1 -->
## Krita 3's 5 Major New Features {#major-new-features}

Krita 3.0 was initially funded by a thousand of backers on Kickstarter in 2015. The campaign had 2 goals: to fund a new, faster rendering engine for digital painting and a traditional animation toolset. This major update brings those additions to the world, and more! Intriguing, right?

Let's explore all of Krita 3's new features in details.

### Instant Preview: the new rendering engine

Krita's performances used to be a major issue for professional work. Painting on large documents would be slow and painful. It's now a matter of the past, at least for the most part: thanks to the Instant Preview, the program is way more responsive.

It is both simple and powerful: Krita gives you an instant preview of your drawing operations and, at the same time, it takes care of the big calculations in the background. What you get, as the artist, is better feedback on your work. You no longer have to wait for endless seconds between large brushstrokes.

The developers completely changed how Krita handles rendering operations under the hood. Thus, the instant preview not only affects brushstrokes, like it was initially meant to. It also works with filters, with the move tool, and with animation playback right now.

[Overview of the Instant Preview beta in Krita 2.9](//www.youtube.com/watch?v=c9yiBRFQnbo)

{{< figure src="/img/post/krita/new-in-krita-3/krita-instant-preview-2.9.png" alt="Instant preview in Krita 2.9 anim edition" >}}

### Krita's animation tools

Yes, you read well. You can now animate in Krita! Version 3 comes with a solid toolset that traditional animators will love. And the development team has plans to make it even better in the future. There are 3 new dockers: animation, timeline and onion skin. They respectively allow you to change your animation's length, to manage your frames and your animation layers, and to control your onion skin, a popular effect to preview multiple frames on the canvas at the same time.

To help you get started animating, there is a new default animation workspace. When you load it, it will display the 3 dockers I just mentioned at the bottom of your interface.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-animation-workspace.jpg" caption="Krita's animation workspace" >}}

For more information on this feature, check out my [Krita animation tutorial](//www.youtube.com/watch?v=9uvju6sUNJA)

The [official Krita docs](//docs.krita.org/Animation) will provide offer you with more information if you want to learn every function the toolset provides

### The new layers docker <small>My favorite feature</small>

This is the change I love the most: layer management is now both much faster and way more flexible. The team redesigned the layers docker from the ground up. It ships with a more compact look, a ton of new functions, keyboard shortcuts... Almost everything a game artist needs to do his job in the best of conditions.

Let me outline some of the changes for you. You can now:

- Tag layers and filter them by color.

- Manipulate layers and navigate the layer stack with the keyboard.

- Group, ungroup layers, and add clipping groups.

- Edit properties on multiple layers at the same time.

Last, but not least: the former 3 display modes have been merged into a single one that gives you all of the options you need at a glance.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-new-layers-docker.jpg" caption="Krita 3's new layers docker, with layer colors" >}}

### Rulers, grid, guides and snapping

These are 3 different features that work together. The grid and rulers are both managed in the same docker, called "grid and guides". The grid tab replaces the toolbox's grid tool. Is it a more flexible version of it. The guides, however, are brand new. They are horizontal or vertical lines that you can place wherever you want on the canvas. You can then use them as a reference to lay your layers out accurately.

The guides are not too interesting in themselves. That's why snapping was also implemented. If you press shift S on your document, a drop-down menu will pop up. It lists a handful of snapping options for you to toggle on or off. Snapping works with grid and guides, but it doesn't end there. It also works with vector shapes, with the geometric tools, with the free transform tool, and more. It doesn't work in every situation just yet, but this opens up a whole new range of possibilities within Krita.

### The port to Qt 5 and KDE frameworks 5

Under the hood, Krita's code went through major changes. The developers ported the program to Qt 5 and the KDE frameworks 5. These popular code libraries power Krita's interface. They are part of the application's foundations. The port was a massive task, but it will give the team a stable ground for future updates.

All of this was made possible thanks to the community and the Kickstarter backers in particular. Speaking of which...

{{< figure src="/img/post/krita/new-in-krita-3/support-krita-2016-kickstarter.jpg" alt="Support Krita's Kickstarter campaign: Let's Make Text and Vector Art Awesome!" link="//www.kickstarter.com/projects/krita/krita-2016-lets-make-text-and-vector-art-awesome" >}}

The 2016 Kickstarter campaign is live right now, and the developers need your support. Check it out now and help Krita to become even more awesome!

<a href="//www.kickstarter.com/projects/krita/krita-2016-lets-make-text-and-vector-art-awesome
" style="font-size:150%">Krita 2016: Let's Make Text and Vector Art Awesome!</a>

## 11 smaller but welcome additions {#smaller-features}

That's it for the big additions to Krita 3. But we are not done yet. There is a lot more we need to cover. A lot of small, welcome new features that add up to turn Krita into a better application all-round.

### New tablet support code

As I told you in the introduction, the tablet code has been rewritten from scratch. Krita 2.9 would just not recognize a variety of tablets. Version 3, on the other hand, already supports more devices. Especially Wacom alternatives! In case you couldn’t use your tablet in the previous version, you should definitely give it a try again.

### Improved layer picking and move tools

You can now pick multiple layers at the same time with the R key. Just keep the Shift key down and click on the canvas to add layers to your selection. You can also drag your cursor across the document with both the R and the Shift keys down, and Krita will pick all of the layers under your cursor.

The move tool got some love as well. You can now nudge your selection around with the arrow keys. If you keep the Shift key down and press an arrow, your layer will move by 10 pixels in the direction of your choice. Without Shift, it will move in one pixel increments.

### New UI for the assistants

The assistants now have a little widget attached to them to control each and every instance separately. The little UI elements move along with the origin of the assistants to help you keep track of them more easily.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-improved-assistant-widget.jpg" caption="The improved assistant widget" >}}

### Improved keyboard shortcuts editor

The keyboard shortcut editor has moved to Krita's preferences. It sits next to the "Canvas Input Settings", where you can edit all canvas related shortcuts. It feels more natural to edit all of the program's options in that unique pop up window.

The keyboard shortcuts are now arranged in categories. Unlike before, you can create shortcut schemes to share online. Krita ships with 3 default schemes: the default one, "Photoshop compatible" and "Paint Tool SAI compatible". The canvas input settings also come with the same 3 shortcut schemes.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-the-shortcut-editor.jpg" alt="Krita 3 editing shortcuts" >}}

### Gradient mapping

You can now do quick split toning with the gradient map filter! It was not planned for this release, and it is still a work in progress. The filter doesn't take advantage of the instant preview yet. It is not available as a filter layer, and it doesn't preserve your layer's alpha channel. But I'm sure game artists will love the addition regardless!

### Greater blending mode

There is a new blending mode in the "mix" category, humbly named Greater. I've never seen something like that in another painting program, but you know what? It's great! With the pixel brush engine, overlapping transparent strokes look ugly in normal mode. They don't blend smoothly, but that's how normal blending works.

The greater blending mode solve this issue. It prevents new strokes from increasing the opacity of existing pixels on the canvas beyond your current maximum opacity setting. It may not sound intuitive, but it does feel very natural when you use it.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-greater-blending-mode.png" caption="Normal (left) vs greater blending mode (right)" >}}

### Gimp brushes support (loading and saving)

You can now both load and save animated brush tips using Gimp's GIH format. This works a bit like importing Photoshop's ABR files: Krita will load the brush tip and add it to your library. For this to work, you have to use the "Import Resources" button in the brush preset editor. If your Gimp file contains multiple layers, you'll be able to import them as an animated brush tip.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-loading-and-saving-gimp-brushes.png" caption="Krita now loads and saves brush tips in Gimp’s format" >}}

### Improved pop-up palette

The pop-up palette got a little polish in this version. The brush icons are now displayed as circles, so they'll always show most of the preset's thumbnail. They also automatically resize based on the amount of brushes you want to display. It is easier to pick the right brush among a dozen or more now!

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-color-palette-new-look.jpg" caption="Krita's new pop-up palette has round icons" >}}

### Stable and faster GMIC on windows

GMIC, the open source image processor, is now stable on Windows. No more violent crashes! Not only that, it now uses all of your CPU threads for rendering, thus it is much faster.

You can find it at the bottom of the filter menu. This tool is a library of more than 400 image effects. They range from simple artistic filters, blurs and sharpen masks to powerful layer splitting tools, as shown in this comic book coloring tutorial by David Revoy.

[Krita 2.9 tutorial - Gmic colorize by David Revoy](//www.youtube.com/watch?v=YigbVY9s6gU)

### Import and export PDF (Windows)

This was already possible on Linux, but not on Microsoft's operating system. In Krita 3, you can both load and export PDF files on Windows.

### Windows shell extension

Another great addition for Windows users is the new shell extension. This tiny program gives Windows Explorer the ability to display thumbnails and metadata for your Krita files.

{{< figure src="/img/post/krita/new-in-krita-3/krita-3-windows-shell-extension.jpg" caption="Preview your Krita files from the Explorer with the shell extension" >}}

### And more!

Since May 2015, the development team released 11 updates for Krita 2.9. These brought a wide range of improvements to the program. As you can guess, a lot has changed since last year, to the point where there is just too much to talk about! I made a video a few months ago to highlight some of those changes.

[Krita's New Features since v2.9.5](//www.youtube.com/watch?v=PIKfrqk09Hk)

## Krita 3 Review: My Verdict after 9 Months {#krita-3-review}

Now you know what Krita 3 has in store for you. But if you have never heard of Krita, or if you barely used it, you might wonder: is it good? Should I give it a try?

I've been following Krita's progress since the first Windows release, version 2.8. At first, I found it quite impressive _for an open source project_, but it was way behind mainstream programs for game artists. It was unstable, slow, and it lacked too many features for me to do my job.

I'm really picky with the programs I choose. I only work with tools that are flexible and that feel well-designed. Although I'm deeply interested in open source, I wouldn't shoot myself in the foot just for the sake of using open source tools. I still use Microsoft office and FL studio in my work for example.

Yet, I've been working with both Krita and Photoshop side-by-side for the past 9 months. If I have done so, it is only because the experience was satisfying. Krita has some unique tools to its name. You can draw in horizontal, vertical and radial symmetry. There is a built-in brush stabilizer. Perspective guides. It is not perfect. Performances have been a major drawback. You have to work on big documents as a 2D game artist, and Krita 2.9 didn't like that. But again, this is mostly fixed in Krita 3.

Krita is great when it comes to painting. As far as games are concerned, it is a great tool for character design, environment design and hand-painted textures. Heck, even for animation! If you specialize in one of those fields, I bet you’ll like it! However, right now, it is not the best tool for everything. It is far from ideal when it comes to creating user interface. And you cannot batch export your sprites directly from the program.

### Final thoughts

I'll be honest: Krita still isn't the ultimate solution for game artists.

Yet, it is a great application. And a healthy open-source project. The developers release updates almost monthly. They listen to the community, which is invaluable in my opinion. They take anyone's feedback in account as long as it's constructive.

As far as I'm concerned, the program is mature for professional use. It's not perfect, but it's powerful. It easily competes with many paid alternatives I've tried in the past. Give Krita 3 a try. See what it has in store for you. You won't regret it!

Krita 3 is out now!

[Download Krita 3](//krita.org/en/download/krita-desktop/)
