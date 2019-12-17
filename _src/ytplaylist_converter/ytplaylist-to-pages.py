import argparse
import os
import re

import config as cfg
import pyyoutube as yt
import utils as u


def sanitize_title(title):
    return re.sub(
        r"[-:,/?]|(\[.*\])|(\(.*\))",
        "",
        title.lower().replace(" ", "_").replace(".", "_"),
    )


def get_base_path(args, playlist):
    title = sanitize_title(args.title or playlist.snippet.title)
    path = os.path.join(
        args.path or os.path.join(cfg.DIR, args.playlist),
        os.path.join("content", "tutorial") if args.path else "",
    )
    if args.folders is not None:
        path = os.path.join(path, *args.folders)
        path = os.path.join(path, title)
    return path


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
    playlists_res = api.get_playlist_by_id(playlist_id=args.playlist, parts=["snippet"])
    playlist = playlists_res.items[0]

    path = get_base_path(args, playlist)
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "_index.md"), "w") as f:
        f.write(
            cfg.FRONTMATTER["series"].format(
                date=playlist.snippet.publishedAt,
                description=args.description
                or playlist.snippet.description.split("\n")[0],
                title=args.title or playlist.snippet.title,
            )
        )

    #  playlist_res = u.get_playlist_all_items(api, playlist_id=args.playlist)


if __name__ == "__main__":
    try:
        main()
    except (IndexError) as error:
        print(error)


#  def main():
#      playlist_id = args.playlist
#
#      playlist_url = "/playlists/?maxResults=25&id={}&part=snippet%2CcontentDetails&key={}".format(
#          playlist_id, API_KEY
#      )
#      playlist_request = requests.get("{}{}".format(BASE_URL, playlist_url))
#      playlist_data = playlist_request.json()
#
#      playlist_snippet = playlist_data["items"][0]["snippet"]
#
#      series_title = args.title if args.title != None else playlist_snippet["title"]
#      path = get_base_path(series_title)
#      print(path)
#      videos_path = os.path.join(path, VIDEOS_FOLDER)
#      create_directories(videos_path)
#
#      with open(os.path.join(videos_path, "_index.md"), "w") as f:
#          f.write(chapter_description)
#
#      series_description = series_description_format.format(
#          date=playlist_snippet["publishedAt"],
#          description=args.description
#          if args.description != None
#          else playlist_snippet["description"].split("\n")[0],
#          title=series_title,
#      )
#
#      with open(os.path.join(path, "_index.md"), "w") as f:
#          f.write(series_description)
#
#      url_videos = "/playlistItems?maxResults=50&part=snippet,contentDetails&key={}&playlistId={}".format(
#          API_KEY, playlist_id
#      )
#      video_requests = requests.get("{}{}".format(BASE_URL, url_videos))
#      videos_data = video_requests.json()
#
#      for video in videos_data["items"]:
#          snippet = video["snippet"]
#          print(
#              snippet["title"]
#              + " / "
#              + "https://www.youtube.com/watch?v="
#              + snippet["resourceId"]["videoId"]
#          )
#
#          description = snippet["description"].split("\n")[0]
#
#          position = snippet["position"]
#          video_data = video_file_format.format(
#              date=snippet["publishedAt"],
#              weight=position,
#              title=snippet["title"],
#              description=description,
#              video_id=snippet["resourceId"]["videoId"],
#          )
#
#          fname = get_formated_file_name(snippet["title"])
#          with open(os.path.join(videos_path, "%s_%s.md" % (position, fname)), "w") as f:
#              f.write(video_data)
#
#
#
#
#  def create_directories(path):
#      if args.force:
#          os.makedirs(path, exist_ok=True)
#      else:
#          try:
#              os.makedirs(path)
#          except:
#              print(
#                  "The provided path already exists, if you'd like to rewrite it, use --force. Use -h for help"
#              )
#              sys.exit()
#
#
#
#
#  main()
