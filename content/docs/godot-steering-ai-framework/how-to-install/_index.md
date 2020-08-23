+++
date = "2020-02-13"
title = "Installation"
weight = 1
+++

This page explains how to install and to update the framework in your projects.

At the time of writing, Godot doesn't have a package manager, that is to say, a tool to easily install and remove dependencies in a project. Here are some instructions and tips to get the framework into your project.

In short, to get started, you can either copy the `addons/com.gdquest.godot-steering-ai-framework` directory and copy it into your project, or you can clone or submodule the files from [this repository](https://github.com/GDQuest/godot-steering-ai-framework-submodule). Keep your project organized and keep things in a directory! Once you open your project in Godot, the engine will automatically register all `GSAI*` classes and give you full auto-completion for them.

## First install ##

To install the framework:

1. Download the latest [GitHub release](https://github.com/GDQuest/godot-steering-ai-framework/releases).
2. Copy the content of the `godot/addons/com.gdquest.godot-steering-ai-framework/` directory.
3. Paste the files into your Godot project.

We recommend to place the framework in a directory where you will store all your third-party libraries or dependencies. For example `res://src/libraries/godot_steering_framework/`.

## Updating the framework ##

Before updating a third-party dependency, you should always read the release notes or the [changelog](https://github.com/GDQuest/godot-steering-ai-framework/blob/master/CHANGELOG.md), in case some feature gets deprecated or a change may affect the behavior of your game. This can happen if the version of a tool you use has a bug on which your game relies.

We use [semantic versioning](https://semver.org/), so unless the framework's major release number changes, it should be safe for you to update to a new release.

{{% notice note %}} 
The major version of a framework is the first digit of the version number. For instance, in version `v2.1.0`, it is `2`.
{{% /notice %}} 

### How to update ###

To update to a new version:

1. Close your Godot project.
1. Delete your copy of the framework's files.
1. Download the latest [GitHub release](https://github.com/GDQuest/godot-steering-ai-framework/releases).
1. Copy the content of the `godot/addons/com.gdquest.godot-steering-ai-framework/` directory where you initially copied the files.
