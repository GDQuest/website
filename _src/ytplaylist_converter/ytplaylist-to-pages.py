import argparse
import os
from itertools import chain, groupby, starmap

import config as cfg
import pyyoutube as yt
import utils as u


def generate_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "playlist", help="The playlist ID you wish to convert the videos from"
    )
    parser.add_argument(
        "--path",
        help=(
            "Website's root directory. If none provided, a playlist folder"
            " will be created in the root."
        ),
    )
    parser.add_argument(
        "--folders",
        metavar="F",
        type=str,
        nargs="+",
        help=(
            "Folder structure in which this series should be placed inside"
            " i.e. game-design godot will result in game-design/godot/TITLE"
        ),
    )
    parser.add_argument(
        "--force",
        help="Rewrites the path in case it already exists",
        action="store_true",
    )
    parser.add_argument(
        "--title",
        help=("If left empty, the playlist's title will be used as the series' title."),
    )
    parser.add_argument(
        "--description",
        help=(
            "If left empty, the playlist's description"
            " will be used as the series' description."
        ),
    )
    return parser


def main():
    parser = generate_parser()
    args = parser.parse_args()
    if args.path is not None and args.folders is None:
        parser.error(
            "When using path, you should specify a folder structure"
            " using --folders. Use -h for help"
        )

    api = yt.Api(api_key=cfg.YT_API_KEY)
    playlists = api.get_playlist_by_id(
        playlist_id=args.playlist, parts=["snippet"]
    ).items

    paths = map(lambda p: u.get_base_path(args, p), playlists)
    for playlist, path in zip(playlists, paths):
        os.makedirs(path, exist_ok=args.force)
        with open(os.path.join(path, cfg.INDEX), "w") as f:
            f.write(
                cfg.FRONTMATTER["series"].format(
                    date=playlist.snippet.publishedAt,
                    description=args.description
                    or playlist.snippet.description.split("\n")[0],
                    title=args.title or playlist.snippet.title,
                )
            )

        path_chapter = os.path.join(path, cfg.DIR_CHAPTER)
        os.makedirs(path_chapter, exist_ok=args.force)
        with open(os.path.join(path_chapter, cfg.INDEX), "w") as f:
            f.write(cfg.FRONTMATTER["chapter"])

        playlists = api.get_playlist_items(
            playlist_id=args.playlist, parts=["snippet"], count=None
        ).items
        snippets = [p.snippet for p in playlists]
        snippets_grouped = groupby(
            enumerate(snippets), lambda ix: ix[0] // cfg.YT_MAX_RESULTS
        )
        videos = chain.from_iterable(
            [
                api.get_video_by_id(
                    video_id=[s.resourceId.videoId for _, s in snippets]
                ).items
                for _, snippets in snippets_grouped
            ]
        )
        for snippet, frontmatter in starmap(
            lambda s, v: (
                s,
                cfg.FRONTMATTER["video"].format(
                    date=s.publishedAt,
                    title=s.title,
                    description=s.description,
                    weight=s.position,
                    video_id=s.resourceId.videoId,
                    video_duration=v.contentDetails.get_video_seconds_duration(),
                ),
            ),
            zip(snippets, videos),
        ):
            path = os.path.join(
                path_chapter,
                "{}_{}.md".format(snippet.position, u.sanitize_title(snippet.title)),
            )
            with open(path, "w",) as f:
                f.write(frontmatter)


if __name__ == "__main__":
    try:
        main()
    except FileExistsError as error:
        print(
            "[error]: {}: {}. Use --force to overwrite".format(
                error.strerror, error.filename
            )
        )
    except yt.error.PyYouTubeException as error:
        print(
            "[error](code {}): {}".format(
                error.status_code, error.response.json()["error"]["errors"]
            )
        )
