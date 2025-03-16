#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fixes filesize"""


import json
import os
from warnings import filterwarnings as filter_warnings


def t(title: str):
    if title:
        title = title[0].upper() + title[1:]
        title = title.replace("Doml #", "DOML #")
    return title


def main() -> int:
    """entry / main function"""

    with open("media/media.json", "r") as fp:
        media = json.load(fp)

    for h in media:
        media[h]["size"] = os.path.getsize(f"media/{h}.{media[h]['ext']}")

    with open("media/media.json", "w") as fp:
        json.dump(media, fp, indent=2)

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
