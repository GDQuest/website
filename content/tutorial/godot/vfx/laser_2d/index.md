---
author: nathan
date: "2023-12-13"
description: Learn how to create a dynamic 2D laser beam in Godot using raycasts, animated lines, and particle effects. Implement casting, collision, and beam particles to create a visually stunning laser effect.
difficulty: beginner
keywords:
- godot 4 beginner tutorial
- learn godot 4
- laser
- raycast
- beam
- particle effect
menuTitle: 2D Laser in Godot 4
programVersion: "4.4"
resources:
- name: banner
  src: cover-laser2d-md.webp
software: godot
sort: 80
title: Create a 2D Laser in Godot 4
weight: 2
type: redirect
featured: false
tutorialType: "youtube"
redirect: https://gdquest.com/library/laser_2d
---

## Download the files to follow along

To download the starting files for this tutorial, click the button below:

{{< calltoaction 
url="//github.com/gdquest-demos/getting-started-with-godot-4/releases/download/1.0.0/2d-project-start.zip" 
text="Download The Godot Files"
class="-large -tall" >}}


## How to import the files in Godot

**Unzipping a ZIP file on Windows:**

Using the File Explorer: Right-click the ZIP file and select "Extract All" from the context menu.

**Unzipping a ZIP file on macOS:**

Double-click the ZIP file to automatically extract the contents of the ZIP file.

**Unzipping a ZIP file on Linux:**

Many file browsers on Linux. Have a right-click command to extract the contents of a ZIP file.

In Gnome files (also known as Nautilus), for example, you can right-click on a ZIP file and select "Extract Here".
In KDE's file manager, Dolphin, you can right-click on the ZIP file and select "Extract > Extract Archive Here".

## Your questions

### What's a ZIP file?

A ZIP file is like a folder that can hold multiple files or directories (folders inside folders) but as a single file on your computer, making it much easier to share online and download.

It also stores data in a compressed format. This means that the ZIP file takes up less space than the individual files or directories would, making it faster to download, to upload, and more lightweight to store.

### What's a Godot project?

A Godot project is a collection of files and folders that represent a game or application made using the Godot game engine. It contains all the assets, code, and settings of a game project or computer program.
