#!/usr/bin/env python3
"""Creates a new content page."""

import argparse
import datetime
import os
import re
from os.path import join

import pyyoutube

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
FRONT_MATTER_TUTORIAL: dict = dict(
    FRONT_MATTER_COMMON,
    {"difficulty": "beginner", "resources": {"src": "banner.png", "name": "banner"},},
)
FRONT_MATTER_VIDEO: dict = dict(
    FRONT_MATTER_COMMON, {"videoId": "", "videoDuration": ""}
)
FRONT_MATTER_REDIRECT: dict = {
    "date": datetime.date.today(),
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


def get_video_data(video_id: str):
    YT_API_KEY = os.getenv("YT_API_KEY")
    api = pyyoutube.Api(api_key=YT_API_KEY())
    video = api.get_video_by_id(video_id=video_id).items
    return video


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

    kind: str = args.section
    if args.video_id:
        kind = "video"
    if args.kind:
        kind = args.kind
    assert kind in front_matter_template

    if args.video_id:
        video = get_video_data(args.video_id)
        import pprint

        pprint.pprint(video)
        return

    front_matter: dict = front_matter_template[kind]
    front_matter["title"] = args.title
    if args.author:
        front_matter["author"] = args.author
    if args.description:
        front_matter["description"] = args.description

    content_dirname = args.dirname if args.dirname else title_to_dirname(args.title)
    path_content = join(
        args.path, "content", args.section, args.dirpath, content_dirname, "index.md"
    )
    print(path_content)

    # TODO:
    # - Populate video front matter
    # - Convert front-matter to TOML
    # - Save document to content/


if __name__ == "__main__":
    main()
