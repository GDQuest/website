import json
from pprint import pprint
import requests
import os
import shutil
import re
import sys

BASE_DIR = "./videos"
os.makedirs(BASE_DIR, exist_ok=True)

API_KEY = "AIzaSyAUCyzwHmO71chFn7wMa6VlBNzk0tpkFYk"
CHANNEL_ID = "UCxboW7x0jZqFdvMdCFKTMsQ"
DOMAIN = "https://content.googleapis.com"
API = "/youtube/v3"
BASE_URL = DOMAIN + API

PLAYLISTS = [
  "PLhqJJNjsQ7KHqNMYmTwtsYTeTrqrRP_fP",
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

# get videos in playlist
for playlist_id in PLAYLISTS:
  path = os.path.join(BASE_DIR, playlist_id)
  os.makedirs(path, exist_ok=True)

  url = "/playlistItems?maxResults=50&part=snippet,contentDetails&key={}&playlistId={}".format(API_KEY, playlist_id)
  r = requests.get("{}{}".format(BASE_URL, url))
  videos_data = r.json()

  for video in videos_data["items"]:
    snippet = video["snippet"]
    print(snippet["title"] + " / " + "https://www.youtube.com/watch?v=" + snippet["resourceId"]["videoId"])

    description = snippet["description"].split("\n")[0]

    pos = snippet["position"]
    vd = video_file_format.format(
      date=snippet["publishedAt"],
      weight=pos,
      title=snippet["title"],
      description=description,
      video_id=snippet["resourceId"]["videoId"]
    )

    fname = re.sub(r'[-:,/?]|(\[.*\])|(\(.*\))', "", snippet["title"].lower().replace(" ", "_").replace(".", "_"))
    with open(os.path.join(path, "%s_%s.md" % (pos, fname)), "w") as f:
      f.write(vd)
