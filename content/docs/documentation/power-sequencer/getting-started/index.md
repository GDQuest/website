+++
title = "Getting Started"
description = "Get to know Power Sequencer's core tools and workflow in this introductory guide."
author = "nathan"

date = 2019-12-19T10:23:34+01:00
weight = 0
+++

This guide is here to get you started with Power Sequencer. It will show you time-saving features when editing with the add-on.

Power Sequencer builds upon Blender's Sequencer and adds features to help you save time when editing. It focuses on everything that has to do with cutting, trimming, moving, importing, and deleting sequences. It does not add features related to compositing or motion design.

Also, we designed it to work in conjunction with other add-ons like the [VSE Transform Tools](https://github.com/doakey3/VSE_Transform_Tools), an add-on to manipulate images directly in the sequencer preview.

## Activating the add-on ##

1. Open Blender
1. Go to `Edit > Preferences > Addons` to open the Preferences window
1. In the search box, search for "Power Sequencer"
1. Activate the checkbox next to "Sequencer: Power Sequencer"

By default, Blender will save your preferences and the add-on will be active the next time you start Blender.

## Importing your work ##

We designed Power Sequencer to work well with projects where the blend file and all the footage are in one directory:

```
.
├── 03.state-class-1.blend
└── footage
    ├── 03.state-class-1.flv
    ├── 03.state-class-2-fix-end.flv
    ├── 03.state-class-3-fix-end-2.flv
    └── BL_proxy
```

To import all the video, audio, and image files at once, go to the Power Sequencer menu and click `File -> Import Local Footage` (<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>I</kbd>). 

This feature adds strips to the editing board for each file found in your project folder. It also detects already imported footage, and only imports newly found files by default.

### Proxy preferences ###

Power Sequencer sets the strips it imports to use proxies automatically, based on your preferences:

1. Go to the Addons tab of the Preferences window
1. Search for "Power Sequencer"
1. Click the white triangle "⏴" to expand the add-on's preferences.
1. Click on the checkboxes under "Proxy" to set sequences to use these proxy sizes by default.

![Proxy preferences in the addon](./img/setting-proxy-preferences.png)

## Cutting and trimming ##

A fair part of our work as editors it to make cuts in the source footage. The add-on comes with tools to save you time doing so.

### Three-point editing ###

<!-- You can use I and O to trim the left and right side of strips under the mouse cursor or the time cursor. This is not three point editing per se, as blender doesn't store any metadata about the edits. This tool directly trims the strips, but it's good to prepare your strips for editing. -->

### The interactive trim tool ###

<!-- Explain how to change the playback speed on the fly. Note the limitations of that feature: at higher speeds, the audio gets chopped up and harder to understand. -->

### Cutting audio strips ###

<!-- You can show concatenate there, as it's powerful in this setting. -->

## Adding fades and crossfades ##

For crossfades to work best, you should keep related strips into a single channel. Blender will add a gamma cross strip in between two visual strips. It makes it easy to remove the crossfade later and prevents your editing board from getting messy.

### Editing and removing fades ###

### Removing crossfades ###

## Rendering the video ##

<!-- Setting the preview range to the selected strips. -->

<!-- Apply a render preset and render the animation. -->

