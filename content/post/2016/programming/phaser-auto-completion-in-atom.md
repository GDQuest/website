---
title: Phaser auto completion in Atom
author: nathan
layout: post
date: 2015-10-03
slide_template:
  - default
category:
  - Game Design
  - Quick Tips
type: post
aliases:
- game-design/phaser-auto-completion-in-atom/
---

_This little guide will show you how to use the tern-phaser plugin by [Angelo][1] with [Atom][2]._

## Installing tern

This first part explains how to get npm, install tern and the tern-phaser plugin. The first thing that you need to ensure is that you have Node.js installed on your computer. You can download it on <https://nodejs.org/en/>. This will give you access to npm as well, a handy package manager for js libraries and plugins. It allows you to download install all sorts of packages from the command prompt.

Once Node.js has finished installing, we have a few commands to call from the command prompt. On windows, you can access the command line need to press the Windows R key combination, type &#8220;cmd&#8221; and press enter.

&nbsp;

![](http://i.imgur.com/HVB8KRn.png)

Then we need to install a few packages. First, there is tern, the JS analyzer that the tern-phaser plugin uses. In the command line tool, type &#8220;npm install tern&#8221; and press enter. Npm will take care of the install for you, it will just take a moment.

![](http://i.imgur.com/H1xIdew.png)

We then need the tern-phaser plugin to be installed where the tern package has been put. You can let windows find the folder for you by typing &#8220;npm install -g tern-phaser&#8221; in the command prompt and pressing enter.

![](http://i.imgur.com/qqUNi8c.png)

## The manual route

**If the automatic install of tern-phaser doesn&#8217;t work**, you&#8217;ll have to go navigate to the tern install folder manually from the command prompt. To change the folder the command prompt is in, you need to type cd (_current directory_) followed by the path you want to reach. By default, tern should be installed to C:\Users\**YourName**\AppData\Roaming\npm\node_modules.

In the command prompt, you then have to enter &#8220;cd C:\Users\**YourName**\AppData\Roaming\npm\node_modules&#8221;. Note that you can copy the path from windows and paste it in the command prompt using the right mouse button (_Ctrl V doesn&#8217;t work by default_).

![](http://i.imgur.com/4shbnrB.png)

![](http://i.imgur.com/rX9oAKb.png)
_Right click on the command line tool to paste text._

Once you got to the right folder, just type npm &#8220;install tern-phaser&#8221; and press enter.

![](http://i.imgur.com/zJusEnO.png)
_Without -g, the command installs the tern-phaser package in the folder you&#8217;re currently in._

## Using tern-phaser with Atom

Now, you have both tern and tern-phaser installed on your computer. Let&#8217;s move to setting up atom to work with tern. There is no native integration of tern in atom. However, there is a plugin called **atom-ternjs** that works like a charm. We can install the package from the command line as well. Either **close and reopen the command** **prompt** or navigate back to your root folder with the following command: &#8220;cd C:\Users\YourName&#8221;.

Then, to call the Atom Package Manager, you need to use the apm command. Type &#8220;apm install atom-ternjs&#8221; and press enter. This will add this package to atom for you. To use tern with your project, you just need to have a tern configuration file. Atom-ternjs can create a basic config file for you. In Atom, you first need to have at least one javascript file loaded. Then, go to packages -> Atom ternjs -> Configure project

![](http://i.imgur.com/QjFJpud.png)

You can set some parameters in the newly opened tab and click on save and restart server. This will create a new .tern-project file in your project folder. We still need to tell it to use the phaser plugin. You just have to add &#8220;phaser&#8221; in the plugins section. Here&#8217;s the content of my .tern-project file:

&nbsp;

  <p>
    {   &#8220;ecmaVersion&#8221;: 5,   &#8220;libs&#8221;: [&#8220;browser&#8221;],   &#8220;plugins&#8221;: {     &#8220;phaser&#8221;: {}   } }
  </p>

![](http://i.imgur.com/EC06Yl4.png)

Save your file, and then go to package -> Atom Ternjs -> Restart server. If you don&#8217;t get any error, you&#8217;re good to go! _Note that having a phaser.js file next to your .tern-project file can prevent tern-phaser from working &#8211; in which case you&#8217;ll get a series of errors in Atom_.

<img src="http://i.imgur.com/Fd9QqM3.png" alt=""/>

 [1]: https://github.com/angelozerr
 [2]: http://atom.io
