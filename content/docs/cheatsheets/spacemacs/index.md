+++
author = "nathan"
date = "2019-08-27T11:32:05+02:00"
description = "A list of some features I find most useful in Spacemacs."
title = "Spacemacs"
aliases = ["/open-source/cheatsheets/spacemacs/"]

+++

Here is my living cheatsheet, a growing list of vim tips and spacemacs features I find particularly useful.
<!-- Use shortcuts template and data? -->

## Jumps ##

In Spacemacs, jumps are bound to <kbd>SPC</kbd> <kbd>J</kbd>. Some of these features help you to navigate around your text or code fast.

You can combine jumps with any command. For instance, `d`, delete, followed by a jump, will delete to the jump location.

- <kbd>SPC</kbd> <kbd>J</kbd> <kbd>J</kbd>: Jump anywhere in visible windows by typing the characters you want to jump to.
- <kbd>SPC</kbd> <kbd>J</kbd> <kbd>W</kbd>: Jump to a word in any visible window by typing its first character.
- <kbd>SPC</kbd> <kbd>J</kbd> <kbd>i</kbd>: Jump to a title, a function definition, a class, etc. anywhere inside the current buffer with helm. Type patterns to filter down the list and press <kbd>RET</kbd> to jump.
- <kbd>SPC</kbd> <kbd>s</kbd> <kbd>s</kbd>: Swoop, search the current file for patterns, and navigate to the matching lines. Use <kbd>Ctrl</kbd> <kbd>n</kbd> and <kbd>Ctrl</kbd> <kbd>p</kbd> to navigate to the **n**ext and **p**revious search results. You can do a lot with this feature, but you can also use it to intuitively move around your file.

### Vim commands ###

Here are some Vim commands I use to jump a lot:

- <kbd>\*</kbd>: Search the word under the cursor jumping forward.
- <kbd>\#</kbd>: Search the word under the cursor jumping backward.
- <kbd>Ctrl</kbd> <kbd>d</kbd>: Move **d**own half a page
- <kbd>Ctrl</kbd> <kbd>u</kbd>: Move **u**p half a page
- <kbd>Ctrl</kbd> <kbd>f</kbd>: Move **f**orward one page.
- <kbd>Ctrl</kbd> <kbd>b</kbd>: Move **b**ack one page.
