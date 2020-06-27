#!/usr/bin/env python3
"""Creates a new content page."""

import argparse
import datetime
import os
import re
from os.path import join, dirname

import pyyoutube
import toml
import json

SECTIONS_SUPPORTED = ["tutorial", "news", "tools", "product"]
AUTHORS = ["nathan", "razvan", "henrique", "johnny", "razoric"]

KINDS = ["course_chapter", "course", "video"]

# Front matter
FRONT_MATTER_COMMON: dict = {
    "author": "nathan",
    "date": datetime.date.today(),
    "description": "",
    "title": "",
    "weight": "5",
    "keywords": [],
    "tags": [],
}
FRONT_MATTER_TUTORIAL: dict = {
    **FRONT_MATTER_COMMON,
    "difficulty": "beginner",
    "resources": {"src": "banner.png", "name": "banner"},
}
FRONT_MATTER_VIDEO: dict = {**FRONT_MATTER_COMMON, "videoId": "", "videoDuration": ""}
FRONT_MATTER_REDIRECT: dict = {
    "date": datetime.date.today().isoformat(),
    "description": "",
    "title": "",
    "weight": "5",
    "redirect": "",
    "type": "redirect",
    "tags": [],
}

front_matter_template = {
    "news": FRONT_MATTER_COMMON,
    "tutorial": FRONT_MATTER_TUTORIAL,
    "course": FRONT_MATTER_TUTORIAL,
    "course_chapter": FRONT_MATTER_COMMON,
    "video": FRONT_MATTER_VIDEO,
    "redirect": FRONT_MATTER_REDIRECT,
}


def title_to_dirname(text: str) -> str:
    """Converts a title into a sanitized dirname.

    title_to_dirname('Godot for Designers') outputs 'godot-for-designers'"""
    string = text.lower().replace(" ", "-").replace(".", "-")
    string = re.sub(r"[_:,/?]|(\[.*\])|(\(.*\))", "", string,)
    return re.sub(r"-+", "-", string, flags=re.DOTALL)


def get_front_matter(args: argparse.Namespace()) -> dict:
    """Returns the front matter of the article as a python dictionary."""
    kind: str = args.section
    if args.video_id:
        kind = "video"
    if args.kind:
        kind = args.kind
    assert kind in front_matter_template

    front_matter: dict = front_matter_template[kind]
    front_matter["title"] = args.title
    if args.author:
        front_matter["author"] = args.author
    if args.description:
        front_matter["description"] = args.description
    if args.video_id:
        video = get_video_data(args.video_id)
        front_matter["videoId"] = args.video_id
        front_matter["title"] = args.title if args.title != "" else video["title"]
        front_matter["description"] = (
            args.description if args.description != "" else video["description"]
        )
        front_matter["date"] = video["date"]
    if args.menu_title:
        front_matter["menuTitle"] = args.menu_title
    return front_matter


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
        "-p",
        "--path",
        type=str,
        default=".",
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
        help=(
            "Name of the content's directory. If not set explicitly, "
            "generated from the `title` positional argument."
        ),
    )
    parser.add_argument(
        "-i", "--video-id", help=("ID of a YouTube video."),
    )

    parser.add_argument(
        "-a", "--author", help="Author of the post. One of {}".format(AUTHORS)
    )
    parser.add_argument(
        "-D", "--description", help=("Description of the content."),
    )
    parser.add_argument(
        "-t", "--tags", nargs="+", help=("List of tags to put in the content."),
    )
    parser.add_argument(
        "-m",
        "--menu-title",
        type=str,
        help=("Optional menu title for tutorial navigation."),
    )
    parser.add_argument(
        "-P",
        "--dirpath",
        type=str,
        default="",
        help=(
            "Relative path to the content's directory. Relative to the `section` argument."
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


def save_document(content: str, path_out: str):
    """Saves `content` to `path_out`, creating directories if necessary. """
    out_dir = dirname(path_out)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    with open(path_out, "w") as document:
        document.write(content)


def get_video_data(video_id: str) -> str:
    """Returns the video data as a dictionary with 'title', 'description', and published 'date'."""
    YT_API_KEY = os.getenv("YT_API_KEY")
    api = pyyoutube.Api(api_key=YT_API_KEY)
    data: dict = api.get_video_by_id(
        video_id=video_id, parts="snippet", return_json=True
    )
    snippet: dict = data["items"][0]["snippet"]
    return {
        "date": snippet["publishedAt"][:-1],
        "title": snippet["title"],
        "description": snippet["description"].split("\n", 1)[0],
    }


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

    content_dirname = args.dirname if args.dirname else title_to_dirname(args.title)
    path_content = os.path.realpath(
        join(
            args.path,
            "content",
            args.section,
            args.dirpath,
            content_dirname,
            "index.md",
        )
    )

    front_matter: dict = get_front_matter(args)
    front_matter_text: str = "+++\n" + toml.dumps(front_matter) + "+++\n"

    save_document(front_matter_text, path_content)


if __name__ == "__main__":
    main()
