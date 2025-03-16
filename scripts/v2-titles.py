#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""changes titles to be capitalised"""


import json
from warnings import filterwarnings as filter_warnings


def t(title: str):
    if title:
        title = title[0].upper() + title[1:]
        title = title.replace("Doml #", "DOML #")
    return title


def main() -> int:
    """entry / main function"""

    with open("blog.json", "r") as fp:
        blog = json.load(fp)

    for slug in blog["posts"]:
        blog["posts"][slug]["title"] = t(blog["posts"][slug]["title"])

    with open("blog.json", "w") as fp:
        json.dump(blog, fp, indent=4)

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
