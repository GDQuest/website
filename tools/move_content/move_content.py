#!/usr/bin/env python3
"""Moves a content page, adding an alias to it."""

import argparse
import re
import sys
import os
import toml
import shutil
from os.path import basename, join, dirname, realpath, listd
import os


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
    data["aliases"] += [path_content]
    return toml.dumps(data)


def get_args(args) -> argparse.Namespace:
    """Parses the command line arguments"""
    parser = argparse.ArgumentParser(description=__doc__,)
    parser.add_argument(
        "files",
        type=argparse.FileType("r"),
        nargs="+",
        default=[],
        help="Path to content files to move.",
    )
    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        default=sys.argv[-1],
        help="Target path to which to move the files.",
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Run the program without modifying or saving files, for debugging purposes.",
    )
    return parser.parse_args(args)


def main():
    args: argparse.Namespace = get_args(sys.argv[1:-1])

    for md_file in args.files:
        filepath = md_file.name
        content = md_file.read()

        try:
            front_matter, body = split_toml_front_matter(content)
        except Exception:
            print("error")
            continue

        front_matter = update_front_matter_aliases(front_matter, filepath)
        new_content = "\n".join(["+++", front_matter, "+++", body]).strip("\n")
        if not args.dry_run:
            path_out = get_path_out(filepath, args)
            save_document(new_content, path_out, args)
            move_dependencies(filepath, path_out)

    for md_file in args.files:
        md_file.close()


def get_path_out(filepath: str, args: argparse.Namespace) -> str:
    """Returns the desired output path for the input file `filepath` based on `args.output`"""
    file_name = basename(filepath)
    path_out = ""
    if file_name in ["index.md", "_index.md"]:
        file_dir = basename(dirname(realpath(filepath)))
        path_out = join(args.output, file_dir, file_name)
    else:
        path_out = join(args.output, file_name)

    return path_out


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
    for i in os.listdir(dirname(filepath)):
        shutil.move(i, dirname(path_out))


if __name__ == "__main__":
    main()
