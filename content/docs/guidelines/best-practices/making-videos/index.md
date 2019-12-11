+++
author = "nathan"
date = "2019-07-07T09:34:00+09:00"
description = "This document is a living tool to help us improve the educational value and the consistency of our video lessons."
title = "Best Practices: Making Videos"
menuTitle = "Making Tutorials"
weight = 4
aliases = ["/open-source/guidelines/gdquest-videos/"]

+++

This document is a living guide to help us improve the quality and consistency across all our tutorials. It focuses on practical tips about writing, recording, and editing. For notes on education, see [Education in online tutorials]({{< ref "docs/guidelines/best-practices/education/index.md" >}}).

Creating great videos starts with **planning**, **writing**, and **recording good footage**. I detail my approach to this in the video below.

{{< youtube n0jir8KmVI8 >}}

## Video recording ##

You will save a lot of time if your source material is clean and your speech precise. If you don't take the time to plan, you will limit the quality of your tutorial.

You should always record:

- At **1920x1080**, in full-HD
- At **29.97 Frames Per Second**, also called NTSC or NTSC film

Your footage should be smooth, not choppy. Be careful that the framerate does not drop in your recordings. To do so, I recommend you to do a test recording at the start of recording sessions or when you change your recording environment. This way you'll ensure that the visual quality and audio levels are working as expected.

You should **suppress or close any program that can distract the viewer** from the tutorial:

- Turn off Notifications
- Close chat applications
- Make the programs full-screen
- Suppress system sounds

**Avoid waving the mouse cursor** as you talk. Put the mouse or stylus down when you're talking, and you're not pointing at anything in particular. The motion can be distracting.

**Set the desktop audio channel to record at a low volume** so it doesn't cover your voice. I keep it at -20db to -30db most of the time in OBS Studio.

![OBS mixer](./img/obs-mixer.png)

When you make a small mistake or need to re-record a sentence, **clap in front of the mic**. This produces a sharp vertical line on the audio waveform that makes it easy for the editor to find and remove the faulty parts.

![Clap on audio waveform](./img/waveform.png)


### Setting up the microphone ###

The closer you are to the microphone when you record, the louder your voice will be relative to the sound reflected by your environment. You should place the microphone no more than 50cm away from your mouth if you can.

Don't place your mouth right next to the microphone if you still move your head while recording: your movement will cause significant changes in your voice's volume.

The voice should be normalized at around -6db. Use other YouTube videos or one of your recordings with good audio levels for reference. Always check your edit against the reference before exporting your video.

### Preventing mouth noises ###

Mouth noises happen when your mouth is dry, or after drinking coffee, tea, and some other beverages.

If you drank one of these, try to brush your teeth, tongue, and palate before recording.

Keep a bottle or a glass of water next to you to stay hydrated.

### Warming up ###

The mouth and vocal folds move thanks to muscles. To articulate to your fullest and to get the most out of your voice, you need to warm up, like before any exercise. At least for a minute or two.

**The longer the recording session, the longer you should warm up**.

Here's a [short vocal warm up](https://www.youtube.com/watch?v=9tXK7cw9mrg) from Julian Treasure's TED talk. You want to warm up your lips, your tongue, and your jaw. The siren exercise then focuses on the vocal cords. To improve pronunciation of specific sounds, add a few [tongue twisters](http://pun.me/pages/tongue-twisters.php): they'll serve both as an exercise and complete your warm up.

### Take your time ###

If you're struggling to explain something while recording, clap, and take the time to breathe and to think. Rehearse the complex idea in your mind or in front of the microphone. You can leave the recording running in the meantime. When you're ready, do a clean and confident take. It's easy to edit the long silence out later.

### Program layout ###

Use one of the default interfaces and, when possible, the default interaction mode for the program covered in the video.

E.g. for Blender 2.80 and up, left click is the default to select and grab objects. As viewers stumble upon videos organically and generally won't watch them in a particular order, the tutorials should stay close to the programs' default settings. There are some exceptions for tools like the shell, vim, or emacs that, once you've learned the basics, you are meant to customize a lot.

Make the program **full-screen** whenever possible. Many programs use the <kbd>F11</kbd> key or a related shortcut for that.

- For Godot, before recording, go to Editor -> Editor Layout -> Default to reset the interface.
- For Krita, I recommend using the Big Paint workspace over the default, as it centers the canvas on screen. It also shows the Layers, color palette, tool options, document overview, brushes, toolbox, and advanced color selector: everything you need to paint is visible on screen.

### Font size ###

The font size should be large enough for the video to read on a tablet, or depending on the video, on a large mobile phone in landscape orientation. If the program supports it, increase the font size to 20pt or more.

For instance, in Godot, I use 20pt for the editor's font and 23pt for the code. Past 20pt, the editor's layout can feel too packed.


## Video editing ##

Avoid abrupt cuts in both the audio and the video. You should cut mistakes and long silences or hesitations, but avoid cutting too much between words. Especially if you are editing live footage: too many cuts and the video will feel robotic or sped up. There's a natural rhythm to the human speech that you want to preserve.

Assume the viewer is facing new information and have a big cognitive load when watching your videos. Anything that makes it harder to keep track of what the teacher is doing increases that load:

1. The lack of visual continuity between shots.
2. Making any change in the project without communicating it to the viewer.

That is why you should use the visuals, audio cues, and our voice to make understanding minor details of the tutorial as comfortable as possible for the student. Things like navigating through the program, navigating through code, or when you bring up a topic that's not illustrated by the original recording.

When navigating around the interface or documents, show how you get there with the mouse cursor. If possible, also say where you are going.

Examples: show when you are launching the game preview in Godot, tell the viewer when you change the script in the text editor, etc.

Use a program to display the keys you are pressing when using keyboard shortcuts.

Add an arrow or some graphic element as an overlay on the video to help guide the viewer's eye to a specific area of the screen, an icon, a label, etc.
