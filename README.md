# [blog.ari.lt](https://blog.ari.lt/)

> The Ari-web blog.

## Installing dependencies

The blog generator has two dependency files - `requirements.txt` and `requirements-extra.txt`. The normal requirements file must *always* be installed such as:

    pip install -r requirements.txt

And the `-extra` requirements file only needs to be installed when you are using commands such as `new` to write blog posts. The normal requirements file is tailored to provide a minimal dependency tree for CI/CD servers.

## Creating a new blog

To create a new blog (not blog post) run

    ./scripts/blog.py blog

This will generate a new empty `blog.json`  which you can edit and adjust to your needs

### Writing a new blog post

After you've set up `blog.json` you can proceed to write a new blog post using the `new` subcommand:

    ./scripts/blog.py new

This will allow you to write blog posts in markdown as well as ask you for metadata.

## Building

- A full-on static website (recommended): `CI=1 ./scripts/blog static`
- Only blog posts: `CI=1 ./scripts/blog build`

The `CI` environment variable is optional, although setting it in a build/CI environment is good to save time on some operations that are useless in that context, for example sorting blog posts or massive logging.

Furthermore, if you want to disable colour support you can also set `NOCLR=1` and it will print things in plain text over a coloured output.

## The API

`recents.json`, `blog.json`, and `media/media.json` are all APIs you can use. For caching purposes SHA256 digests of these static APIs are generated on build at `recents_json_hash.txt`, `blog_json_hash.txt`, and `media/media_json_hash.txt` which you can use to optimise your API usage.

## Help

    help -- print help
    sort -- sort blog posts by creation time
    new -- create a new blog post
    ls -- list all posts
    ed -- edit posts
    med -- minor edit posts
    rm -- remove posts
    build -- build blog posts
    css -- build and minify css
    robots -- generate a robots.txt
    manifest -- generate a manifest.json
    sitemap -- generate a sitemap.xml
    rss -- generate an rss feed
    apis -- generate and hash apis
    clean -- clean up the site
    static -- generate a full static site
    serve -- simple server
    dev -- generate a full static site + serve it
    blog -- generate a new blog
    search -- search for a term
    media -- add media
    lsmedia -- list media
    rmmedia -- remove media
    purgemedia -- purge unused or unindexed media
    infomedia -- get info about media

    Custom markdown extensions (besides the well-known ones):

    * Titlelink: <#:Your Header Title> - links to a header
    * Media embed: <@:e3b0c4429...> - embeds media
