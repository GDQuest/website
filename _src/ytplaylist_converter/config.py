import os
from dotenv import load_dotenv

load_dotenv()

YT_API_KEY = os.getenv("YT_API_KEY")
YT_CHANNEL_ID = "UCxboW7x0jZqFdvMdCFKTMsQ"

DIR = "playlists"
DIR_CHAPTER = "chapter"

_SERIES = """+++
author = "nathan"
title = "{title}"
description = "{description}"
date = "{date}"

keywords = ["ENTER KEYWORDS"]

tags = [
    "free",
    "training"
]

type: "course"

banner = {{ src = "banner.png" }}

[[resources]]"
src = "banner.png"
name = "banner"
+++

"""

_CHAPTER = """+++
author = "nathan"
title = "ENTER TITLE"
description = "ENTER DESCRIPTION"

type: "course_chapter"

weight: 1
+++

"""

_VIDEO = """+++
author = "nathan"
date = "{date}"
title = "{title}"
description = "{description}"

type: "video"

videoid = "{video_id}"
+++

"""


FRONTMATTER = {
    "series": _SERIES,
    "chapter": _CHAPTER,
    "video": _VIDEO,
}
