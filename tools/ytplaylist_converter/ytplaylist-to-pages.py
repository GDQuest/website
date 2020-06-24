# This tool uses the YouTube API. By using this program, you agree to the terms of the YouTube API Terms Of Service and the Google Privacy Policy:
#
# YouTube Terms of Service: https://www.youtube.com/t/terms
# YouTube API Terms Of Service: https://developers.google.com/youtube/terms/api-services-terms-of-service
# Google Privacy Policy: https://policies.google.com/privacy#enforcement
import argparse
import os
from itertools import chain, groupby

import config
import pyyoutube
import utils


def generate_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "playlist",
        type=str,
        help="The playlist ID you wish to convert the videos from",
    )
    parser.add_argument(
        "--path",
        help=(
            "Website's root directory. If none provided, a playlists folder"
            " will be created in the root."
        ),
    )
    parser.add_argument(
        "--folders",
        metavar="F",
        type=str,
        nargs="+",
        help=(
            "Folder structure in which a playlist series should be placed"
            " i.e. '--folders game-design godot' will result in 'game-design/godot/TITLE'"
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
            "When using --path, you should specify a folder structure"
            " using --folders. Use -h for help"
        )
    elif args.folders is not None and len(args.playlist) != 1:
        parser.error(
            "When using --folders, multiple playlists aren't allowed."
            " Use -h for help"
        )

    api = pyyoutube.Api(api_key=config.YT_API_KEY)
    playlists = api.get_playlist_by_id(
        playlist_id=args.playlist, parts=["snippet"]
    ).items

    paths = map(lambda playlist: utils.get_base_path(args, playlist), playlists)
    for playlist, path in zip(playlists, paths):
        os.makedirs(path, exist_ok=args.force)
        with open(os.path.join(path, config.INDEX), "w") as f:
            frontmatter = config.FRONTMATTER["series"].format(
                date=playlist.snippet.publishedAt,
                description=args.description
                or playlist.snippet.description.split("\n")[0],
                title=args.title or playlist.snippet.title,
                playlist_id=args.playlist,
            )
            f.write(frontmatter)

        path_chapter = os.path.join(path, config.DIR_CHAPTER)
        os.makedirs(path_chapter, exist_ok=args.force)
        with open(os.path.join(path_chapter, config.INDEX), "w") as f:
            f.write(config.FRONTMATTER["chapter"])

        playlist_items = api.get_playlist_items(
            playlist_id=args.playlist, parts=["snippet"], count=None
        ).items

        snippets = [playlist.snippet for playlist in playlist_items]
        snippets_grouped = groupby(
            enumerate(snippets), lambda ix: ix[0] // config.YT_MAX_RESULTS
        )

        videos = [
            api.get_video_by_id(
                video_id=[s.resourceId.videoId for _, s in snippets]
            ).items
            for _, snippets in snippets_grouped
        ]
        videos = chain.from_iterable(videos)

        snippet_frontmatter = [
            (
                snippet,
                config.FRONTMATTER["video"].format(
                    date=snippet.publishedAt,
                    title=snippet.title,
                    description=snippet.description.split('\n', 1)[0],
                    weight=snippet.position,
                    video_id=snippet.resourceId.videoId,
                    video_duration=video.contentDetails.get_video_seconds_duration(),
                ),
            )
            for snippet, video in zip(snippets, videos)
        ]
        for snippet, frontmatter in snippet_frontmatter:
            path = os.path.join(
                path_chapter,
                "{}_{}.md".format(snippet.position, utils.sanitize_title(snippet.title)),
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
    except pyyoutube.error.PyYouTubeException as error:
        print(
            "[error](code {}): {}".format(
                error.status_code, error.response.json()["error"]["errors"]
            )
        )
