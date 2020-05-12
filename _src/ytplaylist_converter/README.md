# Youtube playlist to Hugo markdown

This command-line tool converts playlists from YouTube to content pages for the static website engine hugo. It is designed to be ran manually, on your computer.

By using this tool and the YouTube API, you accept the YouTube API's Terms of Service and Google Privacy Policy. You can find the policies in details below:

- [YouTube Developer Policy](https://developers.google.com/youtube/terms/developer-policies)
- [YouTube API Terms Of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service)
- [Google Privacy Policy](https://policies.google.com/privacy#enforcement)

It uses the YouTube API to query information about playlist IDs passed as command-line arguments and outputs website pages as markdown documents:

- One page for the playlist, that contains a list of the videos in the playlist.
- One page for each video in the playlist that contains an embedded version of the YouTube video.

## Example of a page output by the program

The markdown documents created by this tool only contain TOML metadata:

```toml
+++
author = "nathan"
date = "2017-06-05T16:09:54.000Z"
title = "[DEMO] Top-Down Car with Steering in Godot"
description = "Get a simple 2d car controller for your own games! Under the MIT license"
type = "video"
videoid = "d6jICPx6Dto"
+++
```

You can use the website engine [hugo](https://gohugo.io/) to create a static html document from this metadata.

## Getting started

Here is how to install the program's dependencies and get started using it.

### Installing dependencies with pipenv

The program depends on some external packages. You need to create a python environment and install the dependencies.

```bash
pipenv install --dev
```

If you don't have pipenv installed, install it with pip, the package manager that comes preinstalled with Python. On Linux:

```bash
pip3 install pipenv
```

### Storing your YouTube API key as an environment variable

The program reads your API key from the `YT_API_KEY` environment variable.

You can set it locally, by creating a file named `.env` next to `ytplaylist-to-pages.py`. In it, write your `YT_API_KEY` variable as you would usually for your shell:

```bash
export YT_API_KEY="put your API key here"
```

Another option, if you want your API key to be available system-wide, is to export it in your shell's profile. For example, in your `$HOME/.profile` file:

### Running the program

Then run the program using `pipenv run`. You can download as many playlists as you need:

```bash
pipenv run python3 ytplaylist-to-pages.py -- playlist_id_1 playlist_id_2
```

To see all available features and get help, run:

```bash
pipenv run python3 ytplaylist-to-pages.py --help
```
