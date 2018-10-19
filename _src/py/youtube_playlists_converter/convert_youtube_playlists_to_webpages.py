import json
from pprint import pprint
import requests
import os
import shutil
import re
import argparse, sys

BASE_DIR = "./playlist"
VIDEOS_FOLDER = "chapter"
#os.makedirs(BASE_DIR, exist_ok=True)

parser = argparse.ArgumentParser()

parser.add_argument('playlist', help = 'The playlist ID you wish to convert the videos from')
parser.add_argument('--path', help = 'The absolute path to the website\'s root directory. If none provided, a playlist folder will be created in the root.' )
parser.add_argument('--folders', metavar='F', type = str, nargs = '+', help = 'Folder structure in which this this series should be placed inside i.e. game-design godot will result in game-design/godot/TITLE')
parser.add_argument('--force', help = 'Rewrites the path in case it already exists', action = "store_true")
parser.add_argument('--title', help = 'If left empty, the playlist\'s title will be used as the series\' title.')
parser.add_argument('--description', help = 'If left empty, the playlist\'s description will be used as the series\' description.')

args = parser.parse_args()

if args.path != None and args.folders == None:
  print("When using path, you should specify a folder structure using --folders. Use -h for help")
  sys.exit()

API_KEY = "AIzaSyAUCyzwHmO71chFn7wMa6VlBNzk0tpkFYk"
CHANNEL_ID = "UCxboW7x0jZqFdvMdCFKTMsQ"
DOMAIN = "https://content.googleapis.com"
API = "/youtube/v3"
BASE_URL = DOMAIN + API


#We won't need this playlists array anymore but I kept it here because it seems like it's being used
#as a history of what has already been added to the website

PLAYLISTS = [
  "PLhqJJNjsQ7KEVitqVB9WXfgzcj32Yz-iJ",
  #"PLhqJJNjsQ7KHqNMYmTwtsYTeTrqrRP_fP",
  # "PLhqJJNjsQ7KEr_YlibZ3SBuzfw9xwGduK",
  # "PLhqJJNjsQ7KEbSXHacP9eD37xyoPJz9gm",
  # "PLhqJJNjsQ7KEtFciikafqWU-OeU4SEejC",
  # "PLhqJJNjsQ7KExm_EYLVhD6yf4Afax24fV",
]


video_file_format = """---
author: nathan
date: {date}
title: "{title}"
description: "{description}"

type: video

videoid: {video_id}
---

"""

series_description_format = """---
title: '{title}'
description: {description}
date: {date}
author: nathan

keywords:
  - ENTER KEYWORDS

tags:
  - free
  - training

type: course

banner:
    src: banner.png

resources:
- src: banner.png
  name: banner
---
"""

chapter_description = """---
author: nathan
title: ENTER TITLE
description: ENTER DESCRIPTION

type: course_chapter

weight: 1
---
"""

def main():
  playlist_id = args.playlist
  
  playlist_url = "/playlists/?maxResults=25&id={}&part=snippet%2CcontentDetails&key={}".format(playlist_id, API_KEY)
  playlist_request = requests.get("{}{}".format(BASE_URL, playlist_url))
  playlist_data = playlist_request.json()
  
  playlist_snippet = playlist_data["items"][0]["snippet"]
  
  series_title = args.title if args.title != None else playlist_snippet["title"] 
  path = get_base_path(series_title)
  print(path)
  videos_path = os.path.join(path, VIDEOS_FOLDER)
  create_directories(videos_path)

  with open(os.path.join(videos_path, "_index.md"), "w") as f:
    f.write(chapter_description)

  series_description = series_description_format.format(
    date = playlist_snippet["publishedAt"],
    description = args.description if args.description != None else playlist_snippet["description"].split("\n")[0],
    title = series_title
  )

  with open(os.path.join(path, "_index.md"), "w") as f:
    f.write(series_description)

  url_videos = "/playlistItems?maxResults=50&part=snippet,contentDetails&key={}&playlistId={}".format(API_KEY, playlist_id)
  video_requests = requests.get("{}{}".format(BASE_URL, url_videos))
  videos_data = video_requests.json()

  for video in videos_data["items"]:
    snippet = video["snippet"]
    print(snippet["title"] + " / " + "https://www.youtube.com/watch?v=" + snippet["resourceId"]["videoId"])

    description = snippet["description"].split("\n")[0]

    position = snippet["position"]
    video_data = video_file_format.format(
      date=snippet["publishedAt"],
      weight=position,
      title=snippet["title"],
      description=description,
      video_id=snippet["resourceId"]["videoId"]
    )

    fname = get_formated_file_name(snippet["title"])
    with open(os.path.join(videos_path, "%s_%s.md" % (position, fname)), "w") as f:
      f.write(video_data)

def get_base_path(title):
  path = ""
  title = get_formated_file_name(title)
  if args.path == None:
    path = os.path.join(BASE_DIR, title)
  else:
    path = os.path.join(args.path, 'content\\tutorial\\')
    folders = ""
    for folder in args.folders:
      folders += folder + '\\'
    path = os.path.join(path, folders)
    path = os.path.join(path, title)
  return path

def create_directories(path):
  if args.force:
    os.makedirs(path, exist_ok=True)
  else:
    try:
      os.makedirs(path)
    except:
      print("The provided path already exists, if you'd like to rewrite it, use --force. Use -h for help")
      sys.exit()

def get_formated_file_name(name):
  return re.sub(r'[-:,/?]|(\[.*\])|(\(.*\))', "", name.lower().replace(" ", "_").replace(".", "_"))

main()