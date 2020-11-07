# GDQuest.com

![Website banner image](static/img/social-banner.png)

This is the complete source code for [GDQuest.com](http://gdquest.com/). The website is entirely open-source.

**Table of Contents:**

- [Getting started](#getting-started)
- [Writing content](#writing-content)
- [Style guide](#style-guide)
- [Contributing](#contributing)
- [Translating pages](#translating-pages)
- [Licenses](#licenses)

## Getting started

The website uses the static site engine [hugo](https://gohugo.io).

To test the site locally:

1. Install [hugo extended](https://github.com/gohugoio/hugo/releases). On the GitHub releases page of hugo, look for an executable named `hugo_extended_...`. This version of Hugo includes tools to process pictures and SCSS code.
1. Clone this repository.
1. In your terminal, navigate to the repository's folder and run `npm install`. You need to have [node.js](https://nodejs.org/en/) installed for that.
1. Once all node packages are installed, run `hugo server --buildDrafts`.

This will build the website locally, including draft pages, watch for any file changes, and make it accessible via a URL like `localhost:1313`.

## Writing content

To create a new page, use the `hugo new` command. You need to give it a path to a new markdown file relative to the `content/` directory.

```sh
hugo new tutorial/godot/3D/import-from-blender/index.md
```

The command above creates a new 3D Godot tutorial in `content/tutorial/godot/3D/import-from-blender/`. The file's name, `index.md`, is a special name for hugo that defines a page bundle. It links all other files in the directory, like images and videos, as resources of that new page. To define a new section, you want to name the file `_index.md` instead. Look into the `content/` directory for some examples.

You can also use the `--editor` option to open the newly created file in a text editor:

```sh
hugo new tutorial/godot/3D/import-from-blender/index.md --editor $VISUAL
```

On Linux, you can use one of the special variables `$EDITOR` and `$VISUAL` to respectively open the new document in a terminal-based editor or a graphical application like Atom or Emacs.

### Keeping the content as draft and publishing

Each document contains some metadata at the top, also called front-matter:

```
+++
title = "Importing 3D objects from Blender"
author = "nathan"
date = 2020-07-15

draft = true
+++
```

This metadata uses the TOML markup language. If the variable `draft` has the value `true`, the article is considered a draft and won't be published on the website. Remove the line `draft = true` for the article to be published.

## Style guide

For SCSS code, we follow the [RSCSS](https://rscss.io/) (_Reasonable System for CSS Stylesheet Structure_) style guide.

Note: some of the CSS code still doesn't follow the style guide. We're progressively moving code to that style-guide as we go.

## Contributing

Help is always welcome!

Found a bug, a typo? Feel free to fix it or [open a new issue](issues/new) for it. Also check out the [existing issues](issues).

Get in touch:

- Join the community on [Discord](https://discord.gg/87NNb3Z)
- You can also find [GDQuest on Twitter](https://twitter.com/NathanGDQuest)

## Translating pages

The website supports translations into any language.

We are currently working on a Spanish version of the tutorials, and we're looking to support languages such as French and Japanese. If you'd like to contribute to translating tutorials or other pieces of content, you're most welcome!

There are two ways you can translate a page:

1. Use [Gitlocalize](https://gitlocalize.com/repo/5450/), which gives you an accessible online editor and handy tools like one-click machine translation. Watch their [two-minute tutorial](https://www.youtube.com/watch?v=b09LDukIJiU) to get started.
2. Translate the files on your computer and use git instead. More on that below.

### Translating a page manually

To translate a page manually on your computer, you need to:

1. Fork this repository.
1. Clone your fork on your computer.
1. Head to the page's corresponding directory inside the repository's `content` folder.
1. Duplicate the `index.md` file you'll find there and add the target language's two-letter code to the extension.

For example, to translate the [game settings tutorial](https://www.gdquest.com/tutorial/godot/2d/settings-demo/) to French, you need to head to the directory `content/tutorial/godot/2D/character-customization/`, duplicate the file `index.md`, which is the tutorial written in English, and name the copy `index.fr.md`. For Spanish, name the file `index.es.md`. You can call it `name.ja.md` for Japanese. In general, you need to add the corresponding two-letter country code to the copied markdown file's extension.

## Licenses

The website uses two licenses for its content and its source code, respectively:

- The website's content, that is to say, anything in the `content/` directory, or images in the `static/` directory, is available under the [CC-By 4.0](https://creativecommons.org/licenses/by/4.0/) license. If you reuse it, please attribute it to "[GDQuest](http://gdquest.com/) and contributors."
- The website's source code, including the `layouts/`, the `archetypes/`, and the `_src/` folder are under the MIT license.

For more information, see [LICENSE](LICENSE).
