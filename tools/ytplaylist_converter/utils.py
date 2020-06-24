import os
import re

import config as cfg


def sanitize_title(title):
    string = title.lower().replace(" ", "-").replace(".", "-")
    string = re.sub(
        r"[_:,/?]|(\[.*\])|(\(.*\))",
        "",
        string,
    )
    return re.sub(r"-+", "-", string, flags=re.DOTALL)


def get_base_path(args, playlist):
    title = sanitize_title(args.title or playlist.snippet.title)
    path = os.path.join(
        args.path or os.path.join(cfg.DIR, playlist.id),
        os.path.join("content", "tutorial") if args.path else "",
    )
    if args.folders is not None:
        path = os.path.join(path, *args.folders)
        path = os.path.join(path, title)
    return path
