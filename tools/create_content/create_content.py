#!/usr/bin/env python3
"""Creates a new content page."""

import argparse
import os
import re
from os.path import join

SECTIONS_SUPPORTED = ["tutorial", "news", "tools", "product"]
AUTHORS = ["nathan", "razvan", "henrique", "johnny", "razoric"]

def title_to_dirname(text: str) -> str:
    string = text.lower().replace(" ", "-").replace(".", "-")
    string = re.sub(
        r"[_:,/?]|(\[.*\])|(\(.*\))",
        "",
        string,
    )
    return re.sub(r"-+", "-", string, flags=re.DOTALL)



def generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "section",
        type=str,
        help="The section the content should go to. One of {}".format(
            SECTIONS_SUPPORTED
        ),
    )
    parser.add_argument(
        "title", type=str, help=("Title of the content post."),
    )

    parser.add_argument(
        "-p" "--path",
        type=str,
        default="",
        help=(
            "Website's root directory. If none provided, a playlists folder"
            " will be created in the root."
        ),
    )
    parser.add_argument(
        "-k", "--kind", help="Content kind to pass to the `hugo new` command."
    )
    parser.add_argument(
        "-d",
        "--dirname",
        type=str,
        help=("Name of the content's directory. If not set explicitly, "
              "generated from the `title` positional argument."),
    )
    parser.add_argument(
        "-i", "--video-id", help=("Url or id of a YouTube video."),
    )

    parser.add_argument(
        "-a", "--author", help="Author of the post. One of {}".format(AUTHORS)
    )
    parser.add_argument(
        "-d", "--description", help=("Description of the content."),
    )
    parser.add_argument(
        "-t", "--tags", nargs="+", help=("List of tags to put in the content."),
    )
    parser.add_argument(
        "-d",
        "--dirpath",
        type=str,
        default="",
        help=(
            "Relative path to the content's directory. Relative to the `section` argument. "
            "If not provided, the content's folder name is generated from the"
            "content's title."
        ),
    )

    parser.add_argument(
        "-f",
        "--force",
        help="Overwrites the content file if it already exists.",
        action="store_true",
    )
    parser.add_argument(
        "-o",
        "--open",
        help=(
            "Opens the content in your text editor, using the $VISUAL "
            "environment variable."
        ),
    )
    return parser


def main():
    args: argparse.Namespace = generate_parser().parse_args()

    if args.section not in SECTIONS_SUPPORTED:
        raise AttributeError(
            "The section {} must be one of {}".format(args.section, SECTIONS_SUPPORTED)
        )
    if args.author is not None and args.author not in AUTHORS:
        raise AttributeError(
            "The author {} must be one of {}".format(args.author, AUTHORS)
        )

    path_website = join(os.getcwd(), args.path)
    if not os.path.exists(path_website):
        raise NotADirectoryError("The directory path does not exist.")

    # Run command from the website path
    hugo_command = "hugo new {}"
    if args.kind is not None or args.video is not None:
        kind = args.kind if args.kind is not None else "video"
        hugo_command += " --kind " + kind

    content_dirname = args.dirname if args.dirname else title_to_dirname(args.title)
    path_content = join(args.section, args.dirpath, content_dirname, "index.md")

    author = args.author if args.author else "nathan"

    # TODO: use toml library to populate the front matter



if __name__ == "__main__":
    main()
