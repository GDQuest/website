#!/usr/bin/env python3
"""Moves a content page, adding an alias to it."""

from pprint import pprint
import argparse
import os
import re
import shutil
import sys
from os.path import basename, dirname, join, realpath, splitext

import toml


def split_toml_front_matter(content: str) -> str:
    """Returns a tuple of a document's toml front matter and its body.
    Assumes the document use toml front matter surrounded by +++, followed by a line break."""
    parts = re.split(r"\+\+\+\n(.*?)\+\+\+", content, maxsplit=1, flags=re.S)
    if len(parts) == 1:
        raise Exception("Could not extract the toml front matter from the content.")
    return parts[1:]


def update_front_matter_aliases(front_matter: str, filepath: str) -> str:
    """Returns the toml `front_matter` as a string with `filepath` as an added alias."""
    data = toml.loads(front_matter)
    if "aliases" not in data:
        data["aliases"] = []

    path_content = realpath(filepath).split("content/", 1)[-1]

    alias_new = splitext(path_content)[0]
    alias_new = re.sub("_?index$", "", alias_new)
    data["aliases"] += ["/" + alias_new]
    return toml.dumps(data)


def get_args(args) -> argparse.Namespace:
    """Parses the command line arguments"""
    parser = argparse.ArgumentParser(description=__doc__,)
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Run the program without modifying or saving files, for debugging purposes.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Move content files recursively in the directory, treating each as a content page.",
    )
    parser.add_argument(
        "files", type=str, nargs="+", default=[], help="Path to content files to move.",
    )
    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        default=sys.argv[-1],
        help="Target path to which to move the files.",
    )
    return parser.parse_args(args)


def main():
    args: argparse.Namespace = get_args(sys.argv[1:-1])

    files = []
    base_path = dirname(args.files[0])
    base_dirpath = dirname(base_path)
    if args.recursive:
        for dirpath, dirnames, filenames in os.walk(base_path, topdown=False):
            dir_relpath = os.path.relpath(dirpath, base_dirpath)
            files += [join(dir_relpath, f) for f in filenames if f.endswith(".md")]
    else:
        files = args.files

    for path in files:
        filepath = join(base_dirpath, path) if args.recursive else path
        with open(filepath, "r") as md_file:
            content = md_file.read()

            front_matter, body = split_toml_front_matter(content)
            front_matter = update_front_matter_aliases(front_matter, filepath)
            new_content = "\n".join(["+++", front_matter, "+++", body]).strip("\n")
            path_out = join(args.output, path)
            if not args.dry_run:
                save_document(new_content, path_out)
                os.remove(filepath)
                if basename(filepath) in ["index.md", "_index.md"]:
                    move_dependencies(filepath, path_out)


def save_document(content: str, path_out: str):
    """Saves `content` to `path_out`, creating directories if necessary. """
    out_dir = dirname(path_out)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    with open(path_out, "w") as document:
        document.write(content)


def move_dependencies(filepath, path_out):
    """Moves the dependencies of a leaf bundle, that is to say, the content of a directory containing an
index.md document."""
    dir_start = dirname(filepath)
    for i in os.listdir(dir_start):
        if i.endswith(".md"):
            continue
        path = join(dir_start, i)
        shutil.move(path, dirname(path_out))


if __name__ == "__main__":
    main()
