# Youtube playlist to Hugo markdown #

This tool converts playlists from YouTube to content pages for the static website engine hugo.

## Getting started ##

The program depends on some external packages. You need to create a python environment and install the dependencies.

```bash
pipenv install --dev
```

If you don't have pipenv installed, install it with pip, the package manager that comes preinstalled with Python. On Linux:

```bash
pip3 install pipenv
```

Then run the program using `pipenv run`. You can download as many playlists as you need:

```bash
pipenv run python3 ytplaylist-to-pages.py -- playlist_id_1 playlist_id_2
```

To see all available features and get help, run:

```bash
pipenv run python3 ytplaylist-to-pages.py --help
```
