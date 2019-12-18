import os
import re

import config as cfg


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
