#!/usr/bin/env sh

set -xe

main() {
    python3 scripts/blog.py clean
    python3 scripts/blog.py purgemedia

    git diff >/tmp/ari-web-blog.diff

    git add -A
    git commit -s
    git push -u origin "$(git rev-parse --abbrev-ref HEAD)"
}

main "$@"
