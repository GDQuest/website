# GDQuest.com

![Website banner image](content/about/img/social-banner.png)

This is the complete source code for [GDQuest.com](http://gdquest.com/). The website is entirely open-source.

## Getting started

The website uses the static site engine [hugo](https://gohugo.io).

To test the site locally:

1. Install [hugo extended](https://github.com/gohugoio/hugo/releases). On the GitHub releases page of hugo, look for an executable named `hugo_extended_...`. This version of Hugo includes tools to process pictures and SCSS code.
1. Clone this repository.
1. In your terminal, navigate to the repository's folder and run `hugo server`.

This will build the website locally, watch for any file changes, and make it accessible on an address like `localhost:1313`.

## Style guide

For SCSS code, we follow the [RSCSS](https://rscss.io/) (_Reasonable System for CSS Stylesheet Structure_) style guide.

Note: some of the CSS code still doesn't follow the style guide. We're progressively moving code to that style-guide as we go.

## Contributing

Help is always welcome!

Found a bug, a typo? Feel free to fix it or [open a new issue](issues/new) for it. Also check out the [existing issues](issues).

Get in touch:

- Join the community on [Discord](https://discord.gg/CHYVgar)
- You can also find [GDQuest on Twitter](https://twitter.com/NathanGDQuest)

## Licenses

The website uses two licenses for its content and its source code, respectively:

- The website's content, that is to say, anything in the `content/` directory, or images in the `static/` directory, is available under the [CC-By 4.0](https://creativecommons.org/licenses/by/4.0/) license. If you reuse it, please attribute it to "[GDQuest](http://gdquest.com/) and contributors."
- The website's source code, including the `layouts/`, the `archetypes/`, and the `_src/` folder are under the MIT license.

For more information, see [LICENSE](LICENSE).
